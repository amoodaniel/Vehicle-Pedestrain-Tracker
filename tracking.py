'''
import cv2
#images
img_file = 'carpics_2.jpg'
#classifier
classifier_file ='car_detector.xml'

#create opencv img
img = cv2.imread(img_file)

#create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

#convert to grayscale
black_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#detect cars
cars = car_tracker.detectMultiScale(black_white)
print(cars)
#draw rectangles around the cars
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),2)

#display the image with the faces spotted
cv2.imshow('Car detector', img)

#don't autoclose-wait for a key press
cv2.waitKey()
print('code completed')
'''
import cv2
#our Image 
img_file= 'carpics_2.jpg'
video = cv2.VideoCapture('pedes_vid.mp4')
#classifier
classifier_file= 'car_detector.xml'
pedestrian_file = 'pedestrian.xml'
#create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)
pedestrain_tracker = cv2.CascadeClassifier(pedestrian_file)

#run forever
while True:
    #read the current frame
    read_successful, frame = video.read()
    #safe coding
    if read_successful:
        #must convert to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    #detect cars And Pedestrians
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrains = pedestrain_tracker.detectMultiScale(grayscaled_frame)

    #draw rectangles around the cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,0),2)

    #draw rectangles around the pedestrians
    for (x,y,w,h) in pedestrains:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,255),2)

    #display the image with the faces spotted
    cv2.imshow('Car detector', frame)

    #don't autoclose-wait for a key press
    key= cv2.waitKey(1)

    #Stop if Q key is pressed
    if key==81 or key ==113:
        break
#Release the VideoCapture
video.release()





