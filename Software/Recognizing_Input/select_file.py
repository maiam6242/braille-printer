import os
import sys
from getting_usb import GetUSB
from getting_web import GetWEB
import pyttsx3


def select_file():
    """Selects a file from the web or usb interface"""

    usb_getter = GetUSB()
    web_getter = GetWEB()


    while 1:
        web_files = web_getter.get()
        # usb_files = usb_getter.get()
        usb_files = []

        if len(web_files):
            path = '/WebInterface/uploads/' + str(web_files[0])
            break

        if len(usb_files):
            usb_getter.read_out(usb_files)
            #TODO: Add selection interface code here
            selected_file = usb_files[0]
            path = '/media/pi/' + str(selected_file)

    return path



    # parser = Text_Parse()
    # segmented = parser.break_up_text_input(parser.read_text_file(file_path))

def clear_web():
    os.system('bash clear-web.sh')

def clear(path):
    os.system('rm ' + '..' +path)



if __name__ == "__main__":
    path = select_file()
    print(path)
    clear(path)
    # clear_web()
