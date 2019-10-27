from imageai.Detection import ObjectDetection
detector = ObjectDetection()

model_path = "./models/yolo.h5"
input_path = "./input/test45.jpg"
input_path = "./input/breakwaterFull.jpg"
output_path = "./output/breakwaterFull.jpg"

detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path,
minimum_percentage_probability=30)

not_allowed=['airplane','bicycle']
count=0
for x in detection:
    if x['name'] not in not_allowed:
        count=count+1

print(f'''Number of objects detected: {count}''')
#1:08
https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream.20191027T200823457.mp4
#12:58
https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream.20191027T195822005.mp4
#12:48
https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream.20191027T194820283.mp4

#for eachItem in detection:
#    print(eachItem["name"] , " : ", eachItem["percentage_probability"])