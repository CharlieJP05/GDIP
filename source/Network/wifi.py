from time import sleep
from secrets import ssid, password
pico_led = None
network = None
def init(SIM=False):
    global pico_led, network
    if SIM:
        import Robot.simulated as pico_led
        import Robot.simulated as network
    else:
        import network
        from picozero import pico_led

def connect():
    #connect to WLAN
    network.country("GB")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(pm=0xa11140)    #disable pico wifi power save mode
    print(wlan.connect(ssid))#, password))
    while not wlan.isconnected():
        print('Waiting for connection...')
        pico_led.on()
        sleep(0.5)
        pico_led.off()
        sleep(0.5)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    print("Connected:", wlan.isconnected())
    print("Network:", wlan.ifconfig())
    pico_led.on()
    return ip

def is_connected():
    return network.WLAN(network.STA_IF).isconnected()



