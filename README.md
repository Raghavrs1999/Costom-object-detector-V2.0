# Custom Object Detector V2.0

This project is an advanced object detection application using YOLOv5, designed to detect and classify objects in real-time video streams. It features a graphical user interface for easy interaction and control over the detection process.

## Features

- Real-time object detection using YOLOv5
- Graphical user interface with selectable object classes
- Live video processing from webcam or IP camera
- Image capture and video recording capabilities
- Adjustable confidence threshold for detections
- Support for multiple object classes (based on COCO dataset)

## Requirements

To run this project, you need Python 3.7+ and the following libraries:

- OpenCV
- PyTorch
- Numpy
- torchvision

For a complete list of dependencies, see the `requirements.txt` file.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/custom-object-detector-v2.git
   cd custom-object-detector-v2
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Download the YOLOv5 model weights (if not included in the repository):
   ```
   wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5m6.pt -O dnn_model/yolov5m6.pt
   ```

## Usage

To run the object detector:

```
python "Object Detector.py"
```

### Controls:

- Click on the buttons to toggle detection for specific object classes
- Press 's' to save the current frame as an image
- Press 'r' to start recording video
- Press 'e' to stop recording video
- Press '+' to increase the confidence threshold
- Press '-' to decrease the confidence threshold
- Press 'q' or 'Esc' to quit the application

## Customization

- To add or remove object classes, modify the `classes.txt` file
- Adjust the `conf_threshold` variable in the script to change the default confidence threshold
- Modify the `cap` variable to change the video source (e.g., different camera index or IP camera address)

## Building Executable

To create a standalone executable:

```
python setup.py build
```

This will create an executable in the `build` directory.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.


## Acknowledgments

- YOLOv5 by Ultralytics
- OpenCV community

