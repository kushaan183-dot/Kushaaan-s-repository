import cv2
import numpy as np
import matplotlib.pyplot as plt
def display_image(title,image):
    """Utility function to display an image"""
    plt.figure(figsize=(8,8))
    if len(image.shape)=2:
        plt.imshow(image,cmap="grey")
    else:
        plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
def interactive_edge_detection(image_path):
    """Interactive edge display system"""
    image=cv2.imread(image_path)
    if image is none:
        print("error here is no image!")
        grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        display_image("Original greyscale image",grey_image)
        print("Select an option:")
        print("1.Sorbel edge detection")
        print("2.Canny edge detection")
        print("3.Laplacian edge detection")
        print("4.Gaussian smoothening")
        print("5.Median filtering")
        print("6.Exit")
        while True:
            choice=input("Enter your choice(1-6):")
            if choice=="1":
                sorbel_x=cv2.Sorbel(grey_image,cv2.CV2_64F,1,0,ksize=3)
                sorbel_y=cv2.Sorbel(grey_image,cv2.CV2_64F,0,1,ksize=3)
                combined_sorbel=cv2.bitwise_or(sorbel_x.astype(np.uint8),sorbel_y.astype(np.uint8))
                display_image("Sorbel Edge Detection",combined_sorbel)
            elif choice=="2":
                print("Adjust thresholds for canny (default: 100 and 200)")
                lower_thresh=int(input("Enter Lower threshhold:"))
                upper_thresh=int(input("Enter upper threshhold:"))
                edges=cv2.Canny(grey_image,lower_thresh,upper_thresh)
                display_image("Canny edge detection",edges)
            elif choice=="3":
                laplacian=cv2.Laplacian(grey_image,cv2.CV2_64F)
                display_image("Laplacian edge detecton",np.abs(laplacian).astype(np.uint8))
interactive_edge_detection('examplr_of_rotation.jpg')