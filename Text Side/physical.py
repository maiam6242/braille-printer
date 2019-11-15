import serial
import time
from decimal import Decimal

class physical:
    ser = 0
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate = 115200, timeout = 5)
        self.ser.write('M21\r\n'.encode())  # Moved this first so it knows machine mode is active
        time.sleep(3)
        self.ser.write('M701\r\n'.encode())  #TODO: Make this check for completion because it could take more than 3 seconds
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
                print((Decimal(x)))
                print((Decimal(y)))
                return Decimal(x), Decimal(y)    # Removed int conversion ans these have double precision


    def write_row(self, segment1, segment2, x, y):
        self.ser.write('G1 x %f' % x)  #TODO: Need to wait for one of these to complete before sending the other
        self.ser.write('G1 y %f' % y)

        line_one = []
        line_two = []
        for i, punch in enumerate(segment1):
            if i%4 == 0:
                line_one.append(punch)
        for i, punch in enumerate(segment2):
            if i%4 == 0:
                line_two.append(punch)

        self.ser.write('F %' % (''.join(line_one)))   #TODO: Make these into one fire statement the firmware fires all 14 at once
        self.wait_for_completion()
        self.ser.write('F %' % (''.join(line_two)))
        self.wait_for_completion()

    def wait_for_completion(self):
        while True:
            ser_in = self.ser.readline()
            if ser_in == '0':
                return 0

    def load_paper(self):
        self.ser.write('M701')
        self.wait_for_completion()
    def unload_paper(self):
        self.ser.write('M702')
        self.wait_for_completion()
    def enable(self):
        self.ser.write('M17')
        self.wait_for_completion()
    def disable(self):
        self.ser.write('M18')
        self.wait_for_completion()
    def home(self):
        self.ser.write('G28')
        self.wait_for_completion()