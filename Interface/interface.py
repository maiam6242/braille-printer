"""Interface class for GPIO """
import serial
import pyttsx3
from gpiozero import LED, Button

class Interface:
    """Creates interface to the raspi GPIO pins to control the buttons and leds of the UI"""
    
    def __init__(self, serial):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('rate', 130)
        self.engine.setProperty('voice', self.voices[11].id)

        self.error = LED(20) #checked
        self.ready = LED(16) #checked
        self.start_print = Button(26) #checked
        self.play = Button(13) #checked
        self.cancel = Button(6) #checked
        self.sound = Button(19) #checked
        self.ser = serial
        
        #checks if the buttons/switch change to an "on" state
        self.sound_triggered = False
        self.play_triggered = False
        self.print_triggered = False
        self.cancel_triggered = False
        
        #boolean to distinguish if press is for play or pause
        self.is_play = True

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
            if(self.sound_triggered):
                self.engine.say("Sound is on")
                self.sound_triggered = False
                #print('Sound switched on')
        else:
            self.sound_triggered = True

        return bool(self.sound.is_pressed)

    def is_cancel(self):

        if(bool(self.cancel.is_pressed)):
            if(self.cancel_triggered):
                if(bool(self.sound.is_pressed)):
                    self.engine.say("Process Canceled")
                self.cancel_triggered = False
        else:
            self.sound_triggered = True

        return bool(self.cancel.is_pressed)

    #TODO: This should probably be different!! How?!

    def is_play_pause(self):

        if(bool(self.play.is_pressed)):
            if(self.play_triggered):
                if(bool(self.sound.is_pressed)):
                    if(self.is_play):
                        self.engine.say("Process Continuing")
                        self.is_play = False
                    else:
                        self.engine.say("Process is Paused")
                        self.is_play = True
                self.play_triggered = False
        else:
            self.play_triggered = True

        return bool(self.play.is_pressed)

    def is_start_print(self):
        if(bool(self.start_print.is_pressed)):
            if(self.print_triggered):
                if(bool(self.sound.is_pressed)):
                    self.engine.say("Printing")
                self.print_triggered = False
        else:
            self.print_triggered = True
        return bool(self.start_print.is_pressed)


if __name__ == "__main__":
    import time
    interface = Interface(1)
    while 1:
        if(interface.is_start_print() and interface.print_triggered):
            print('Is start print %s' %interface.is_start_print())
        if(interface.is_sound() and interface.sound_triggered):
            print('Is sound %s' %interface.is_sound())
        if(interface.is_play_pause() and interface.play_triggered):
            print('Is play pause %s' %interface.is_play_pause())
        if(interface.is_cancel() and interface.cancel_triggered):
            print('Is cancel %s' %interface.is_cancel())
        #if interface.is_cancel() or interface.is_play_pause() or interface.is_start_print():

            #interface.signal_ready()
            #time.sleep(.5)
            #interface.resolve_ready()
            #time.sleep(.5)
            
            #interface.signal_error()
            #time.sleep(.5)
            #interface.resolve_error()
            #time.sleep(.5)

