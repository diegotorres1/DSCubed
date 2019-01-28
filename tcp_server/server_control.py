#This is for the RPI to receive commands

#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : Server is placed in computer
import socketserver
import numpy as np
import sys
import threading
from control_handler import control_handler
class server_control():
    def __init__(self,server_ip, control_port):
        self.control_ip = control_port
        #Create a thread to handle the throughput for both the video and the sensor information
        self.control_stream(server_ip,control_port)
        print('server control has started')

    def control_stream(self,server_ip,control_port):
        print('control_stream thread')
        vs_socket = socketserver.TCPServer((server_ip,control_port),control_handler)
        vs_socket.serve_forever()


