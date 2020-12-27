# UpLift
### Overview:
Uplift is a mood changer programmed with **Python** that plays a song to positively change the user's mood. The song choice is based on the user's facial expression, so if the user is happy, cheerful music is played to keep them motivated, and if they are sad or angry, relaxing music is played to soothe them. A combination of hardware (**Raspberry Pi**), and software (**OpenCV, Keras, Pandas**) components were used to create this project. 
<br />
Other than helping individual users, a commercial application of this product is usage in restaurants and cafes to detect the most dominant emotion, and play music based on the customer’s emotions.


### Components:
#### Software:
The project utilizes **OpenCV** to read each frame of the video input from the **PiCamera**, which is connected to a **Raspberry Pi**. Once this is done **OpenCV** detects where the user’s face is in the frame by pixel location. When a face is detected, a blue rectangle is drawn over the face to allow the user to see the program in action. **Keras** then takes the frames and runs them against a dataset from **Kaggle** to determine the user's facial expression. After this using **MatplotLib** visualization library and **Pandas**, a graph is displayed showing the user their emotions based on their facial expression, and music is played using the **SimpleAudio** Python package.

#### Hardware:
For hardware a **PiCamera** was used as well as a **Raspberry Pi 4**, to allow for efficient and speedy processing of the video frames. These components were connected to a monitor, so that the user can see the live video feed and a graph of their emotions that was displayed using the **Matplotlib**, and hear the music playing.


### Demo:
#### 1. OpenCV detects the user's face and crops an image of their face
<img src="https://user-images.githubusercontent.com/66835262/103143615-f19e3880-46e7-11eb-9e94-6a8dc7155ed4.png" width="600px">

#### 2. Keras runs a model against the detected faces and determines a facial expression, the data is displayed using MatplotLib
<img src="https://user-images.githubusercontent.com/66835262/103143643-6a9d9000-46e8-11eb-82e7-1dae90e5593f.png" width="600px">

#### 3. A song is played through the speakers attached to the Raspberry Pi to maintain or elevate the user's mood 


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
* Jinwoo Park: https://github.com/hilfiger1
* Mousa Zourob https://github.com/MousaZourob
