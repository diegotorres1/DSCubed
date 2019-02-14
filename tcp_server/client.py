#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : This will be placed in the raspberry pi
import picamera as picamera
import socket
import struct
import time
import io
import sys
import threading
sys.path.insert(0, '../')
from bluetooth_test import bluetooth_test
class client():
    def __init__(self,server_ip, server_port):
        
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((server_ip,server_port))
        #we want to treat the stream as a file
        connection = client_socket.makefile('wb')
        btt = bluetooth_test()
        threading.Thread(target=btt.bluetooth_stream).start()
        #~ c = input('continue')   
        try:
            with picamera.PiCamera() as cam:
                cam.resolution = (640,480)
                time.sleep(3)
                #create streams
                stream = io.BytesIO()
                for frame in cam.capture_continuous(stream,'jpeg',use_video_port = True):
                    print('1-1 Video Packet')
                    connection.write(struct.pack('<L',stream.tell()))
                    connection.flush()
                    #find the start of the stream
                    stream.seek(0)
                    connection.write(stream.read())
                    stream.seek(0)
                    stream.truncate()
            connection.write(struct.pack('<L', 0))
        finally:
            print('Connection is closed')
            connection.close()
            client_socket.close()
            
            
#~ import io
#~ import socket
#~ import struct
#~ import time
#~ import picamera
#~ import sys
#~ from SplitFrames import SplitFrames

#~ class client():
    #~ def __init__(self,server_ip, server_port):
        #~ res = (320, 240)
        #~ client_socket = socket.socket()
        #~ client_socket.connect((server_ip, server_port))
        #~ connection = client_socket.makefile('wb')
        #~ try:
            #~ output = SplitFrames(connection)
            #~ with picamera.PiCamera(resolution=res, framerate=30) as camera:
                #~ time.sleep(2)
                #~ start = time.time()
                #~ camera.start_recording(output, format='mjpeg')
                #~ camera.wait_recording(sys.maxint)
                #~ camera.stop_recording()
                #~ # Write the terminating 0-length to the connection to let the
                #~ # server know we're done
                #~ connection.write(struct.pack('<L', 0))
        #~ finally:
            #~ finish = time.time()
            #~ print('Sent %d images in %d seconds at %.2ffps' % (output.count, finish-start, output.count / (finish-start)))
            #~ connection.close()
            #~ client_socket.close()

