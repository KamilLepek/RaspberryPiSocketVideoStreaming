import cv2
import datetime
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera
from socket import *

def sendFile(fName):
    sock = socket(AF_INET, SOCK_DGRAM) # AF_INET - ipv4 protocol, SOCK_DGRAM - UDP
    sock.sendto(fName, addr)

    frame = open(fName, "rb")
    data = frame.read(buf)

    while data:
        if(sock.sendto(data, addr)):
            data = frame.read(buf)
    frame.close()
    sock.close()

def mainLoop():
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        
        image = frame.array

        # write image to file and send via socket
        cv2.imwrite("frame.jpg", image)
        sendFile("frame.jpg")
 
        # show the frame if debug mode
        if input == "debug":
            cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
 
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
 
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

if __name__ == '__main__':

    # validate if there was input
    if (len(sys.argv) > 1):
        input = sys.argv[1]

    width = 480
    height = 640

    if input == "size":
        if (len(sys.argv)== 4):
            try:
                width = int(sys.argv[2])
                height = int(sys.argv[3])
            except ValueError:
               print("Cannot parse parameters!")                

    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (width, height)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(width, height))

    host = "192.168.0.19"
    port = 4096
    addr = (host, port)
    buf = 1024 # size of buffer to send files
    
    print(cv2.__version__)
    mainLoop()
    cv2.destroyAllWindows()
