import json
import prompt
import workstation
import wifi
import groq


wifi.connect()

request = input("\nLab task: ")

plan = json.loads(groq.call(prompt.formatter(request)))

print(plan)

if plan["Mode"] != "DO":
    print("Didnt work")
else:
    for action in plan["Action"]:
        if action["do"] == "pick" or action["do"] == "place":
            x, y, z = workstation.get_position(action["at"])
            print(x,y,z)
