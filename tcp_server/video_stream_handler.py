#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : Server is placed in computer
import socketserver
import cv2 as cv2
import time
import numpy as np
class video_stream_handler(socketserver.StreamRequestHandler):
    def handle(self):
        recv_size = 1024
        stream_bytes = b''
        print('video_stream_handler : HANDLE YES')
        try:
            print('Connection')
            while True:
                #need to read posted data
                stream_bytes += self.rfile.read(recv_size)
                #identify the tags in the data being sent for the image
                first = stream_bytes.find(b'\xff\xd8')
                last =  stream_bytes.find(b'\xff\xd9')
                if (first != -1 and last != -1):
                    print('stream')
                    i = stream_bytes[first:last + 2]
                    #move the stream bytes to the next image
                    stream_bytes = stream_bytes[last + 2:]
                    #reads an image from a buffer in memory
                    #np.fromstring A new 1-D array initialized from text data from string
                    image = cv2.imdecode(np.fromstring(i,dtype = np.uint8),cv2.IMREAD_GRAYSCALE)
                    cv2.imshow('stream',image)
                    if(cv2.waitKey(33) == 27):
                        print('Stream stopped')
                        break

        except Exception as e:
            print(e)
        finally:
            print('Windows Destroyed')
            cv2.destroyAllWindows()
            return 0
