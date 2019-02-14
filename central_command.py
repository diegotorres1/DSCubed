from tkinter import *
import cv2
class App:
    def __init__(self, master):
        self.speed = 0
        self.angle = 0
        main_frame = Frame(master)
        main_frame.pack()
        speed_frame = Frame()
        speed_frame.pack(side = BOTTOM)
        angle_frame = Frame()
        angle_frame.pack(side = BOTTOM)


        #MAIN
        self.button = Button(main_frame,text="SHUTDOWN", fg="red",command=main_frame.quit)
        self.button.pack(side=LEFT)



        #SPEED CONTROL
        self.speed_label = Label(speed_frame, text="Speed Controls")
        self.speed_label.pack(side=TOP)
        self.increment_speed_button = Button(speed_frame,text="+",command=self.increment_speed)
        self.increment_speed_button.pack(side=LEFT)
        self.decrement_speed_button = Button(speed_frame,text="-",command=self.decrement_speed)
        self.decrement_speed_button.pack(side=LEFT)
        self.speed_entry = Entry(speed_frame, width=50)
        self.speed_entry.pack(side=RIGHT)
        self.submit_speed_button = Button(speed_frame,text="submit",command=self.submit_speed)
        self.submit_speed_button.pack(side=RIGHT)

        #STEERING CONTROL
        self.angle_label = Label(angle_frame, text="Steering Controls")
        self.angle_label.pack(side=TOP)
        self.increment_angle_button = Button(angle_frame,text="+",command=self.increment_angle)
        self.increment_angle_button.pack(side=LEFT)
        self.decrement_angle_button = Button(angle_frame,text="-",command=self.decrement_angle)
        self.decrement_angle_button.pack(side=LEFT)
        self.angle_entry = Entry(angle_frame, width=50)
        self.angle_entry.pack(side=RIGHT)
        self.submit_speed_button = Button(angle_frame,text="submit",command=self.submit_angle)
        self.submit_speed_button.pack(side=RIGHT)







    #SPEED
    def increment_speed(self):
        self.speed += 1
        print('speed : \t' + str(self.speed))
    def decrement_speed(self):
        self.speed -= 1
        print('speed : \t' + str(self.speed))
    def submit_speed(self):
        try:
            self.speed = int(self.speed_entry.get())
        except Exception as e:
            print(e)
            print('Invalid input is attempting to be submitted. Value must be an integer')
        print('speed : \t' + str(self.speed))


    #SPEED
    def increment_angle(self):
        self.angle += 1
        print('angle :\t' + str(self.angle))
    def decrement_angle(self):
        self.angle -= 1
        print('angle : \t' + str(self.angle))
    def submit_angle(self):
        try:
            self.angle = int(self.angle_entry.get())
        except Exception as e:
            print(e)
            print('Invalid input is attempting to be submitted. Value must be an integer')
        print('angle : \t' + str(self.angle))


root = Tk()
app = App(root)
root.mainloop()
