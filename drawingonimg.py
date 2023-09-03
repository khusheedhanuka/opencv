import cv2
import numpy as np

img=np.zeros([512,512,3],np.uint8)


# img=cv2.imread('lena.jpg',1)
img=cv2.line(img,(0,0),(255,255),(255,0,0),10)#drawing a line on the image
#can use bgr coloe picker format remember only bgr
img=cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),10)#arrow line

img=cv2.rectangle(img,(384,0),(510,128),(25,255,0), -1)
img=cv2.circle(img,(453,69),90,(255,255,255),-1)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),10,cv2.LINE_AA)
# img=cv2.ellipse2Poly((223,89),1,30)
cv2.imshow('image',img)



cv2.waitKey(0)

cv2.destroyAllWindows()