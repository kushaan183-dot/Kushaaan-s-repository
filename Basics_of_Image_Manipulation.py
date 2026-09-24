import cv2
import matplotlib.pyplot as plt
image=cv2.imread("example.jpg")
plt.imshow(image)
plt.show()
cropped_image=image[100:300, 200:400]
cropped_rgb=cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_image)
plt.title("Cropped Region")
plt.show()