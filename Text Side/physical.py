import serial
import time
from decimal import Decimal

class physical:
    ser = 0
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate = 115200, timeout = 5)
        self.ser.write('M701\r\n'.encode())
        time.sleep(3)
        self.ser.write('M21\r\n'.encode())
        time.sleep(3)
        self.ser.write('M17\r\n'.encode())
        time.sleep(3)
        self.ser.reset_input_buffer()
    
    def current_position(self):
        
        # print(self.ser.write(b'M114\r\n'))
        
        self.ser.write('M114\r\n'.encode())
        time.sleep(3)
        
        self.ser.write('M18\r\n'.encode())
        time.sleep(3)
        
        # self.ser.flushInput() # does this actually work?
        time.sleep(3)
        # print(self.ser.in_waiting)
        print('ahhhh!')
        # # print(self.ser.read())
        while (True):
            # print(self.ser.in_waiting)
            ser_in = self.ser.readline()
            print('Yooo am I here?')
            # in the form of Position: x,y
            print(ser_in)
            if('Position' in str(ser_in)):
                ser_in = str(ser_in).replace("b'Position:", "")
                ser_in = ser_in.replace(r"\r\n'", "")
                x, y = ser_in.split(',')
                print(int(Decimal(x)))
                print(int(Decimal(y)))
                return int(Decimal(x)), int(Decimal(y))


    def write_row(self, segment1, segment2, x, y):
        self.ser.write('G1 x %f' % x)
        self.ser.write('G1 y %f' % y)

        line_one = []
        line_two = []
        for i, punch in enumerate(segment1):
            if i%4 == 0:
                line_one.append(punch)
        for i, punch in enumerate(segment2):
            if i%4 == 0:
                line_two.append(punch)

        self.ser.write('F %' % (''.join(line_one)))
        wait_for_completion()
        self.ser.write('F %' % (''.join(line_two)))
        wait_for_completion()

    def wait_for_completion(self):
        while True:
            ser_in = self.ser.readline()
            if ser_in == '0':
                return 0

    def load_paper(self):
        self.ser.write('M701')
        wait_for_completion()
    def unload_paper(self):
        self.ser.write('M702')
        wait_for_completion()
    def enable(self):
        self.ser.write('M17')
        wait_for_completion()
    def disable(self):
        self.ser.write('M18')
        wait_for_completion()
    def home(self):
        self.ser.write('G28')
        wait_for_completion()