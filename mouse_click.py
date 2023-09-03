import cv2
import numpy as np



def event_click(event ,x,y,flag,para):
    if event==cv2.EVENT_LBUTTONDOWN:
        font=cv2.FONT_HERSHEY_COMPLEX
        text=str(x)+','+str(y)
        cv2.putText(img,text,(x,y),font,1,(255,0,0),2)
        cv2.imshow('image', img)


img=np.zeros((512,512,4),np.uint8)
cv2.imshow('image',img)


cv2.setMouseCallback('image',event_click)

cv2.waitKey(0)

cv2.destroyAllWindows()



