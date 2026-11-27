# ================================
# ID CARD CUT-OUT
# ================================

# ---------- SETUP (given to you) ----------
import cv2
import numpy as np

photo = np.full((120, 100, 3), 180, np.uint8)                 # a grey classroom wall
cv2.rectangle(photo, (30, 60), (70, 120), (40, 90, 220), -1)  # the student's shirt
cv2.circle(photo, (50, 40), 18, (150, 180, 220), -1)          # the student's face
cv2.rectangle(photo, (80, 10), (95, 30), (60, 60, 60), -1)    # a poster of a person on the wall

person = np.zeros((120, 100), np.float32)                     # what a perfect AI would say
cv2.rectangle(person, (30, 60), (70, 120), 1.0, -1)
cv2.circle(person, (50, 40), 18, 1.0, -1)
matte = cv2.GaussianBlur(person, (7, 7), 0)                   # soft edges, like a real matte
matte[35:45, 42:58] = 0.45                                    # the AI was unsure here (a hand near the face)
matte[10:31, 80:96] = 0.9                                     # the AI thinks the poster is a person too
blue = np.zeros((120, 100, 3), np.uint8)
blue[:] = (200, 120, 40)                                      # the ID card's blue background
print("Photo", photo.shape, "matte", matte.shape)

# ---------- PART 1: read the matte ----------
print("\nPART 1: Read the matte")
sure = int(np.count_nonzero(matte >= 0.8))
unsure = int(np.count_nonzero((matte >= 0.2) & (matte < 0.8)))
room = int(np.count_nonzero(matte < 0.2))
print(sure, unsure, room)

# ---------- PART 2: keep only the student ----------
print("\nPART 2: Keep only the student")
patches = (matte > 0.35).astype(np.uint8)
patch_count, labels, stats, _ = cv2.connectedComponentsWithStats(patches, 8)

largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
largest_patch = (labels == largest_label).astype(np.uint8)
contours, _ = cv2.findContours(
    largest_patch, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
body = np.zeros_like(largest_patch)
cv2.drawContours(body, contours, -1, 1, thickness=cv2.FILLED)
print(patch_count - 1, int(np.count_nonzero(body)))

# ---------- PART 3: paste onto the ID card ----------
print("\nPART 3: ID card")
body_float = body.astype(np.float32)
card = (
    photo.astype(np.float32) * body_float[:, :, None]
    + blue.astype(np.float32) * (1.0 - body_float[:, :, None])
).astype(np.uint8)
print(card[50, 40])
print(card[88, 20])
print(card[0, 0])

# ---------- PART 4: the ghost ----------
print("\nPART 4: Raw matte against cleaned")
ghost = (
    photo.astype(np.float32) * matte[:, :, None]
    + blue.astype(np.float32) * (1.0 - matte[:, :, None])
).astype(np.uint8)
print(ghost[50, 40], card[50, 40])
