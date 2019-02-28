from tkinter import *
import cv2
import threading
from central_command_gui import App
import time

def app_worker():
    root = Tk()
    app = App(root)
    root.mainloop()


def main():
    # t = threading.Thread(target = app_worker)
    # t.daemon = True
    # t.start()
    #
    #
    # start = time.time()
    # with open('transmit_f.txt')as f:
    #     read_data = f.read()
    # f.close()
    # # print(read_data)
    # print('time : ' + str(time.time() - start))
    #
    # time.sleep(5)

    app_worker()




if __name__ == '__main__':
    main()
    print('Autonomous Vehicle Test')
