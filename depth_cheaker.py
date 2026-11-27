# ================================
# ROBOT VACUUM DEPTH CHECK
# ================================

# ---------- SETUP (given to you) ----------
import cv2
import numpy as np

raw = np.tile(np.linspace(1.0, 5.0, 60, dtype=np.float32)[:, None], (1, 80))   # the floor: bigger = nearer the robot
raw[:20, :] = 1.0                                              # the far wall of the hallway
cv2.rectangle(raw, (55, 30), (70, 50), 6.0, -1)                # a toy box close to the robot
photo = np.zeros((60, 80, 3), np.uint8)
photo[:, :, 0] = np.arange(80) * 3                             # a test picture: blue = 3 x the column number
WOBBLE = 12
print("Raw depth", raw.shape, "from", raw.min(), "to", raw.max())

# ---------- PART 1: numbers from 0 to 1 ----------
print("\nPART 1: Normalise")
near = (raw - raw.min()) / (raw.max() - raw.min() + 1e-6)
print(
    "wall", round(near[10, 40], 2),
    "floor", round(near[45, 20], 2),
    "box", round(near[40, 60], 2),
)

# ---------- PART 2: where is the obstacle? ----------
print("\nPART 2: Obstacle")
close = near > 0.85
rows, columns = np.where(close)
count = len(columns)
average_column = float(columns.mean())
if average_column < 80 / 3:
    side = "left"
elif average_column < 80 * 2 / 3:
    side = "middle"
else:
    side = "right"
print(count, side, round(average_column, 2))

# ---------- PART 3: one frame of the wobble ----------
print("\nPART 3: Parallax")
ys, xs = np.mgrid[0:raw.shape[0], 0:raw.shape[1]]
xs = xs.astype(np.float32)
ys = ys.astype(np.float32)
shift = (WOBBLE * (near - 0.5)).astype(np.float32)
moved = cv2.remap(photo, xs + shift, ys, cv2.INTER_LINEAR)
print(
    "box slide", round(shift[40, 60], 2),
    "wall slide", round(shift[10, 40], 2),
    "box column", round(moved[40, 60, 0] / 3, 2),
)

# ---------- PART 4: relative, not metres ----------
print("\nPART 4: Relative depth")
raw2 = raw * 3                                                 # the same hallway, another photo: the AI's numbers are 3 times bigger
near2 = (raw2 - raw2.min()) / (raw2.max() - raw2.min() + 1e-6)
print(raw.max(), raw2.max(), np.allclose(near, near2))
