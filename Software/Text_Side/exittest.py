import time
import os

try:
    while 1:
        print('Working')
        time.sleep(1)
        raise ValueError
except KeyboardInterrupt:
    raise KeyboardInterrupt
except:
    os.system("python3 exittest.py")
