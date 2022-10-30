"""
The easy way:
sudo edit /etc/udev/rules.d/50-myusb.rules

Save this text:
KERNEL=="ttyUSB[0-9]*",MODE="0666"

Unplug the device and replug it, and it should be read/write from any user!
"""

from datetime import datetime
import serial
import serial.tools.list_ports

# baudrate for serial connection
# default Data bits 8, Stop bits 1, Parity None
BAUD = 38400


def get_ports():
    print("I am looking for ports")
    # get list of all devices connected through serial port
    comPorts = serial.tools.list_ports.comports()
    # dictionary of available ports
    av_ports = {}

    for i,p in enumerate (comPorts,1):
        # print available port
        print(f'{i}. {p.device} - {p.manufacturer} - {p.description}')
        # add to dictionary
        av_ports[i] = p.device
        
    print("Select comport: ")
    while 1:
        port = int(input())
        if port not in av_ports:
            print("Expected number of available ports (e.g 1, 2 ...)")
        else:
            break
    return av_ports.get(port)


def send():

    ser = serial.Serial()
    ser.baudrate = BAUD
    ser.port = get_ports()
    ser.open()
    date_time = datetime.now().strftime("AT+SET?:%H:%M:%S:%y:%m:%d:%w\n\r").encode()
    ser.write(date_time)
    #print(date_time)
    # ser.write("AT+RST?\n\r".encode())
    ser.close()


def main():
    # get_ports()
    send()


if __name__ == "__main__":
    main()


