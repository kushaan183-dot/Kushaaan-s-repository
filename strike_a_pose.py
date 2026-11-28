# STRIKE A POSE: a pose appears on screen. Copy it with your body and hold it for 1 second to score.
# Run it from this folder:  python strike_a_pose.py      (movenet.onnx and requirements.txt must sit next to this file)
# Lines marked (given) are done for you. Your job is TODO 1 to TODO 4. Do them in order, and run the program after each one.
# Keys in the camera window: r = play again   q or Esc = quit (or close the window)
# Errors appear in this terminal, not in the camera window.

import os
import random
import subprocess
import sys
import time

# (given) A: install the three packages if they are missing, then load them.
HERE = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--disable-pip-version-check", "-r", os.path.join(HERE, "requirements.txt")])
import cv2                                          # opencv-python, numpy and onnxruntime: installed by the line above
import numpy as np
import onnxruntime

# (given) B: the five poses as 4 arm angles in degrees (left upper arm, left forearm, right upper arm, right forearm),
#   the game settings, the AI model (MoveNet), the 12 bones that join the 17 points, and the colours.
POSES = {"Arms up!": [-90, -90, -90, -90], "T-pose!": [180, 180, 0, 0], "Right arm up!": [90, 90, -90, -90],
         "Left arm up!": [-90, -90, 90, 90], "Strong arms!": [180, -90, 0, -90]}   # arm angles: left upper, left lower, right upper, right lower
SECONDS, HOLD = 10, 1.0                             # seconds for each pose, and how long to hold it
model = onnxruntime.InferenceSession(os.path.join(HERE, "movenet.onnx"))     # MoveNet: finds 17 body points
BONES = [(5, 7), (7, 9), (6, 8), (8, 10), (5, 6), (5, 11), (6, 12), (11, 12), (11, 13), (13, 15), (12, 14), (14, 16)]
FONT, WHITE, YELLOW, GREEN = cv2.FONT_HERSHEY_SIMPLEX, (255, 255, 255), (0, 255, 255), (0, 200, 0)


def find_body(frame):
    side = max(frame.shape[:2])
    square=cv2.copyMakeBorder(frame, 0, side - frame.shape[0], 0, side - frame.shape[1], cv2.BORDER_CONSTANT)
    x=cv2.cvtColor(cv2.resize(square,(192,192)),cv2.COLOR_BGR2RGB).astype(np.int32)[None]
    return [(px*side,py*side,sure) for py, px, sure in model.run(None, {"input": x})[0][0,0]]


def match(points, target):
    if min(points[i][2] for i in (5, 6, 7, 8, 9, 10)) < 0.3:   # if any arm point is not sure, return 0
        return 0
    differences=[abs((a-t+180)%360-180) for a, t in zip(arm_angles(points), target)]
    return max(0, 100 - 2 * sum(differences))                 

def arm_angles(points):
    left,right=((5,6,9),(6,8,10)) if points[5][0]<points[6][0] else ((6,5,10),(5,7,9))
    return [np.degrees(np.arctan2(points[b][1]-points[a][1],points[b][0]-points[a][0])) for a, b in [*zip(left,left[1:]),*zip(right,right[1:])]]

# (given) C: draw a small stick figure of the pose to copy, top right of the window.
def draw_target(view, angles):                      # a small stick figure of the pose to copy, top right
    x, y = view.shape[1] - 80, 150
    cv2.rectangle(view, (x - 76, y - 70), (x + 76, y + 80), (40, 40, 40), -1)
    cv2.circle(view, (x, y - 42), 11, WHITE, 2)
    cv2.polylines(view, [np.array([(x - 20, y - 22), (x + 20, y - 22)]), np.array([(x, y - 22), (x, y + 30)])], False, WHITE, 3)
    step = lambda point, angle: (int(point[0] + 26 * np.cos(np.radians(angle))), int(point[1] + 26 * np.sin(np.radians(angle))))
    for shoulder, (upper, lower) in (((x - 20, y - 22), angles[:2]), ((x + 20, y - 22), angles[2:])):   # each arm: shoulder, elbow, hand
        cv2.polylines(view, [np.array([shoulder, step(shoulder, upper), step(step(shoulder, upper), lower)])], False, YELLOW, 4)


