import cv2
image=cv2.imread('example.jpg')
cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image',800,500)
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resized_image=cv2.resize(grey_image,(224,224))
cv2.imshow("Prosesed Image",resized_image)
key=cv2.waitKey(0)
if key==ord("s"):
    cv2.imwrite("greyscale_resized_image.jpg",resized_image)
else:
    print("Imaged not saved.")
cv2.destroyAllWindows()
