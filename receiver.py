from socket import *
import cv2

host = "192.168.0.19"
port = 4096
buffer = 1024
addr = (host, port)
fName = 'frame.jpg'
timeOut = 0.05


def foo():
    while True:

        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind(addr)

        data, address = sock.recvfrom(buffer)

        try:
            frame = open(data, 'wb')
        except:
            continue

        data, address = sock.recvfrom(buffer)

        try:
            while data:
                frame.write(data)
                sock.settimeout(timeOut)
                data, address = sock.recvfrom(buffer)
        except timeout:
            frame.close()
            sock.close()

        image = cv2.imread(fName)
        cv2.imshow('DjRoomba', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    foo()
    cv2.destroyAllWindows()
