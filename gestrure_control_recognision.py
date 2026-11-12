"""Use hand pinches to capture photos and switch live image filters."""

from datetime import datetime
from pathlib import Path
import time

import cv2
import mediapipe as mp
import numpy as np


FILTERS = ("GRAYSCALE", "SEPIA", "NEGATIVE", "BLUR")
FINGER_TIPS = {
    "index": mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP,
    "middle": mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP,
    "ring": mp.solutions.hands.HandLandmark.RING_FINGER_TIP,
    "pinky": mp.solutions.hands.HandLandmark.PINKY_TIP,
}
PALM_LANDMARKS = (
    mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP,
    mp.solutions.hands.HandLandmark.PINKY_MCP,
)
THUMB_TIP = mp.solutions.hands.HandLandmark.THUMB_TIP
TOUCH_RATIO = 0.3
GESTURE_DEBOUNCE_SECONDS = 1.0
PHOTO_DIRECTORY = Path(__file__).resolve().parent / "captured_photos"
SEPIA_MATRIX = np.array(
    [
        [0.131, 0.534, 0.272],
        [0.168, 0.686, 0.349],
        [0.189, 0.769, 0.393],
    ],
    dtype=np.float32,
)


def apply_filter(frame, filter_name):
    """Return a filtered BGR image without modifying the input frame."""
    if filter_name == "GRAYSCALE":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    if filter_name == "SEPIA":
        return np.clip(cv2.transform(frame, SEPIA_MATRIX), 0, 255).astype(
            np.uint8
        )
    if filter_name == "NEGATIVE":
        return cv2.bitwise_not(frame)
    if filter_name == "BLUR":
        return cv2.GaussianBlur(frame, (21, 21), 0)
    raise ValueError(f"Unknown filter: {filter_name}")


def detect_touch(hand_landmarks, finger, frame_width, frame_height):
    """Check whether the thumb is close to a fingertip relative to palm width."""
    points = hand_landmarks.landmark
    thumb = points[THUMB_TIP]
    fingertip = points[FINGER_TIPS[finger]]
    index_mcp = points[PALM_LANDMARKS[0]]
    pinky_mcp = points[PALM_LANDMARKS[1]]

    thumb_xy = (thumb.x * frame_width, thumb.y * frame_height)
    finger_xy = (fingertip.x * frame_width, fingertip.y * frame_height)
    index_xy = (index_mcp.x * frame_width, index_mcp.y * frame_height)
    pinky_xy = (pinky_mcp.x * frame_width, pinky_mcp.y * frame_height)

    palm_width = float(np.hypot(index_xy[0] - pinky_xy[0], index_xy[1] - pinky_xy[1]))
    if palm_width == 0:
        return False

    fingertip_distance = float(
        np.hypot(thumb_xy[0] - finger_xy[0], thumb_xy[1] - finger_xy[1])
    )
    return fingertip_distance / palm_width < TOUCH_RATIO


def current_gesture(hand_landmarks, frame_width, frame_height):
    """Return the active thumb-touch gesture, preferring the photo pinch."""
    if detect_touch(hand_landmarks, "index", frame_width, frame_height):
        return "index"

    for finger in ("middle", "ring", "pinky"):
        if detect_touch(hand_landmarks, finger, frame_width, frame_height):
            return finger
    return None


def main():
    hands_module = mp.solutions.hands
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        camera.release()
        raise RuntimeError("Could not open the webcam.")

    filter_index = 0
    last_action_time = float("-inf")
    previous_gesture = None
    feedback = "Show your hand"
    feedback_until = 0.0

    try:
        PHOTO_DIRECTORY.mkdir(parents=True, exist_ok=True)
        with hands_module.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7,
        ) as hands:
            while True:
                ok, frame = camera.read()
                if not ok:
                    raise RuntimeError("Could not read a frame from the webcam.")

                frame = cv2.flip(frame, 1)
                height, width = frame.shape[:2]
                result = hands.process(
                    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                )
                gesture = None
                hand_landmarks = None

                if result.multi_hand_landmarks:
                    hand_landmarks = result.multi_hand_landmarks[0]
                    gesture = current_gesture(hand_landmarks, width, height)

                now = time.monotonic()
                if (
                    gesture is not None
                    and gesture != previous_gesture
                    and now - last_action_time >= GESTURE_DEBOUNCE_SECONDS
                ):
                    if gesture == "index":
                        filtered_frame = apply_filter(frame, FILTERS[filter_index])
                        filename = (
                            "photo_"
                            + datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                            + ".jpg"
                        )
                        photo_path = PHOTO_DIRECTORY / filename
                        if not cv2.imwrite(str(photo_path), filtered_frame):
                            raise OSError(f"Could not save photo: {photo_path}")
                        feedback = f"Photo saved: {filename}"
                        print(f"Saved photo: {photo_path}")
                    else:
                        filter_index = (filter_index + 1) % len(FILTERS)
                        feedback = f"Filter changed to {FILTERS[filter_index]}"
                    last_action_time = now
                    feedback_until = now + 2.5

                previous_gesture = gesture
                display = apply_filter(frame, FILTERS[filter_index])
                if hand_landmarks is not None:
                    mp.solutions.drawing_utils.draw_landmarks(
                        display,
                        hand_landmarks,
                        hands_module.HAND_CONNECTIONS,
                    )

                cv2.putText(
                    display,
                    f"Filter: {FILTERS[filter_index]}",
                    (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                )
                message = feedback if now < feedback_until else (
                    "Index: photo | Middle/Ring/Pinky: next filter"
                )
                cv2.putText(
                    display,
                    message,
                    (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.55,
                    (0, 255, 255),
                    2,
                )
                cv2.putText(
                    display,
                    "Press Q or Esc to quit",
                    (20, height - 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.55,
                    (255, 255, 255),
                    1,
                )
                cv2.imshow("Hand Gesture Filters", display)

                key = cv2.waitKey(1) & 0xFF
                if key in (ord("q"), 27):
                    break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()