import cv2
import datetime
import sys
from socket import *

cap = cv2.VideoCapture(0)
cap.set(3,320); # sets height of the frame
cap.set(4,240); # sets width of the frame

host = "192.168.0.19"
port = 4096
addr = (host, port)
buf = 1024 # size of buffer to send files

if (len(sys.argv) > 1):
    input = sys.argv[1]


def sendFile(fName):
    sock = socket(AF_INET, SOCK_DGRAM) # AF_INET - ipv4 protocol, SOCK_DGRAM - UDP
    sock.sendto(fName, addr)

    frame = open(fName, "rb")
    data = frame.read(buf)

    print("Sending data.." + str(datetime.datetime.now()))

    while data:
        if(sock.sendto(data, addr)):
            data = frame.read(buf)
    frame.close()
    sock.close()

def mainLoop():
    while(cap.isOpened()):
        ret,frame = cap.read() # capture frame
        if ret == True:
            cv2.imwrite("frame.jpg", frame)
            if input == "debug":
                cv2.imshow('frame', frame)
            sendFile("frame.jpg")
            count = 0
        else:
            break;
        if cv2.waitKey(1) & 0xFF == ord('q'): # exit if 'q' pressed
            break

if __name__ == '__main__':
    print(cv2.__version__)
    mainLoop()
    cap.release()
    cv2.destroyAllWindows()
