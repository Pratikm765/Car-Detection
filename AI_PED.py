import cv2

def CarDetection():
    video=cv2.VideoCapture("testVideo_Trim2.mp4")
    car_tracker = cv2.CascadeClassifier('cars_detector.xml')

    while True:
        (read_successful,frame)=video.read()
        if(read_successful):
            bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            break

        cars = car_tracker.detectMultiScale(bw_frame, minSize=(150, 150))
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('Cars Tracking',frame)
        key=cv2.waitKey(1)

        if key==81 or key==113:
            break


CarDetection()
