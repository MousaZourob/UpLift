import cv2
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from picamera import PiCamera
from time import sleep
from picamera.array import PiRGBArray
import simpleaudio as sa
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppresses the warnings from tf

# Declaration & initialization
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
video = PiCamera()
rawCapture=PiRGBArray(video)
video.framerate=32
sleep(0.1)
counter = 1
rectangleBorder = 2
imageWidth = 48
imageHeight = 48
numberOfImages = 15
numberOfSongs = 10;
videoDelay = 20
new_model = tf.keras.models.load_model('../kerasTraining/saved_model/my_model')

for frame in video.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # videoRead, frame = video.capture(rawCapture, format="bgr") # Reads frame from camera, videoRead true if successful
        frame = frame.array
        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converts frame to grayscale
        frameFaces = faceCascade.detectMultiScale(frameGray, 3, 4)  # Detects faces

        for (x, y, w, h) in frameFaces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), rectangleBorder)
            frameCropped = frameGray[y + rectangleBorder:y + h - 2 * rectangleBorder,
                           x + rectangleBorder:x + w - 2 * rectangleBorder]
            frameResized = cv2.resize(frameCropped, (imageWidth, imageHeight))
            # cv2.imshow("Cropped", frameCropped)
            # cv2.imshow("Resized", frameResized)
            cv2.imwrite("UserFaceImages/frame" + str(counter) + ".jpg", frameResized)
            counter += 1

        cv2.imshow("Frame", frame)
        rawCapture.truncate(0)
        if counter > numberOfImages:
            video.close()
            break
        if cv2.waitKey(videoDelay) & 0xFF == ord('q'):
            break

# cv2.waitKey(0)  # Allows you to close image window
percentageArray = [0.0]*6
for i in range(1, numberOfImages+1):
    img = tf.keras.preprocessing.image.load_img(
        "../OpenCV/UserFaceImages/frame" + str(i) + ".jpg", target_size=(48, 48)
    )

    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img, 0)  # Create a batch

    img_array = img_array.reshape(-1, imageHeight, imageWidth, 1) / 255.0

    predictions = new_model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    percentageArray = np.add(percentageArray, score)

emotions = ['Angry', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
percentageArray = np.array(percentageArray)

ultimateArray = [percentageArray[0],
                 percentageArray[2]+percentageArray[4],
                 percentageArray[3]+0.25*percentageArray[5]]

emotions = ['Angry', 'Happy', 'Sad']
userEmotion = emotions[int(np.argmax(ultimateArray))]
print(userEmotion)
# print(percentageArray)
# new_model.summary()


# print bar chart of percentage
y_pos = np.arange(len(emotions))
plt.bar(y_pos, ultimateArray/sum(ultimateArray), align='center', alpha=0.5)
plt.xticks(y_pos, emotions)
plt.ylim([0, 1])
plt.ylabel('Emotion')
plt.title('Emotion of this face')
plt.show()

# print 9 random faces
plt.figure(0, figsize=(6, 6))
for i in range(1, 5):
    img = tf.keras.preprocessing.image.load_img(
       "../OpenCV/UserFaceImages/frame" + str(np.random.randint(numberOfImages)+1) + ".jpg", target_size=(48, 48)
    )
    plt.subplot(2, 2, i)
    plt.imshow(img)

plt.show()

if userEmotion == 'Happy':
    happySong = "../OpenCV/Songs/Happy/" + str(np.random.randint(1, 10)) + '.wav'
    happySongWav = sa.WaveObject.from_wave_file(happySong)
    happySongWavPlaying = happySongWav.play()
    happySongWavPlaying.wait_done()
else:
    calmSong = "../OpenCV/Songs/Calm/" + str(np.random.randint(1, 10)) + '.wav'
    calmSongWav = sa.WaveObject.from_wave_file(calmSong)
    calmSongWavPlaying = calmSongWav.play()
    calmSongWavPlaying.wait_done()
