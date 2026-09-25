import cv2
import matplotlib.pyplot as plt
image_path="examples_of_rotation.jpg"
image=cv2.imread(image_path)
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,_=image_rgb.shape
rect1_width,rect1_height=150,150
top_left1=(20,20)
bottem_right1=(top_left1[0]+rect1_width,top_left1[1]+rect1_height)
cv2.rectangle(image_rgb,top_left1,bottem_right1,(0,255,255),3)
rect2_width,rect2_height=150,150
top_left2=(width-rect2_width-20,height-rect2_height-20)
bottem_right2=(top_left2[0]+rect2_width,top_left2[1]+rect2_height)
cv2.rectangle(image_rgb,top_left2,bottem_right2,(255,255,0),3)
center1_x=top_left1[0]+rect1_width//2
center1_y=top_left1[0]+rect1_height//2
center2_x=top_left2[0]+rect2_width//2
center2_y=top_left2[0]+rect2_height//2
cv2.circle(image_rgb, (center1_x,center1_y),15,(0,255,255),-1)
cv2.circle(image_rgb, (center2_x,center2_y),15,(0,255,255),-1)
plt.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.axes('off')
plt.show()