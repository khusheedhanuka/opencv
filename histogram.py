import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('lena.jpg',0)
# img=np.zeros((200,200),np.uint8)
# cv2.rectangle(img,(0,100),(200,200),(255),-1)


cv2.imshow("img",img)


# plt.hist(img.ravel(),256,[0,256])
# plt.show()

hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()


cv2.waitKey(0)

cv2.destroyAllWindows()