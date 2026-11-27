from math import *

from math import sqrt, sin, cos, atan2, acos, radians, degrees

pca = None
pca9685 = None
dh = None
def init(SIM=False):
    global pca, pca9685, dh
    if SIM:
        import Robot.simulated as pca9685
        i2c = None
    else:
        import machine
        import micropython_pca9685 as pca9685
        i2c = machine.I2C(0, scl=machine.Pin(17),sda=machine.Pin(16))

    pca = pca9685.PCA9685(i2c)
    pca.frequency = 50
    dh = {
        "L1":140,
        "L2":190,
        "L3":119,
        "base_height":70
    }

class Servo:
    def __init__(self,minimum,home,maximum,offset,servo_id) -> None:
        self.servo = pca9685.Servo(pca.channels[servo_id],actuation_range=120)
        self._min = minimum
        self._max = maximum
        self._angle = home
        self._id = servo_id
        self._home = home
        self._offset = offset
    def set_angle(self,angle):
        self._angle = angle
        if angle > self._max or angle < self._min:
            return 0
        self.servo.angle = angle + self._offset
        return 1
    def get_angle(self):
        return self._angle
    def get_point(self): # gets the value 0 - 1 of where it is in its travel
        return (self._angle - self._min) / (self._max-self._min)
    def home(self):
        self.set_angle(self._home)
    
class Robot:
    def __init__(self) -> None:
        self.base =     Servo(0,60,120,10,0) # min home max offset id
        self.shoulder = Servo(0,60,120,10,1)
        self.elbow =    Servo(0,60,120,5,2)
        self.pitch =    Servo(0,60,120,10,3)
        self.roll =     Servo(0,60,120,0,4)
        self.grip =     Servo(0,60,120,0,5)
        self.ik = Ik()
    def home(self):
        self.set_angles(60,60,60,60)
        self.set_roll(60)
        self.set_grip(60)
    def set_angles(self,s0,s1,s2,s3):
        self.base.set_angle(s0)
        self.shoulder.set_angle(s1)
        self.elbow.set_angle(s2)
        self.pitch.set_angle(s3)
    def go_to(self,x,y,z,p):
        s0,s1,s2,s3 = self.ik.solve(x,y,z,p)
        self.set_angles(s0,s1,s2,s3)
    def set_roll(self,r):
        self.roll.set_angle(r)
    def set_grip(self,g):
        self.grip.set_angle(g)




class Ik:
    def __init__(self):
        self.home_angles = (0, 90, -90,0)
        self.servo_home = (60, 60, 60, 60)
        self.directions = (1, 1, 1, 1)

    def solve(self, x, y, z, p):
        # Link dimensions
        L1 = dh["L1"]
        L2 = dh["L2"]
        L3 = dh["L3"]
        h = dh["base_height"]

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
        #D = (rw**2 + zw**2 - L1**2 - L2**2) / (2*L1*L2)

        #if D < -1-1e-9 or D > 1+1e-9:
            #raise ValueError("Target is unreachable")
        
        # Calculate wrist distance in mm
        
        # Calculate wrist distance in mm
        distance = sqrt(rw**2 + zw**2)

        # Geometric reach limits
        min_reach = abs(L1 - L2)
        max_reach = L1 + L2

        # Diagnostic information
        print("IK target (mm):", x, y, z)
        print("Pitch (degrees):", degrees(p))
        print("Wrist centre (mm):", rw, zw)
        print("Wrist distance (mm):", distance)
        print("Allowed distance (mm):", min_reach, max_reach)

        # Check whether the target is reachable
        tolerance = 0.000001

        if (distance < min_reach - tolerance or
                distance > max_reach + tolerance):
            raise ValueError(
                "IK unreachable: wrist distance = {:.2f} mm, "
                "allowed = {:.2f} to {:.2f} mm".format(
                    distance, min_reach, max_reach
                )
            )

        # Cosine rule
        D = (rw**2 + zw**2 - L1**2 - L2**2) / (2*L1*L2)

        D = max(-1.0, min(1.0, D))

        distance = sqrt(rw**2 + zw**2)

        # Geometric reach limits
        min_reach = abs(L1 - L2)
        max_reach = L1 + L2

        D = max(-1.0, min(1.0, D))
        q2 = -acos(D)#acorrding to our understanding of home position the servo is negative, changeable 

        # Shoulder angle
        q1 = atan2(zw, rw) - atan2(
            L2*sin(q2),
            L1 + L2*cos(q2)
        )

      # Wrist pitch
        q3 = p - q1 - q2

        # Convert mathematical angles to degrees
        joint_angles = (
            degrees(q0),
            degrees(q1),
            degrees(q2),
            degrees(q3)
        )

        # Convert mathematical angles to servo angles
        servo_angles = []

        for i in range(4):
            angle = self.servo_home[i] + self.directions[i] * (
                joint_angles[i] - self.home_angles[i]
            )

            servo_limits = (110, 110, 115, 110)

            if not 0 <= angle <= servo_limits[i]:
                raise ValueError(
                    "Joint {} exceeds servo limits: {:.2f}".format(
                        i, angle
                    )
                )

            servo_angles.append(angle)


        # Diagnostic information
        print("Mathematical angles:", joint_angles)
        print("Servo angles:", servo_angles)

        return tuple(servo_angles)
