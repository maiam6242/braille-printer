"""Module to find text files on a usb"""
import subprocess
import time
import pyttsx3

class GetUSB:
    """Find files from any inserted media"""

    def __int__(self):
        pass

    def output_reader(self, proc):
        """Reads outputs from the stdout"""
        self.result = []
        while 1:
            line = proc.stdout.readline()
            if len(line) > 0: # If there is anything on the line
                self.result.append(('{0}'.format(line.decode('utf-8'), end='')))
            else:
                return self.result

    def get(self):
        """Gets a list of paths to text files in the removable media"""
        self.proc = subprocess.Popen(['bash', 'Recognizing_Input/finding-usb.sh'], \
            stdout=subprocess.PIPE)
        self.lines = self.output_reader(self.proc)
        self.lines = [s.strip('\n') for s in self.lines]
        return self.lines

    def read_out(self, lines):
        """Reads the names of the files"""
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 130)
        engine.setProperty('voice', voices[11].id)

        for count, line in enumerate(lines):
            engine.say(line)
	    # print('hey, let's read some shit')
            print(count)
            print(line)
            time.sleep(2)
        engine.runAndWait()

if __name__ == "__main__":
    usb = GetUSB()
    files = usb.get()
    print((usb.get()))
    print(type(usb.get()))
    usb.read_out(files)
