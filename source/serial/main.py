from ser import *
import time
# import serial.tools.list_ports
# 
# for port in serial.tools.list_ports.comports():
# 
#     print(port.hwid)
#     print(f"{port.device}: {port.description}")

t = 0
while True:
    run,runself = robot.goto_home_pos_smooth()
    while True:
        a= run(runself)
        if a < 1:
            break
        time.sleep(t)
    time.sleep(1)
    run,runself = robot.goto_pos_smooth(1200)
    while True:
        a= run(runself)
        if a < 1:
            break
        time.sleep(t)
    time.sleep(1)
robot.show_pos()
#robot.goto_home()
print(sp.read_all())