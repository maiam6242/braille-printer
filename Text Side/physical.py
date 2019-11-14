import serial

class physical:
    ser = 0
    def __init__(self, port):
        self.ser = serial.Serial(port, 115200)
        self.ser.write('M21'.encode())
    
    def current_position(self):
        self.ser.write('M114'.encode())
        print('written, baby!')
        while (True):
            ser_in = self.ser.readline()
            print('Yooo am I here?')
            # in the form of Position: x,y
            print(ser_in)
            if('Position' in ser_in):
                ser_in = ser_in.replace("Position: ", "")
                x, y = ser_in.split(',')
                return int(x), int(y)


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