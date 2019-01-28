import socketserver
import time
import numpy as np
import cv2 as cv2
class sensor_handler(socketserver.StreamRequestHandler):
    def handle(self):
        recv_size = 1024
        stream_bytes = b''
        print('sensor_handler : HANDLE YES')
        try:
            print('Connection')
            while True:
                #need to read posted data
                stream_bytes += self.rfile.read(recv_size)
                #identify the tags in the data being sent for the image jpeg
                first = stream_bytes.find(b'sensor_start')
                last =  stream_bytes.find(b'sensor_end')
                if (first != -1 and last != -1):
                    #the plus 2 is from the '<2'

                    i = stream_bytes[first + len(b'sensor_start'):last]
                    stream_bytes = stream_bytes[last + len(b'sensor_end'):]
                    print(str(i))
                    values = np.fromstring(i,dtype = np.float)

                    try:
                        print('Voltage_1:' + str(values))
                    except Exception as e:
                        print(e)
                        print('Voltage_1 was incorrectly read, ' + str(values))
                    if(cv2.waitKey(33) == 27):
                        print('Stream stopped')
                        break

        except Exception as e:
            print(e)
        finally:
            print('Windows Destroyed')
            cv2.destroyAllWindows()
            return 0
