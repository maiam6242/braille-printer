import subprocess
import sys

class GetUSB:

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
        lines = self.output_reader(self.proc)
        return lines
