import cv2
import numpy as np


videos_data = np.load('videoframeprediction\mnist_test_seq.npy')


for video in videos_data:
   
    for frame in video:
       
        cv2.imshow('Frame', frame)
        
       
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break


cv2.destroyAllWindows()