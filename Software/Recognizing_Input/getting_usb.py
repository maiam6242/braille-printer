"""Module to find text files on a usb"""
import subprocess
import time
import pyttsx3
import sys
sys.path.append(".")
from Physical_Interface.interface import Interface

class GetUSB:
    """Find files from any inserted media"""

    def __init__(self, interface):
        self.interface = interface
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
        """Gets a list of paths to text files in the removable media
        Returns a list of strings which specify absolute paths to usb files"""

        self.proc = subprocess.Popen(['bash', 'Recognizing_Input/finding-usb.sh'], \
            stdout=subprocess.PIPE)
        self.lines = self.output_reader(self.proc)
        self.lines = [s.strip('\n') for s in self.lines]
        return self.lines

    def read_out(self, lines):
        """Reads the names of the files
        Takes a list of strings and reads them one by one"""
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 130)
        engine.setProperty('voice', voices[11].id)

        for count, line in enumerate(lines):
            if interface.is_sound():
                engine.say(line.split('/')[-1])
                engine.runAndWait()
            print(count)
            print(line)
            last_time = time.time()
            while time.time() < last_time + 3:
                self.interface.check_buttons()
                if self.interface.start_print.is_pressed:
                    print("selecting your choice")
                    if interface.is_sound():
                        engine.say("selecting your choice")
                        engine.runAndWait()
                    return lines[count]
        
        print("No file chosen, printing first file")
        if interface.is_sound():
            engine.say("No file chosen, printing first file")
            engine.runAndWait()
        return lines[0]

if __name__ == "__main__":
    usb = GetUSB()
    files = usb.get()
    print((usb.get()))
    print(type(usb.get()))
    usb.read_out(files)
