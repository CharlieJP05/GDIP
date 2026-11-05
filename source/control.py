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



from math import sqrt, sin, cos, atan2, acos, radians, degrees

class Ik:
    def __init__(self, dh):
        self.dh = dh

    def solve(self, x, y, z, p):
        # Link dimensions
        L1 = self.dh["L1"]
        L2 = self.dh["L2"]
        L3 = self.dh["L3"]
        h = self.dh["base_height"]

        # Convert pitch to radians
        p = radians(p)

        # Base rotation
        q0 = atan2(y, x)

        # Horizontal distance
        r = sqrt(x*x + y*y)

        # Wrist centre position
        rw = r - L3*cos(p)
        zw = z - h - L3*sin(p)

        # Elbow angle
        D = (rw**2 + zw**2 - L1**2 - L2**2) / (2*L1*L2)

        if D < -1-1e-9 or D > 1+1e-9:
            raise ValueError("Target is unreachable")

        D = max(-1.0, min(1.0, D))
        q2 = acos(D)

        # Shoulder angle
        q1 = atan2(zw, rw) - atan2(
            L2*sin(q2),
            L1 + L2*cos(q2)
        )

        # Wrist pitch
        q3 = p - q1 - q2

        return {
            "base": degrees(q0),
            "shoulder": degrees(q1),
            "elbow": degrees(q2),
            "pitch": degrees(q3)
        }
