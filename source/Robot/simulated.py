class Servo:
    def __init__(self,channel,actuation_range=2):
        self.channel = channel
        self._angle = 60.1
    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self,angle):
        self._angle = angle
        self._callback()

    def _callback(self):
        print(f"SIM // SERVO {self.channel} ANGLE: {self._angle}")




class PCA9685:
    def __init__(self,i2c):
        self.channels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.frequency = None




# pico led
def off():
    print("SIM // LED: OFF")
def on():
    print("SIM // LED: ON")

# wifi
def country(co):
    print(f"SIM // Country set as: {co}")
STA_IF = None

class WLAN:
    def __init__(self,sta):
        pass
    def active(self,status):
        pass
    def config(self,value):
        pass
    def connect(self,ssid):
        pass
    def isconnected():
        return True
    def ifconfig():
        return ["SIM // Fake IP Addr"]
    