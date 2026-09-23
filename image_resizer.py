import cv2
image=cv2.imread('example.jpg')
cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL)
small=cv2.resizeWindow('Loaded Image',200,200)
normal=cv2.resizeWindow('Loaded Image',400,400)
large=cv2.resizeWindow('Loaded Image',600,600)
cv2.imshow("Large image",large)
cv2.imshow("Normal image",normal)
cv2.imshow("Small image",small)
key=cv2.waitKey[0]
if key==ord("s"):
    cv2.imwrite("Small_size_image.jpg",small)
    cv2.imwrite("Normal_size_image.jpg",normal)
    cv2.imwrite("Large_size_image.jpg",large)
else:
    print("Imaged not saved.")
cv2.destroyAllWindows()