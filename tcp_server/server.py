#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : Server is placed in computer
import socketserver
import numpy as np
import sys
import threading

class server():
    def __init__(self,server_ip, video_port, sensor_port):
        self.video_port = video_port
        self.sensor_port = sensor_port
        #Create a thread to handle the throughput for both the video and the sensor information
        s_thread = threading.Thread(target=sensor_s, args=(server_ip,sensor_port))
        v_thread = threading.Thread(target=video_s, args=(server_ip,video_port))
        s_thread.daemon = True
        v_thread.daemon = True
        s_thread.start()
        v_thread.start()
        print('server has started')

    def video_stream(self,server_ip,video_port):
        print('video_stream thread')
        vs_socket = socketserver.TCPServer((host,port),video_stream_handler())
        vs_socket.serve_forever()

    def sensor_stream(self,server_ip,sensor_port):
        print('sensor_stream thread')
        ss_socket = socketserver.TCPServer((host,port),sensor_stream_handler())
        ss_socket.serve_forever()
