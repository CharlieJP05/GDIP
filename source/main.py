# runs after boot.py
from control import *
import time
robot = Robot()
print("?")
robot.home()
while True:
    time.sleep(2)
    robot.base.set_angle(120)
    time.sleep(0.5)
    robot.grip.set_angle(90)
    time.sleep(2)
    robot.base.set_angle(100)
    time.sleep(0.5)
    robot.grip.set_angle(180)