import cv2
import matplotlib.pyplot
import colorama

def apply_color_filter(image,filter_type):
    """Apply the specified color filter to image"""
    filter_image=image.copy()
    if filter_type=="red_tint":
        filter_image[:,:,0]=0
        filter_image[:,:,1]=0
    elif filter_type=="blue_tint":
        filter_image[:,:,1]=0
        filter_image[:,:,2]=0
    elif filter_type=="green_tint":
        filter_image[:,:,0]=0
        filter_image[:,:,2]=0
    elif filter_type=="increase_red":
        filter_image[:,:,2]=cv2.add(filter_image[:,:,2], 50)
    elif filter_type=="decrease_blue":
        filter_image[:,:,0]=cv2.subtract(filter_image[:,:,0], 50)
    return filter_image
image_path='example_of_rotation.jpg'
image=cv2.imread(image_path)

if image is None:
    print(f"{Font.RED}Error: image not found")
else:
    filter_type="original"
    print("Press the folowing keys to aply the required tint")
    print("r-red tint")
    print("g-green tint")
    print("b-blue tint")
    print("i-increase red intensity")
    print("d-decrease blue intensity")
    print("q-Quit")
    while True:
        filter_image=apply_color_filter(image,filter_type)
        key=cv2.waitKey[0] & 0xFF
        if key==ord("r"):
            filter_type="red_tint"
        elif key==ord("g"):
            filter_type="green_tint"
        elif key==ord("b"):
            filter_type="blue_tint"
        elif key==ord("i"):
            filter_type="increase_red"
        elif key==ord("d"):
            filter_type="decrease_blue"
        elif key==ord("q"):
            print("Exiting")
            break
        else:
            print(f"{Font.RED}Error: Please use keys 'r','b','g','i','d' or 'q'")
cv2.destroyAllWindows()