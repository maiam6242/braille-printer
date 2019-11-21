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
        self.ser.write('M17\r\n'.encode())
        time.sleep(3)
        self.wait_for_completion()
        self.ser.reset_input_buffer()
    
    def current_position(self):
        '''
        Finds the current postion of the steppers in terms of x and y
        Returns: the values associated with the current position in the form x, y
        '''
        # print(self.ser.write(b'M114\r\n'))
        
        self.ser.write('M114\r\n'.encode())
        time.sleep(3)
        # self.wait_for_completion()

        self.ser.write('M17\r\n'.encode())
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
        '''
        Writes two entire consecutive rows of braille text (punches the solenoids)
        Args: The rows to write and the inital x and y positions where to begin the writing
        '''
        print('write row position: %s' %y)
        print(str(y).encode())
        print(('G1 y %s \r\n' % str(y)).encode())
        self.ser.write(('G1 x %s \r\n' % str(x)).encode())  #TODO: Need to wait for one of these to complete before sending the other
        time.sleep(3) 
        self.wait_for_completion()
        
        self.ser.write(('G1 y %s \r\n' % str(y)).encode())
        time.sleep(3) 
        self.wait_for_completion()

        line_one = ""
        line_two = ""
     
        sol_commands = []
        print(np.shape(row1))
        print(np.shape(row2))
        
        # segment(major row_num, column (pod)_num, row of pod, col w/in pod)
        # row1(pod (column) num, row of pod, col w/in pod)

        num_chars = np.shape(row1)[0]
        print("the size of the first line is:")
        print(np.shape(row1))
        for pod_row in range(3):
            for sol_chars in range(4):
                for pod_col in range(2):
                    pod_num = sol_chars
                    while pod_num >= 0 and pod_num < num_chars:
                        print('Pod Num %s' %pod_num)
                        print('Pod Row %s' %pod_row)
                        print('Pod Col %s' %pod_col)
                        print(row1[pod_num, pod_row, pod_col])
                        
                        if pod_num < np.shape(row1)[0]:
                            line_one += str(row1[pod_num, pod_row, pod_col])
                        if pod_num < np.shape(row2)[0]:
                            line_two += str(row2[pod_num, pod_row, pod_col])
                        pod_num +=4 
                                      
                    sol_commands.append(line_one+line_two)
                  
                    line_one = ""
                    line_two = ""
                    
        # print(np.shape(sol_punches_one)[0])
        # print(sol_punches_one)
        print(np.shape(sol_commands))
        print(sol_commands)
        print(sol_commands[0])
        for command in sol_commands:
            self.wait_for_completion()
            self.ser.write(('F x %s \r\n' % str(command).encode()).encode())  
            
        
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
            elif 'Going' in str(ser_in):
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