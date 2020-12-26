# UpLift
### Overview:
A mood changer that plays a song to positively change someone's mood based on their facial expression. 

### Features:

### Components:
#### Software:
The project utilizes OpenCV to read each frame of the video input from the PiCamera. Once this is done it detects where the user’s face is in the frame by pixel location. When a face is detected, a blue rectangle is drawn over the face to allow the user to 

#### Hardware:
For hardware a **Raspberry Pi 4** was used as well as a **PiCamera**, to allow for efficient and speedy processing of the video frames. These components were connected to a monitor, so that the user can see the live video feed, a graph of their emotions that was displayed using the **Matplotlib** visualization library, and hear the music playing.

### Demo:
#### 1. OpenCV detects the user's face and crops an image of their face
<img src="https://user-images.githubusercontent.com/66835262/103143605-aab04300-46e7-11eb-948e-8729de5d88e5.png" width="800px">



### Libraries and Frameworks Used:
* **Keras:** https://keras.io/
* **OpenCV:** https://opencv.org/
* **Pandas:** https://pandas.pydata.org/
* **MatPlotLib:** https://matplotlib.org/
* **NumPy:** https://numpy.org/


### Contributers:
* Christophe Zhang: https://github.com/asianz9863
* Jenny Tai: https://github.com/aegerita
* Alperen Asim Kes: https://github.com/alperenkes
* Jinwoo Park
