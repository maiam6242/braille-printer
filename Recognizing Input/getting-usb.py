import subprocess
import sys
import time
import os
import playsound
from gtts import gTTS
import pyttsx

class GetUSB:

    def __int__(self) :
        pass

    def output_reader(self, proc):
            self.result = []
            while 1:
                line = proc.stdout.readline()
                if len(line) > 0: # If there is anything on the line

                    self.result.append( ('{0}'.format(line.decode('utf-8'), end='')))
                else:
                    return self.result

    def get(self):
        self.proc = subprocess.Popen(['./finding-usb.bash'], stdout=subprocess.PIPE)
        self.lines = self.output_reader(self.proc)
        self.lines = [s.strip('\n') for s in self.lines]
        return self.lines

    def read_out(self, lines):
        language = 'en'
        engine = pyttsx.init()
        for line in lines:
            engine.say(line)
            # lets_convert = gTTS(text=line, lang=language, slow=True)
            # lets_convert.save('line_to_read.wav')
            # playsound('line_to_read.wav')
            # os.system()
            time.sleep(2)
            
            


if __name__ == "__main__":
    usb = GetUSB()
    print(usb.read_out(usb.get()))
