import network
import time
from secrets import ssid, password

def connect():
    #connect to WLAN
    network.country("GB")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(pm=0xa11140)    #disable pico wifi power save mode
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')

def is_connected():
    return network.WLAN(network.STA_IF).isconnected()
