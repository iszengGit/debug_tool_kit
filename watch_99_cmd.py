# -*-coding: utf-8 -*-
import serial
import threading
import binascii
from datetime import datetime
import struct
import csv
import time



class SerialPort:
    def __init__(self, port, buand, bytesize, parity, stopbit, timeout, \
    xonxoff, rtscts, write_timeout, dsrdtr, inter_byte_timeout, exclusive):
        self.port = serial.Serial(port, buand, bytesize, parity, stopbit, timeout, \
        xonxoff, rtscts, write_timeout, dsrdtr, inter_byte_timeout, exclusive)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self):
        self.port.write('')

    def read_data(self):
        global is_exit
        global data_bytes
        start_check_interval = 0
        last = 0
        next = 0
        print('start...')
        while not is_exit:
            count = self.port.inWaiting()
            if count > 0:
                start_check_interval = 1
                last = time.perf_counter()
                rec_str = self.port.read(count)
                data_bytes = data_bytes + rec_str
            else:
                if (start_check_interval == 1):
                    next = time.perf_counter()
                    interval = next - last
                    if (interval < 0.01):
                        continue
                    else:
                        if len(data_bytes) == 95:
                            for i in range(28, 40):
                                if data_bytes[i] != 0:
                                    print(str(datetime.now()),':',binascii.b2a_hex(data_bytes),'\n')
                                    break
                        data_bytes = bytearray()

serialPort = 'COM1'  # 串口
baudRate = 19200  # 波特率
is_exit = False
data_bytes = bytearray()

if __name__ == '__main__':
    #打开串口
    mSerial = SerialPort(serialPort, baudRate, bytesize=8, parity='N', stopbit=1, timeout=None, \
    xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None, exclusive=None)
    
    mSerial.read_data()

