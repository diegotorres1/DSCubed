import socketserver
import time
import numpy as np
import cv2 as cv2
class sensor_handler(socketserver.BaseRequestHandler):
    data = " "
    def handle(self):
        global sensor_data
        while self.data:
            self.data = self.request.recv(1024)
            # print "{} sent:".format(self.client_address[0])
            print(self.data)
