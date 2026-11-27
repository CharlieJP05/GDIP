import socket
import sys
pico_led = None
def init(SIM=False):
    global pico_led
    if SIM:
        import Robot.simulated as pico_led
    else:
        from picozero import pico_led

def open_socket(ip):
    # Open a socket
    address = ("0.0.0.0", 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


def webpage():
    fd =  open("Webpage/index.html")
    html = fd.read()
    # html = html.replace('{state}', state)
    # html = html.replace('{temperature}', str(temperature))
    return html


def serve(connection):
    #Start a web server
    pico_led.off()
    while True:
        print("Waiting for Client...")
        client = connection.accept()[0]
        request = client.recv(1024)
        print("Got Request:")
        request = str(request)
        try:
            request = request.split()[1]
            print("split:")
            print(request)
        except IndexError:
            pass
        if request == '/action_page.php?':
            pico_led.on()
        elif request == '/close?':
            sys.exit()
        html = webpage()
        client.send(html)
        client.close()