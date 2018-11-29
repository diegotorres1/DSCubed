#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : This will be placed in the raspberry pi
import picamera as pc
import socket
import time
import io
class client():
    def __init_(self,server_ip, server_port):
        client_socket = socket.socket(socket.AF_INIT,socket.SOCK_STREAM)
        client_socket.connect()
        #we want to treat the stream as a file
        connection = client_socket.makefile('wb')
        try:
            with picamera.PiCamera() as cam:
                cam.resolution(640,480)
                time.sleep()
                #create streams
                stream = io.BytesIO()
                for frame in cam.capture_continuous(stream,'jpeg',use_video_port = True)
                    connection.write(struct.pack('<L',stream.tell()))
                    connection.flush()
                    #find the start of the stream
                    stream.seek(0)
                    connection.write(stream.read())
                    stream.seek(0)
                    stream.truncate()
            connection.write(struct.pack('<L', 0))
        finally:
            connection.close()
            client_socket.close()
