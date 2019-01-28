#Author : Diego Torres
#Date of Modification : 1/27/2019
# Description : The control handler is a server side handler to process
#	the request of the client computer controls
import socketserver
import time
import numpy as np
from process_execute_test import process_execute_test

class control_handler(socketserver.StreamRequestHandler):
    def handle(self):
		pe = process_execute_test()
        count = 0
        recv_size = 32
        stream_bytes = b''
        print('control_handler : HANDLE YES')
        try:
            print('Connection')
            while True:
                count += 1
                print(count)
                print('receiving')
                #need to read posted data
                stream_bytes += self.rfile.read(recv_size)
                print('read')
                #identify the tags in the data being sent for the image jpeg
                first = stream_bytes.find(b'control_start')
                last =  stream_bytes.find(b'control_end')
                if (first != -1 and last != -1):
                    #the plus 2 is from the '<2'
                    i = stream_bytes[first + len(b'control_start'):last]
                    stream_bytes = stream_bytes[last + len(b'control_end'):]
                    values = np.fromstring(i,dtype = np.int)
                    try:
                        print(str(values))
                        pe.pe_control(values[0])
                    except Exception as e:
                        print(e)
                        print('The control was incorrectly received, ' + str(values))
                print('end') 

        except Exception as e:
            print(e)
        finally:
            return 0

