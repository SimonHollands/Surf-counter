# Importing all necessary libraries 
import cv2 
import os 
  
# Read the video from specified path 


class ReadVidz:

    def __init__(self,cam_link):
        self.cam_link=cam_link
        self.cam = cv2.VideoCapture(self.cam_link)
        self.frame_count= int(self.cam.get(cv2.CAP_PROP_FRAME_COUNT))


    def pull_frames(self,how_many=10):
                currentframe = 0
                #import pytest
                #pytest.set_trace()
                print("Boo")
                while(currentframe<=self.frame_count): 
                    
                    # reading from frame 
                    ret,frame = self.cam.read()                 
                    if ret:
                        currentframe += 1
                        if currentframe%(int(self.frame_count/how_many))==0:
                            # if video is still left continue creating images 
                            name = './data/frame' + str(currentframe) + '.jpg'
                            print ('Creating...' + name) 
                    
                            # writing the extracted images 
                            cv2.imwrite(name, frame) 
                    
                            # increasing counter so that it will 
                            # show how many frames are created 
                            
                    else: 
                        break
                            

    # Release all space and windows once done 

#r=ReadVideoS("https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream.20191027T211834705.mp4")#reader.pull_frames(how_many=10)
#r.pull_frames()
#cam.release() 
#cv2.destroyAllWindows() 
