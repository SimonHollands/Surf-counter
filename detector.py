from imageai.Detection import ObjectDetection
detector = ObjectDetection()

model_path = "./models/yolo.h5"
input_path = "./input/test45.jpg"
input_path = "./input/surfers.jpg"

output_path = "./output/bird2.jpg"

detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path,
minimum_percentage_probability=30)

print(f'''Number of objects detected: {len(detection)}''')

#for eachItem in detection:
#    print(eachItem["name"] , " : ", eachItem["percentage_probability"])