import playsound
import cv2

cam = cv2.VideoCapture(1)

num=0
while cam.isOpened():
    if num%50 == 0:
        playsound.playsound("/Users/utkarsh/Downloads/squid-game-red-light-green-light-sound-effect (1).mp3") #red light green light music
        flag = 1

    # Making 2 continuous frames
    _,frame1 = cam.read()
    _,frame2 = cam.read()

    # Finding difference between those 2 continuous frames
    diff = cv2.absdiff(frame1, frame2)

    # Greyscale and blurring the image for better detection
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Creating a threshold for the movement to be large enough for detection
    _, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

    # Dilating and making contours(boxes around detected image)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for i in contours:
        if cv2.contourArea(i) < 2000:
            continue
        else:
            if(flag == 0):
                playsound.playsound("/Users/utkarsh/Downloads/RPzvNzyQZTI_48 (1).mp3") #you are dead audio
    flag = 0
    num +=1




