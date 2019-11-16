import serial 
import time
from decimal import Decimal
import numpy as np

class Physical:
    ser = 0
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate = 115200, timeout = 5)
        self.ser.write('M21\r\n'.encode())  # Moved this first so it knows machine mode is active
        time.sleep(3)
        self.ser.write('M701\r\n'.encode())  # TODO: Make this check for completion because it could take more than 3 seconds
        time.sleep(3)
        # self.wait_for_completion()
        self.ser.write('M17\r\n'.encode())
        time.sleep(3)
        # self.wait_for_completion()
        self.ser.reset_input_buffer()
    
    def current_position(self):
        
        # print(self.ser.write(b'M114\r\n'))
        
        self.ser.write('M114\r\n'.encode())
        time.sleep(3)
        # self.wait_for_completion()

        self.ser.write('M18\r\n'.encode())
        time.sleep(3)
        # self.wait_for_completion()

        
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
                return round(float(Decimal(x)),2), round(float(Decimal(y)),2)    # Removed int conversion ans these have double precision


    def write_row(self, row1, row2, x, y):
        self.ser.write(('G1 x %s \r\n' % str(x).encode()).encode())  #TODO: Need to wait for one of these to complete before sending the other
        time.sleep(3) 
        self.wait_for_completion()
        self.ser.write(('G1 y %s \r\n' % str(y).encode()).encode())
        time.sleep(3) 
        self.wait_for_completion()

        line_one = []
        line_two = []
        print(np.shape(row1))
        print(np.shape(row2))
        # segment(major row_num, column (pod)_num, row of pod, col w/in pod)
        # row1(pod (column) num, row of pod, col w/in pod)

        start_num = 0
        num_chars = np.shape(row1)[0]
        for pod_row in range(3):
            for pod_col in range(2):
                # while pod_num < num_chars+1:
                #FIXME: WTAF Python?! No one likes you!! AHHHHHHH
                for pod_num in range(start_num, num_chars+1):
                    print('Pod Num %s' %pod_num)
                    print('Pod Col %s' %pod_col)
                    print('Pod Row %s' %pod_row)
                    print(row1[0, pod_num, pod_row, pod_col])
                    line_one.append(row1[pod_num,pod_row,pod_col])
                    print('Start Num %s' %start_num)
                    pod_num +=4
            start_num += 1    

        # for i, punch in enumerate(row2):
        #     if i%4 == 0:
        #         line_two.append(punch)

        # self.ser.write('F %' % (''.join(line_one)))   #TODO: Make these into one fire statement the firmware fires all 14 at once
        # self.wait_for_completion()
        self.ser.write('F %' % (''.join(line_two)))
        self.wait_for_completion()

    def wait_for_completion(self):
        while True:
            ser_in = self.ser.readline()
            print(ser_in)
            if ('0'.encode() in ser_in):
                return 0
            elif 'Position' in str(ser_in):
                return 0
            elif 'paper' in str(ser_in):
                return 0
            elif 'steppers' in str(ser_in):
                return 0
            elif 'Axis' in str(ser_in):
                return 0


    def load_paper(self):
        self.ser.write('M701\r\n'.encode())
        time.sleep(3)
        self.wait_for_completion()
    def unload_paper(self):
        self.ser.write('M702\r\n'.encode())
        time.sleep(3)
        self.wait_for_completion()
    def enable(self):
        self.ser.write('M17\r\n'.encode())
        time.sleep(3)
        self.wait_for_completion()
    def disable(self):
        self.ser.write('M18\r\n'.encode())
        time.sleep(3)        
        self.wait_for_completion()
    def home(self):
        self.ser.write('G28\r\n'.encode())
        time.sleep(3)        
        self.wait_for_completion()