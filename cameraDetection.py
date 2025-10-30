import cv2

net = cv2.dnn.readNet("yolov8.weights", "yolov8.cfg")
classes = ["wallet", "pen", "book"]
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True)
    net.setInput(blob)
    outputs = net.forward(net.getUnconnectedOutLayersNames())

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = scores.argmax()
            confidence = scores[class_id]
            if confidence > 0.5:
                print(f"Detected: {classes[class_id]}")
