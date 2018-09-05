import cv2
import time

print(cv2.__version__)

cap = cv2.VideoCapture(0)
cap.set(3,320);
cap.set(4,240);

start_time = time.time()
interval = 1 # displays the frame rate every 1 second
counter = 0

while(True):
    ret,frame = cap.read()
    if ret == True:
        counter+=1

    cv2.imshow('DjRoomba',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if (time.time() - start_time) > interval :
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()
        
cap.release()
cv2.destroyAllWindows()
