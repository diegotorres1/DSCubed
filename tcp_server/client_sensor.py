#The client for the sensor information to be sent back to the computer


import socket
import struct
import time
import io
import numpy as np
class client_sensor():
    def __init__(self,server_ip, server_port):
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((server_ip,server_port))
        #we want to treat the stream as a file
        connection = client_socket.makefile('wb')
        print('Client Sensor')
        try:
            stream = io.BytesIO()
            while(True):
                print('streaming sensor data')
                #sensor_start, and sensor_end
                x = np.array([1.23, 4.3])
                stream.write(str.encode('sensor_start') + (x.tobytes()) + str.encode('sensor_end'))
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
            print('Error HIT with Sensor')    
        finally:
            print('Connection is closed')
            connection.close()
            client_socket.close()

