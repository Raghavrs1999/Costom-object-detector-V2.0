import cv2
from gui_buttons import Buttons
import os
import torch

# Initialize Buttons
button = Buttons()
button.add_button("person", 20, 20)
button.add_button("phone", 20, 100)
button.add_button("clock", 20, 180)
button.add_button("cat", 1120, 20)
button.add_button("dog", 1111, 100)
button.add_button("chair", 1080, 180)


if not os.path.exists("images"):
    os.makedirs("images")
count = 0
out = None
recording = False

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

colors = button.colors

model = torch.hub.load('ultralytics/yolov5', 'custom', path='dnn_model/yolov5s.pt')


# Load class lists
classes = []
with open('dnn_model/classes.txt', 'r', encoding='utf8') as f:
    classes = {i: line.strip() for i, line in enumerate(f)}

#print("Objects list")
#print(classes)
print("Loading...")

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def click_button(event, x, y, flags, params):
    global button_person
    if event == cv2.EVENT_LBUTTONDOWN:
        button.button_click(x, y)

# Create window
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click_button)

# Confidence threshold for object detection
conf_threshold = 0.3

while True:
    # Get frames
    ret, frame = cap.read()

    # Get active buttons list
    active_buttons = button.active_buttons_list()

    # Object Detection
    results = model(frame)

    # Loop through detected objects
    for result in results.xyxy[0]:
        class_id = int(result[5])
        class_name = classes[class_id]
        confidence = float(result[4])


        if class_name in active_buttons and confidence > conf_threshold :
            x1, y1, x2, y2 = map(int, result[:4])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (125, 150, 175), 2)
            confidence = confidence * 100
            # Add label to bounding box
            label = f"{class_name} {confidence:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_PLAIN, 2, (125, 150, 175), 4)

    # Display buttons
    button.display_buttons(frame)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

    if key == 27 or key == ord("q"): #exit
        if recording == True :
            print("Recording stopped!")
            out.release()
            recording = False
        break
    if key == ord("s"): # to save image
        count += 1
        cv2.imwrite(f"images/image_{count}.jpg", frame)

    if key == ord("r") and not recording:  #recording video
        print("Recording started!")
        out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (1280, 720))
        recording = True
    elif recording:
        out.write(frame)

    # Stop recording
    if key == ord("e") and recording:
        print("Recording stopped!")
        out.release()
        recording = False

    if key == ord('+'):
        if conf_threshold<.9:
            conf_threshold += 0.1
            print(f"Confidence threshold increased to {conf_threshold:.1f}")
    elif key == ord('-'):
        conf_threshold -= 0.1
        if conf_threshold < 0:
            conf_threshold = 0
        print(f"Confidence threshold decreased to {conf_threshold:.1f}")
print("Closing...")
cap.release()
cv2.destroyAllWindows()