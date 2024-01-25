from ultralytics import YOLO
import cv2
 
model = YOLO('yolov8m.pt')
results = model("Demo/img/1.jpeg", show=True)
cv2.waitKey(0)



'''
 YOLOv8 may be used directly in the Command Line Interface (CLI) with a yolo


$ yolo predict model=yolov8n.pt source='"Demo/img/1.jpeg"


 runs
 └── detect
      └── predict
          └── 1.jpeg


$ open runs/detect/predict/1.jpeg


'''
