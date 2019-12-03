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
            self.engine.runAndWait()
        self.error.on()

    def resolve_error(self):
        if(bool(self.sound.is_pressed)):
            self.engine.say("The error has been resolved")
            self.engine.runAndWait()
        self.error.off()

    def signal_ready(self):
        if(bool(self.sound.is_pressed)):
            self.engine.say("The printer is ready to print")
            self.engine.runAndWait()
        self.ready.on()

    def resolve_ready(self):
        self.ready.off()

    def wait_for_play(self):
        self.play.wait_for_press()

    def wait_for_print(self):
        self.start_print.wait_for_press()

    #Checks to see if buttons are pressed/sound switch is on

    def is_sound(self):
	# Checks to see if sound has been changed from OFF to ON
        if(bool(self.sound.is_pressed)):
            if(self.sound_triggered):
                self.engine.say("Sound is on")
                self.engine.runAndWait()
                self.sound_triggered = False
                print('Sound switched on')
        else:
            self.sound_triggered = True
	
	#True if ON, False if OFF
        return bool(self.sound.is_pressed)


    def is_cancel(self):
        #Checks to see if cancel button is pressed
        if(bool(self.cancel.is_pressed)):
            # If sound is on, speak
            if(self.cancel_triggered):
                if(bool(self.sound.is_pressed)):
                    self.engine.say("Process Canceled")
                    self.engine.runAndWait()
                self.cancel_triggered = False
                print('Cancel button pressed')
        else:
            self.cancel_triggered = True

        return bool(self.cancel.is_pressed)


    def is_play_pause(self):
        # Checks to see if play/pause button has been pressed
        # Keeps track of whether the state is to play or to pause 
        #TODO: Need a method (elsewhere probably) that defaults to pause when print starts
        if(bool(self.play.is_pressed)):
            if(self.play_triggered):
                # If sound is on, speak
                if(bool(self.sound.is_pressed)):
                    if(self.is_play):
                        self.engine.say("Process Continuing")
                        self.engine.runAndWait()
                        self.is_play = False
                    else:
                        self.engine.say("Process is Paused")
                        self.engine.runAndWait()
                        self.is_play = True
                self.play_triggered = False
                print('play/pause button pressed')
        else:
            self.play_triggered = True

        return bool(self.play.is_pressed)


    def is_start_print(self):
        #Checks to see if start print button is pressed
        if(bool(self.start_print.is_pressed)):
            if(self.print_triggered):
                # If sound is on, speak
                if(bool(self.sound.is_pressed)):
                    self.engine.say("Printing")
                    self.engine.runAndWait()
                self.print_triggered = False
                print('print button pressed')
        else:
            self.print_triggered = True
        return bool(self.start_print.is_pressed)


if __name__ == "__main__":
    import time
    interface = Interface(1)
    #TODO: Right now, the code is taking too long to respond to the below operators. Need to call
    #methods within the methods to make sure that they are called.
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

