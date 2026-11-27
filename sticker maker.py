# ================================
# STICKER SHOP
# ================================

# ---------- SETUP (given to you) ----------
import cv2
import numpy as np

photo = np.full((256, 512, 3), (200, 210, 220), np.uint8)            # a light table
cv2.circle(photo, (256, 150), 80, (40, 40, 200), -1)                 # a red apple
cv2.ellipse(photo, (300, 58), (30, 14), -30, 0, 360, (60, 170, 60), -1)  # its green leaf
cv2.rectangle(photo, (420, 30), (500, 110), (150, 110, 70), -1)      # a blue mug behind it
clicks = [(256, 150, 1), (460, 60, 0)]                               # click: the apple. Right-click: the mug.

guesses = np.full((3, 256, 256), -4.0, np.float32)                   # SAM's 3 guesses (256 x 256), in no order
cv2.ellipse(guesses[0], (128, 150), (40, 80), 0, 0, 360, 4.0, -1)    # the apple without its leaf
cv2.ellipse(guesses[1], (128, 150), (10, 20), 0, 0, 360, 4.0, -1)    # only a shiny spot on the apple
cv2.ellipse(guesses[2], (128, 150), (40, 80), 0, 0, 360, 4.0, -1)    # the apple with its leaf
cv2.ellipse(guesses[2], (150, 58), (15, 14), -30, 0, 360, 4.0, -1)
print("Photo", photo.shape, "guesses", guesses.shape)

# ---------- PART 1: clicks to prompts ----------
print("\nPART 1: Prompts for SAM")
points = np.array(
    [[x * 2, y * 4] for x, y, _ in clicks],
    dtype=np.float32,
)
labels = np.array([label for _, _, label in clicks], dtype=np.int64)
print(points.tolist())
print(labels.tolist())
print("point", points.shape, "box", points.shape)
print("label", labels.shape)
print("SAM shapes", list(points[None, None].shape), list(labels[None, None].shape))

# ---------- PART 2: sort the guesses ----------
print("\nPART 2: Part, bigger, whole")
ordered = sorted(guesses, key=lambda guess: np.count_nonzero(guess > 0))
sizes = [int(np.count_nonzero(guess > 0)) for guess in ordered]
print(sizes)

# ---------- PART 3: the whole apple, photo-sized ----------
print("\nPART 3: Mask")
biggest = ordered[-1]
resized = cv2.resize(
    biggest,
    (photo.shape[1], photo.shape[0]),
    interpolation=cv2.INTER_LINEAR,
)
mask = (resized > 0).astype(np.uint8)
print(mask.shape, int(np.count_nonzero(mask)))

# ---------- PART 4: the sticker ----------
print("\nPART 4: Sticker")
ys, xs = np.where(mask)
x1, x2 = int(xs.min()), int(xs.max())
y1, y2 = int(ys.min()), int(ys.max())
box = (x1, y1, x2, y2)

alpha = cv2.GaussianBlur(
    (mask * 255).astype(np.uint8),
    (3, 3),
    0,
)
sticker = np.dstack((photo, alpha))[y1:y2 + 1, x1:x2 + 1]

print(box)
print(sticker.shape)
middle_alpha = alpha[(y1 + y2) // 2, (x1 + x2) // 2]
print("middle alpha", int(middle_alpha), "top-left alpha", int(alpha[y1, x1]))
cv2.imwrite("sticker.png", sticker)
