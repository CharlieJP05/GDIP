import network
import time
from   secrets import ssid, password

#connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
    print("waiting for connection...")
    time.sleep(1)
print(wlan.ifconfig())

