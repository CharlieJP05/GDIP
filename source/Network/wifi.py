import Network.network as network
from time import sleep
from picozero import pico_led
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
        pico_led.on()
        sleep(0.5)
        pico_led.off()
        sleep(0.5)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    pico_led.on()
    return ip

def is_connected():
    return network.WLAN(network.STA_IF).isconnected()



