
import socket
import struct
import time
import io
import numpy as np
import cv2
class client_control():
    def __init__(self,server_ip, server_port):
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((server_ip,server_port))
        #we want to treat the stream as a file
        connection = client_socket.makefile('wb')
        print('Client Control')
        x = np.array([0,0])
        greyscale_image = cv2.imread('edith.jpg',0)
        cv2.imshow('greyscale image', greyscale_image)
        try:
            stream = io.BytesIO()
            while(True):
                print('streaming control data')
                x = self.control()
                print(x)
                stream.write(str.encode('control_start') + (x.tobytes()) + str.encode('control_end'))
                connection.write(struct.pack('<L',stream.tell()))
                connection.flush()
                #find the start of the stream
                stream.seek(0)
                connection.write(stream.read())
                stream.seek(0)
                stream.truncate()
            connection.write(struct.pack('<L', 0))

        except Exception as e:
            print(e)
            print('Error HIT with Control')
        finally:
            print('Connection is closed')
            print('Windows Destroyed')
            cv2.destroyAllWindows()
            connection.close()
            client_socket.close()
    def control(self):
        x = np.array([1,0])
        c = cv2.waitKey(30)
        if(c == ord('a')):
            print('a')
            x = np.array([3,4])
        return x
