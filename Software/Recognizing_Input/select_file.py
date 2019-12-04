import os
import sys
from Recognizing_Input.getting_usb import GetUSB
from Recognizing_Input.getting_web import GetWEB
import pyttsx3


def select_file():
    """Selects a file from the web or usb interface"""

    usb_getter = GetUSB()
    web_getter = GetWEB()

    web_files = []
    usb_files = []
    while 1:
        web_files = web_getter.get()
        usb_files = usb_getter.get()
        # usb_files = []

        if not web_files == []:
            print('web files:' + str(web_files))
            path = 'WebInterface/uploads/' + str(web_files[0])
            break

        if not usb_files == []:
            print('usb files:' + str(usb_files))
            # usb_getter.read_out(usb_files)
            #TODO: Add selection interface code here
            selected_file = usb_files[0]
            path = str(selected_file)
            break

    return path



    # parser = Text_Parse()
    # segmented = parser.break_up_text_input(parser.read_text_file(file_path))

def clear_web():
    os.system('bash clear-web.sh')

def clear(path):
    os.system('rm ' + path)



if __name__ == "__main__":
    path = select_file()
    print(path)
    clear(path)
    # clear_web()
