import serial

class physical:
    ser = 0
    def __init__(self, port):
        self.ser = serial.Serial(port, 115200)
        self.ser.write('M21')
    
    def current_position(self):
        self.ser.write('current_position_placeholder')
        while (True):
            ser_in = self.ser.readline()
            # in the form of Position: x,y
            if('Position' in ser_in):
                ser_in = ser_in.replace("Position: ", "")
                x, y = ser_in.split(',')
                return int(x), int(y)

            


    