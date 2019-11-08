import serial

class physical:
    ser = 0
    def __init__(self, port):
        self.ser = serial.Serial(port, 115200)
        # self.ser.write('M21')
    
    def current_position(self):
        self.ser.write('M114')
        while (True):
            ser_in = self.ser.readline()
            # in the form of Position: x,y
            if('Position' in ser_in):
                ser_in = ser_in.replace("Position: ", "")
                x, y = ser_in.split(',')
                return int(x), int(y)


    def write_row(self, segment, x, y):
        pass


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