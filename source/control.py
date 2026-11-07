import pca
from math import *
class Servo:
    def __init__(self,minimum,home,maximum,servo_id) -> None:
        self._min = minimum
        self._max = maximum
        self._angle = home
        self._id = servo_id
        self._home = home
    def set_angle(self,angle):
        self._angle = angle
        if angle > self._max or angle < self._min:
            return 0
        pca.set_servo_duty(self._id,self.get_point())
        return 1
    def get_angle(self):
        return self._angle
    def get_point(self): # gets the value 0 - 1 of where it is in its travel
        return (self._angle - self._min) / (self._max-self._min)
    def home(self):
        self.set_angle(self._home)
    
class Robot:
    def __init__(self) -> None:
        self.base =     Servo(0,135,270,0)
        self.shoulder = Servo(0,90,180,1)
        self.elbow =    Servo(0,90,180,2)
        self.pitch =    Servo(0,90,180,3)
        self.roll =     Servo(0,90,180,4)
        self.grip =     Servo(0,90,180,5)
    def home(self):
        self.base.home()
        self.shoulder.home()
        self.elbow.home()
        self.pitch.home()
        self.roll.home()
        self.grip.home()


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
