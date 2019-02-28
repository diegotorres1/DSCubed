#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : Server is placed in computer
import socketserver
import numpy as np
import sys
import threading
from video_stream_handler import video_stream_handler
from sensor_handler import sensor_handler
class server():
    def __init__(self,server_ip, video_port, sensor_port):
        self.video_port = video_port
        self.sensor_port = sensor_port
        #Create a thread to handle the throughput for both the video and the sensor information
        s_thread = threading.Thread(target=self.sensor_stream, args=(server_ip,sensor_port))
        s_thread.daemon = True
        s_thread.start()
        self.video_stream(server_ip,video_port)
        # v_thread.daemon = True

        print('server has started')

    def video_stream(self,server_ip,video_port):
        print('video_stream thread')
        vs_socket = socketserver.TCPServer((server_ip,video_port),video_stream_handler)
        vs_socket.serve_forever()

    def sensor_stream(self,server_ip,sensor_port):
        print('sensor_stream thread')
        ss_socket = socketserver.TCPServer((server_ip,sensor_port),sensor_handler)
        ss_socket.serve_forever()
