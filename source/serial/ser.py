import serial
import numpy as np
class Servo:
    def __init__(self,n) -> None:
        self.min = 0
        self.max = 1000
        self.num = n
        self.numstr = "#"+str(self.num)
        self.path = {}
    def set_position(self,p):
        sp.write((self.numstr + "P"+str(p)+"\r").encode())
    def set_point(self,p):
        if p > 1 or p < 0:
            return 0# fail
        point = self.min + (self.max-self.min)*p
        sp.write((self.numstr + "P"+str(point)+"\r").encode())
        print(self.numstr + " P"+str(int(point))+"\r")
    def get_point(self):
        qd = sp.write((self.numstr + " QP\r").encode())
        print("#"+str(qd))
        if qd == None:
            return -1
        point = self.min + (self.max-self.min)*qd
        return point
    def move(self,p):
        sp.write((self.numstr + "MD"+str(p)+"\r").encode())
    def smooth_to_position(self,a,p):
        self.path["start"] = a
        self.path["end"] = p
        self.path["step"] = 1
        if a > p:
            self.path["step"] *= -1
        self.path["current"] = a
        def run(self):
            pos = self.path["current"] + self.path["step"]
            self.path["current"] = pos
            self.set_position(pos)
            if pos == self.path["end"]:
                return 1 # got to end
            return 0
        return run,self
            
class Robot:
    def __init__(self) -> None:
            self.servos = []
    def add_servo(self):
        s = Servo(len(self.servos))
        self.servos.append(s)
    def add_many_servos(self,num):
        for i in range(num):
            self.add_servo()
    def goto_home(self):
        for servo in self.servos:
            servo.set_point(0.5)
    def goto_home_pos(self):
        for servo in self.servos:
            # if servo.num == 2:
            #     servo.set_position()
            servo.set_position(1500)
    def goto_home_pos_smooth(self):
        funcs = []
        for servo in self.servos:
            funcs.append(servo.smooth_to_position(1200,1500))
        def run(self):
            for i in funcs:
                out = i[0](i[1])
                if out == 1:
                    funcs.remove(i)
            return len(funcs)
        return run,self
    def goto_pos_smooth(self,num):
        funcs = []
        for servo in self.servos:
            funcs.append(servo.smooth_to_position(1500,num))
        def run(self):
            for i in funcs:
                out = i[0](i[1])
                if out == 1:
                    funcs.remove(i)
            return len(funcs)
        return run,self
    def show_pos(self):
        for i in self.servos:
            print(i.numstr)
sp = serial.Serial("/dev/ttyUSB0",115200)


robot = Robot()
robot.add_many_servos(6)
