"""Handles physical attribtes of the machine"""

import time
from decimal import Decimal
import sys
import serial
import numpy as np
sys.path.append(".")
from Physical_Interface.interface import Interface

class Physical:
    """Handles physical attribtes of the machine"""
    # ser = 0
    def __init__(self, ser, character_width, character_height, interface):
        self.char_height = character_height
        self.char_width = character_width
        self.ser = ser
        self.physical_interface = interface
        # self.ser.write('M21\r\n'.encode())  # Moved this first so it knows machine mode is active
        # time.sleep(1)
        self.ser.write('M17\r\n'.encode())
        self.physical_interface.sleep(1)
        # self.wait_for_completion()
        self.ser.reset_input_buffer()

    def current_position(self):
        '''
        Finds the current postion of the steppers in terms of x and y
        Returns: the values associated with the current position in the form x, y
        '''
        # if(not self.physical_interface.is_play_pause()):
             # self.physical_interface.wait_for_play()
        # print(self.ser.write(b'M114\r\n'))

        #TODO: check below 7 lines for check buttons stuff
        if not self.physical_interface.is_cancel() and self.physical_interface.is_play():
            self.ser.write('M114\r\n'.encode())
            self.physical_interface.sleep(1)
      
        while True:
            # print(self.ser.in_waiting)
            ser_in = self.ser.readline()
            print('[physical.py]','Yooo am I here?')
            self.physical_interface.check_buttons()
            # in the form of Position: x,y
            print('[physical.py]',ser_in)
            if 'Position' in str(ser_in):
                self.physical_interface.check_buttons()
                ser_in = str(ser_in).replace("b'Position:", "")
                ser_in = ser_in.replace(r"\r\n'", "")
                x, y = ser_in.split(',')
                print("[physical.py] ", (Decimal(x)))
                print("[physical.py] ",(Decimal(y)))
                return round(float(Decimal(x)), 2), \
                   round(float(Decimal(y)), 2)
                        # Removed int conversion ans these have double precision


    def write_row(self, row1, row2, x, y):
        '''
        Writes two entire consecutive rows of braille text (punches the solenoids)
        Args: The rows to write and the inital x and y positions where to begin the writing
        row1 (np.array): The first row of dots
        '''
        cal_values = [0, 2, 6, 8, 12.3, 14.3, 18.5, 20.5]
        sol_commands = []
        
        if (self.physical_interface.check_buttons()):
            print('[physical.py] ','write row position: %s' %y)
            print('[physical.py] ', str(y).encode())
            print(('[physical.py] G1 y %s \r\n' % str(y)).encode())
            self.ser.write(('G1 x %s \r\n' % str(x)).encode())  #TODO: Need to wait for one of these to complete before sending the other
            self.physical_interface.sleep(1)
            self.wait_for_completion()

        if (self.physical_interface.check_buttons()):
            self.ser.write(('G1 y %s \r\n' % str(y)).encode())
            self.physical_interface.sleep(1) 
            self.wait_for_completion()

            line_one = ''
            line_two = ''

            print('[physical.py] ', np.shape(row1))
            print('[physical.py] ', np.shape(row2))

        # segment(major row_num, column (pod)_num, row of pod, col w/in pod)
        # row1(pod (column) num, row of pod, col w/in pod)
        if (self.physical_interface.check_buttons()):
            num_chars = np.shape(row1)[0]
            #print('[physical.py] ','the braille of the first line is: ')
            #print('[physical.py] ', row1)
            for pod_row in range(3):
                for sol_chars in range(4):
                    for pod_col in range(2):
                        pod_num = sol_chars
                        while pod_num >= 0 and pod_num < num_chars:
                            #print('[physical.py] ','Pod Num %s' %pod_num)
                            #print('[physical.py] ','Pod Row %s' %pod_row)
                            #print('[physical.py] ','Pod Col %s' %pod_col)
                            #print(row1[pod_num, pod_row, pod_col])

                            if pod_num < np.shape(row1)[0]:
                                line_one += str(row1[pod_num, pod_row, pod_col])
                            if row2.any():
                                line_two += str(row2[pod_num, pod_row, pod_col])
                            else: 
                                line_two = '00000000000000'
                            pod_num += 4

                        sol_commands.append(line_one+line_two)
                        line_one = ""
                        line_two = ""

        # print(np.shape(sol_punches_one)[0])
        # print(sol_punches_one)
                print('[physical.py] ',np.shape(sol_commands))
                print('[physical.py] ',sol_commands)
                print('[physical.py] ',sol_commands[0])

        row_in_pod = 1 #starts at index 1 because will never reach 3

        for i, command_string in enumerate (sol_commands):
                self.physical_interface.check_buttons()
                is_command_blank = command_string == '00000000000000'
                print('[physical.py] ',command_string)
                print('[physical.py] ',is_command_blank)
                print('[physical.py] ',i)

                #if not is_command_blank:
                    #self.ser.write(('F %s \r\n' % str(command_string)).encode())
                   # print('F %s \r\n' % str(command_string))
                   # self.physical_interface.sleep(4)
            # self.wait_for_completion()
            # if (self.physical_interface.check_buttons()):
                if(i % 8 == 0 and not i == 0):
                    self.physical_interface.check_buttons()
                    x = 0
                    print('not lower loop ' +str(i))
                    print('[physical.py]', 'x %s' %x)
                    y += row_in_pod * (self.char_height/3)
                    self.ser.write(('G1 y %s \r\n' % str(y)).encode())
                    self.physical_interface.sleep(1)
                    self.wait_for_completion()
                    self.ser.write(('G1 x %s \r\n' % str(x)).encode())
                    self.physical_interface.sleep(1)
                    self.wait_for_completion()
                    row_in_pod += 1
                # elif i%2 ==0 use list
                else:
                    self.physical_interface.check_buttons()
                    print('lower loop ' +str(i))
                    x = cal_values[(i)%8]
                    print('x: ' + str(x))
                    print('i%8: ' + str((i)%8))
                    print('cal_values[(i)%8]: ' + str(cal_values[(i)%8]))
                    # x += self.char_height/2
                    if not is_command_blank:
                        print('[physical.py]','x %s' %x)
                        self.ser.write(('G1 x %s \r\n' % str(x)).encode())
                        self.physical_interface.sleep(1)
                        self.wait_for_completion()
                if not is_command_blank:
                    self.ser.write(('F %s \r\n' % str(command_string)).encode())
                    print('F %s \r\n' % str(command_string))
                    self.physical_interface.sleep(1)
    def write_in_order(self):
        for i in range(1,15): 
        
            string = '0'*(i-1) + '1' + '0'* (15-i)
            
            self.ser.write(('F %s \r\n' % str(string)).encode())
            self.physical_interface.sleep(1)
            self.wait_for_completion()

    def wait_for_completion(self):
        ''' Waits for a serial return to continue '''
        begin_time = time.time()
        timeout = 5 # Seconds until it signals error
        while True:
            if time.time() > begin_time + timeout and not self.physical_interface.error.is_on():
                self.physical_interface.signal_error()
            ser_in = self.ser.readline()
            print(ser_in)
            if ser_in:
                self.physical_interface.resolve_error()
                return 0

    def load_paper(self):
        '''Loads paper'''
        if (self.physical_interface.check_buttons()):
            self.ser.write('M701\r\n'.encode())
            self.physical_interface.sleep(1)
            self.wait_for_completion()
    def unload_paper(self):
        '''Unloads paper'''
        if (self.physical_interface.check_buttons()):
            self.ser.write('M702\r\n'.encode())
            self.physical_interface.sleep(1)
            self.wait_for_completion()
    def enable(self):
        '''Enables steppers'''
        if (self.physical_interface.check_buttons()):
            self.ser.write('M17\r\n'.encode())
            self.physical_interface.sleep(1)
            self.wait_for_completion()
    def disable(self):
        '''Disables steppers'''
        if (self.physical_interface.check_buttons()):
            self.ser.write('M18\r\n'.encode())
            self.physical_interface.sleep(1)        
            self.wait_for_completion()
    def home(self):
        '''Homes x axis'''
        if (self.physical_interface.check_buttons()):
            self.ser.write('G28\r\n'.encode())
            self.physical_interface.sleep(1)
            self.wait_for_completion()
