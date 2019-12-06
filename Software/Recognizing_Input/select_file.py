'''Selects the file to be printed from possible files on web and usb'''
import os
import sys
sys.path.append(".")
from Recognizing_Input.getting_usb import GetUSB
from Recognizing_Input.getting_web import GetWEB
from Physical_Interface.interface import Interface
import pyttsx3

def select_file(interface):
    '''Selects a file from the web or usb interface'''
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 130)
    engine.setProperty('voice', voices[11].id)
    
    usb_getter = GetUSB(interface)
    web_getter = GetWEB()

    web_files = []
    usb_files = []
    while 1:
        web_files = web_getter.get()
        usb_files = usb_getter.get()
        

        if not web_files == []:
            print('web files:' + str(web_files))
            web_getter.read_out(web_files)
            path = 'WebInterface/uploads/' + str(web_files[0])
            break

        if not usb_files == []:
            if len(usb_files) > 0:
                engine.say('Please select the middle play pause button when you would like to select the file which you heard previously')
            
            print('usb files:' + str(usb_files))
            selected_file = usb_getter.read_out(usb_files)
            #TODO: Add selection interface code here
            # selected_file = usb_files[0]
            path = str(selected_file)
            break

    return path

def clear_web():
    '''Clears the web dump folder (WebInterface/uploads)'''
    os.system('bash clear-web.sh')

def clear(path):
    '''Clears the selected file from the folder'''
    os.system('rm ' + path)



if __name__ == '__main__':
    path = select_file()
    print(path)
    clear(path)
    # clear_web()
