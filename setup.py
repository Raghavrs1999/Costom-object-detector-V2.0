import sys
from cx_Freeze import setup, Executable


setup(name="Custom Object Detection Software version 2.0",
      version="2.0",
      description="This is the object detection software version 2.0 upgraded then its prior version. "
      "Now it have the functionality adjusting the threshold and to save the images as well as the video according to the user requirement",
      executables=[Executable("Object Detector.py")]
      )

