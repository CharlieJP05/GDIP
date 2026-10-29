from control import *
import sys
SIM = 0


if __name__ == "__main__":
    # if len(sys.argv) > 1:
    #     SIM = sys.argv[1]
    robot = Robot()
    
    robot.base.set_angle(90)