import json
from picozero import pico_led
import sys
import time
#
from LLM import prompt, groq
from Robot import workstation, control
from Network import wifi, network



# rob = control.Robot()
# rob.home()
# time.sleep(1)
# rob.go_to(10,10,10,0)
# print("1")
# time.sleep(3)
# rob.go_to(110,90,100,0)
# print("2")

# sys.exit() ## remove
ip = wifi.connect()
connection = network.open_socket(ip)
network.serve(connection)


request = input("\nLab task: ")
plan = json.loads(groq.call(prompt.formatter(request)))

if plan["Mode"] == "DO":
    for action in plan["Action"]:
            if action["do"] == "pick" or action["do"] == "place":
                x, y, z = workstation.get_position(action["at"])
                print(x,y,z) 
elif plan["Mode"] == "Error":
    print(f"Error: {plan["Reason"]}")
else:
    print(f"Unknown Error: {plan}")

# Shutdown Code

pico_led.off()
