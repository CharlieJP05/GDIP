import json
import prompt
import workstation
import wifi
import groq
from picozero import pico_led


ip = wifi.connect()
connection = wifi.open_socket(ip)
wifi.serve(connection)


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