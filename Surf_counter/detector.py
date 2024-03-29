from imageai.Detection import ObjectDetection
from Surf_counter.read_video import ReadVidz
from os import listdir
from os.path import isfile, join
import os, shutil 
import imageai
from Surf_counter.spot_urls import SpotUrls
from Surf_counter.scrape_video_links import ScrapeVideoLinks

class Detect:
    model_path = "./models/yolo.h5"
    output_path = "./output/breakwaterFull.jpg"

    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()


    def __init__(self):
        self.surfimages = ['./data/'+ f for f in listdir('./data') if f[0] !='.' and isfile(join('./data', f))]
    
    #ScrapeVideoLinks
    def pull_images(self,link):
        '''Pull images from video'''
        r=ReadVidz(link)
        r.pull_frames(5)
        self.surfimages = ['./data/'+ f for f in listdir('./data') if f[0] !='.' and isfile(join('./data', f))]

    def clear_data_dir(self):
        folder = './data'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        self.surfimages = ['./data/'+ f for f in listdir('./data') if f[0] !='.' and isfile(join('./data', f))]


    def detection(self):
        print("Images")
        print (self.surfimages)
        print("Input image is "+ self.surfimages[0])
 
        detection_ = self.detector.detectObjectsFromImage(input_image=self.surfimages[0],output_image_path=self.output_path,
        minimum_percentage_probability=30)

        not_allowed=['airplane','bicycle']
        count=0
        for x in detection_:
            if x['name'] not in not_allowed:
                count=count+1

        return count


det=Detect()
# det.clear_data_dir()
# #Find the video
# url=SpotUrls.lookup['venice_beach']
# v=ScrapeVideoLinks(url)
# link=v.get_link()
# print("LINK:")
# print(link)
# det.pull_images(link)
surfer_count=det.detection()
# # #surfer_count = 10
output=f'''There are currently {surfer_count} surfers at the Breakwater'''
# print(output)

# det=Detect()
# #Find the video
# url=SpotUrls.lookup['venice_beach']
# url=SpotUrls.venice2
# v=ScrapeVideoLinks(url)
# link=v.get_link()
# det.pull_images(link)
# n_surfers=det.detection()



# print("link:")
# print (link)
# det.pull_images(link)
# n_surfers=det.detection()
# print(f'''There are {n_surfers} surfers''')
#  https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream.20191027T235900139.mp4
# #1:08
# https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream.20191027T200823457.mp4
# #12:58
# https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream.20191027T195822005.mp4
# #12:48
# https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream.20191027T194820283.mp4

#for eachItem in detection:
#    print(eachItem["name"] , " : ", eachItem["percentage_probability"])