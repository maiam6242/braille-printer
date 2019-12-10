'''Module to find text files that were added by the web interface'''
import subprocess
import sys
import time
import pyttsx3

class GetWEB:
    ''' Gets a list of documents from the folder accessed by the web interface '''

    def __init__(self, interface):
        self.interface = interface

    def output_reader(self, proc):
        ''' Reads the stdout '''
        self.result = []
        while 1:
            line = proc.stdout.readline()
            if line: # If there is anything on the line

                self.result.append(('{0}'.format(line.decode('utf-8'), end='')))
            else:
                return self.result

    def get(self):
        '''Get the list of files '''
        self.proc = subprocess.Popen(['bash', 'Recognizing_Input/finding-web.sh'], \
            stdout=subprocess.PIPE)
        self.lines = self.output_reader(self.proc)
        self.lines = [s.strip('\n') for s in self.lines]
        return self.lines

    def read_out(self, lines):
        '''Read the lines over speaker'''
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 130)
        engine.setProperty('voice', voices[11].id)

        for count, line in enumerate(lines):
            if self.interface.is_sound():
                engine.say(line)
	    # print('hey, let's read some shit')
            print(count)
            print(line)
            time.sleep(2)
        if self.interface.is_sound():
            engine.runAndWait()

if __name__ == '__main__':
    usb = GetWEB()
    files = usb.get()
    print((usb.get()))
    print(type(usb.get()))
    usb.read_out(files)
