import cv2


# Create our body classifier
car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('cars_video.mp4')


# Loop once video is successfully loaded
while cap.isOpened():
    
    # time.sleep(.05)
    # Read first frame
    ret, frame = cap.read()
    # height, width, _ = frame.shape
    # print(height,width)


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

 
    # Pass frame to our car classifier
    cars = car_classifier.detectMultiScale(gray, 1.4, 2)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

        # recognise color of bounding box
        # use centre of bounding box
        cx = int(x+w/2)
        cy = int(y+h/2)
        if cx >= 720 or cy >= 1280:
            cx = 719
            cy = 1279

        pixel_centre = hsv_frame[cx,cy]
        b,g,r = int(pixel_centre[0]),int(pixel_centre[1]),int(pixel_centre[2])
        hue_value = pixel_centre[0]

        color = 'undefined'
        if 0<hue_value<5:
            color = 'red'
        elif 5<hue_value<22:
            color = 'black'
        elif 22<hue_value<33:
            color = 'yellow'
        elif 33<hue_value<78:
            color = 'green'
        elif 78<hue_value<131:
            color = 'blue'        
        elif 131<hue_value<167:
            color = 'white'
        else:
            color = 'violet'

        print(pixel_centre)

        cv2.circle(frame, (cx,cy), 2, (255,0,0), 2)   
        cv2.putText(frame, color, (x + 6, y - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (b, g, r), 2)
        cv2.imshow('Cars', frame)


    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()