# (given) D: start the camera and the game: the poses in a random order, the turn, the score and the timers.
video = cv2.VideoCapture(0)
order, turn, score, held_since, nice_until, deadline = random.sample(list(POSES), len(POSES)), 0, 0, None, 0, time.time() + SECONDS
while True:
    # (given) E: read a frame, mirror it like a selfie, find the body, and draw every bone whose two points are sure.
    ok, frame = video.read()
    if not ok:
        break
    view = cv2.flip(frame, 1)
    points = find_body(view)
    for a, b in BONES:                              # the body the AI found: 17 points joined into a skeleton
        if points[a][2] > 0.3 and points[b][2] > 0.3:
            cv2.line(view, (int(points[a][0]), int(points[a][1])), (int(points[b][0]), int(points[b][1])), YELLOW, 4)
    if turn<len(order):
        percent=match(points,POSES[order[turn]])
        held_since=(held_since or time.time()) if percent>=80 else None
        if (held_since and time.time() if held_since >= HOLD else None) or time.time() > deadline:
            if held_since:
                score, nice_until = score+1, time.time()+ 0.8
                cv2.imwrite(os.path.join(HERE, time.strftime("pose_%H%M%S.jpg")), view)
                turn, held_since, deadline=turn + 1,None,time.time()+SECONDS
        cv2.rectangle(view, (0, 0), (view.shape[1], 60), (30, 30, 30), -1)
    
        if turn < len(order):
            cv2.putText(view,order[turn],(15,42),FONT,1.2,YELLOW,3)
            cv2.putText(view,f"{max(0,int(deadline-time.time()))}s score={score}/{len(order)}")
            cv2.rectangle(view,(15,70),(15+int(3*percent),85),GREEN if percent>=80 else (0,140,255)-1)
            cv2.putText(view, "Hold it!" if held_since else f"match (percent:.0f)%", (330, 84), FONT, 0.6,WHITE, 2)
            draw_target(view, POSES [order[turn]])
        else:
            veiw=view//3
            cv2.putText(view, f"You scored {score} of {len(order)}!", (40, view.shape[0] // 2), FONT, 1.4,YELLOW, 3)
            cv2.putText(view, "r play again q quit", (40, view.shape[0] // 2 +50), FONT, 0.8, WHITE, 2)
        if time.time() < nice_until:
            cv2.rectangle(view, (0, 0), (view.shape[1]-1).GREEN,14)
            cv2.putText(view,"Nice!",(view.shape[1]//2-70,view.shape[0]//2),FONT,2,GREEN,5)
        cv2.imshow("STRIKE a pose",view)
        key=chr(cv2.waitKey(1) & 255).lower()
    if turn < len(order):
        cv2.putText(view, order[turn], (15, 42), FONT, 1.2, YELLOW, 3)
        cv2.putText(view, f"{max(0, int(deadline - time.time()))} s    score {score}/{len(order)}", (view.shape[1] - 250, 40), FONT, 0.8, WHITE, 2)
        cv2.rectangle(view, (15, 70), (15 + int(3 * percent), 85), GREEN if percent >= 80 else (0, 140, 255), -1)
        cv2.putText(view, "Hold it!" if held_since else f"match {percent:.0f}%", (330, 84), FONT, 0.6, WHITE, 2)
        draw_target(view, POSES[order[turn]])
    else:
        view = view // 3
        cv2.putText(view, f"You scored {score} of {len(order)}!", (40, view.shape[0] // 2), FONT, 1.4, YELLOW, 3)
        cv2.putText(view, "r play again    q quit", (40, view.shape[0] // 2 + 50), FONT, 0.8, WHITE, 2)
    # (given) G: the green "Nice!" flash, then show the picture.
    if time.time() < nice_until:
        cv2.rectangle(view, (0, 0), (view.shape[1] - 1, view.shape[0] - 1), GREEN, 14)
        cv2.putText(view, "Nice!", (view.shape[1] // 2 - 70, view.shape[0] // 2), FONT, 2, GREEN, 5)
    cv2.imshow("Strike a Pose", view)
    # (given) H: the keys. Every key is made lowercase, so Caps Lock does not matter. r starts a new game.
    key = chr(cv2.waitKey(1) & 255).lower()
    if key in ("q", "\x1b") or cv2.getWindowProperty("Strike a Pose", cv2.WND_PROP_VISIBLE) == 0:
        break
    if key == "r":
        order, turn, score, held_since, deadline = random.sample(list(POSES), len(POSES)), 0, 0, None, time.time() + SECONDS
video.release()
cv2.destroyAllWindows()
