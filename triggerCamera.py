import serial
import cv2

ser = serial.Serial('COM3', 9600)  # Adjust COM port
camera = cv2.VideoCapture(0)

while True:
    line = ser.readline().decode().strip()
    if line == "Person Left":
        print("Opening camera...")
        ret, frame = camera.read()
        if ret:
            cv2.imshow("Camera Feed", frame)
            cv2.waitKey(3000)  # Show for 3 seconds
            cv2.destroyAllWindows()
