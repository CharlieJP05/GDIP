class Servo:
    def __init__(self,min,home,max) -> None:
        self.min = 0
        self.max = 270
        self.angle = (self.min+self.max)/2
        self.pin = pin
    def set_angle(self,angle):
        self.angle = angle
        # run PWM?
    def get_angle(self):
        return self.angle
    def get_range(self):
        return # the pos within the range
    
class Robot:
    def __init__(self) -> None:
        self.base =     Servo(0,90,180)
        self.shoulder = Servo(0,90,180)
        self.elbow =    Servo(0,90,180)
        self.pitch =    Servo(0,90,180)
        self.yaw =      Servo(0,90,180)
        self.grip =     Servo(0,90,180)