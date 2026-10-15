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
while False:
    sp.write("#0QP\r".encode())
    print(sp.read_all().decode())
    time.sleep(2)
    print("running")
    path = robot.teach(2,1)
    print("finish teach")
    robot.run(2,1,path)
    print("done")
# robot.show_pos()
# #robot.goto_home()
# print(sp.read_all())