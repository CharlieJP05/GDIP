import pca
from math import *
class Servo:
    def __init__(self,min,home,max,pin) -> None:
        self.min = 0
        self.max = 270
        self.angle = (self.min+self.max)/2
        self.pin = 0
    def set_angle(self,angle):
        self.angle = angle
        pca.set_servo_duty(self.pin,angle)
        # run PWM?
    def get_angle(self):
        return self.angle
    def get_range(self):
        return # the pos within the range
    
class Robot:
    def __init__(self) -> None:
        self.base =     Servo(0,90,180,0)
        self.shoulder = Servo(0,90,180,1)
        self.elbow =    Servo(0,90,180,2)
        self.pitch =    Servo(0,90,180,3)
        self.yaw =      Servo(0,90,180,4)
        self.grip =     Servo(0,90,180,5)


class Ik:
    def __init__(self,dh):
        self.dh = dh
    def solve(self,x,y,z,p):
        r = sqrt(x*x+y*y)