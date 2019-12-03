"""Interface class for GPIO """
import serial
import pyttsx3
from gpiozero import LED, Button

class Interface:
    """Creates interface to the raspi GPIO pins to control the buttons and leds of the UI"""
    
    def __init__(self, serial):
        self.engine = pyttsx3.init()
        self.voices = engine.getProperty('voices')
        self.engine.setProperty('rate', 130)
        self.engine.setProperty('voice', voices[11].id)

        self.error = LED(20) #checked
        self.ready = LED(16) #checked
        self.start_print = Button(26) #checked
        self.play = Button(13) #checked
        self.cancel = Button(6) #checked
        self.sound = Button(19) #checked
        self.ser = serial

    def signal_error(self):
        if(bool(self.sound.is_pressed)):
            self.engine.say("There has been an error")
        self.error.on()

    def resolve_error(self):
        if(bool(self.sound.is_pressed)):
            self.engine.say("The error has been resolved")
        self.error.off()

    def signal_ready(self):
        if(bool(self.sound.is_pressed)):
            self.engine.say("The printer is ready to print")
        self.ready.on()

    def resolve_ready(self):
        self.ready.off()

    def wait_for_play(self):
        self.play.wait_for_press()

    def wait_for_print(self):
        self.start_print.wait_for_press()

   #Checks to see if buttons are pressed/sound switch is on

    def is_sound(self):
        if(bool(self.sound.is_pressed)):
            engine.say("Sound is on")
        #if(self.sound.is_pressed):
            #print('Sound is pressed!')
        return bool(self.sound.is_pressed)

    def is_cancel(self):
        #if(self.cancel.is_pressed):
        #    print('Cancel is Pressed!')
        # self.ser.write('G1 x 0 \r\n'.encode())
        # self.ser.write('M18'.encode())
        # self.ser.write('M702'.encode())
        if(bool(self.sound.is_pressed) and self.cancel.is_pressed):
            engine.say("Process Canceled")
        return bool(self.cancel.is_pressed)

    #TODO: This should probably be different!! How?!
    def is_play_pause(self):
        if(bool(self.sound.is_pressed) and self.play.is_pressed):
            engine.say("Process Continuing")
        elif(bool(self.sound.is_pressed) and not self.play.is_pressed):
            engine.say("Process is Paused")
        #if(self.play.is_pressed):
            #print('Play Pause is Pressed!')
        return bool(self.play.is_pressed)

    def is_start_print(self):
        if(bool(self.sound.is_pressed) and self.start_print.is_pressed):
            engine.say("Printing")
        #if(self.start_print.is_pressed):
            #print('Start Print is Pressed!')
        return bool(self.start_print.is_pressed)


if __name__ == "__main__":
    import time
    interface = Interface(1)
    while 1:
        if(interface.is_start_print()):
            print('Is start print %s' %interface.is_start_print())
        if(interface.is_sound()):
            print('Is sound %s' %interface.is_sound())
        if(interface.is_play_pause()):
            print('Is play pause %s' %interface.is_play_pause())
        if(interface.is_cancel()):
            print('Is cancel %s' %interface.is_cancel())
        if interface.is_cancel() or interface.is_play_pause() or interface.is_start_print():

            interface.signal_ready()
            time.sleep(.5)
            interface.resolve_ready()
            time.sleep(.5)
            
            interface.signal_error()
            time.sleep(.5)
            interface.resolve_error()
            time.sleep(.5)

