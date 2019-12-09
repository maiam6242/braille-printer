'''Interface class for GPIO '''
import serial
import pyttsx3
from gpiozero import LED, Button
import time

class Interface:
    '''Creates interface to the raspi GPIO pins to control the buttons and leds of the UI'''
    
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
        self.is_play_active = True
        self.is_cancel_active = False
        self.is_sound_active = False
        self.is_start_active = False

        # Debouncing boolean
        self.last_time = time.time()

    def debounced(self):
        if .1 + self.last_time < time.time():
            self.last_time = time.time()
            debounced = True
        else:
            debounced = False
        return debounced

    def signal_error(self):
        self.error.on()
        if self.sound.is_pressed:
            self.engine.say('There has been an error')
            self.engine.runAndWait()

    def resolve_error(self):
        self.error.off()
        if self.sound.is_pressed:
            self.engine.say('The error has been resolved')
            self.engine.runAndWait()

    def signal_ready(self):
        if self.sound.is_pressed:
            self.engine.say('The printer is ready to print')
            self.engine.runAndWait()
        self.ready.on()

    def resolve_ready(self):
        self.ready.off()

    def wait_for_play(self):
        self.play.wait_for_press()

    def wait_for_print(self):
        self.signal_ready()
        self.start_print.wait_for_press()

    def is_sound(self):
        if self.sound.is_pressed and not self.is_sound_active:
            self.engine.say('Sound is on')
            self.engine.runAndWait()
            print('[interface.py] ','Sound switched on')
            self.is_sound_active = True
        if not self.sound.is_pressed:
            self.is_sound_active = False
        return not self.sound.is_pressed


    def is_cancel(self):

        if self.cancel.is_pressed:
            self.is_cancel_active = True
            print('Process Cancelling')
            self.engine.say('Process Canceled')
            self.engine.runAndWait()
            raise KeyboardInterrupt 
        return self.is_cancel_active
    
    
    def check_buttons(self):
        '''Checks the status of the buttons and returns true if it should continue'''
        self.is_play()
        self.is_cancel()    
        return True
            
    def sleep(self, amount_of_seconds):
        time_start = time.time()  
        while time.time() < time_start + amount_of_seconds:
            self.is_play()
            self.is_cancel()

    def is_play(self):
        ''' Checks if the print should be played and holds if it should not'''
        if self.play.is_pressed and self.debounced():
            self.is_play_active = not self.is_play_active
            if self.is_play_active:
                print ('Playing')
                self.engine.say('Playing')
                self.engine.runAndWait()
            if not self.is_play_active:
                print ('Paused')
                self.engine.say('Paused')
                self.engine.runAndWait()
                while not self.is_play_active:
                    self.is_cancel()
                    if self.play.is_pressed and self.debounced():
                        self.is_play_active = True
                print ('Playing')
                self.engine.say('Playing')
                self.engine.runAndWait()
                
            # print ("Play is " + str(self.is_play_active))
        return self.is_play_active
    
    def is_start_print(self):
        if self.start_print.is_pressed and self.debounced():
            self.is_start_active = not self.is_start_active
        if self.is_start_active:
            print ('Starting Print')
            self.engine.say('Printing')
            self.engine.runAndWait()
            self.resolve_ready()

        return self.is_start_active



    #Checks to see if buttons are pressed/sound switch is on

    # def is_sound(self):
	# # Checks to see if sound has been changed from OFF to ON
    #     if self.sound.is_pressed :
    #         if(self.sound_triggered):
    #             self.engine.say("Sound is on")
    #             self.engine.runAndWait()
    #             self.sound_triggered = False
    #             print('[interface.py] ','Sound switched on')
    #             return True
    #     else:
    #         self.sound_triggered = True
    #         return False
	#True if ON, False if OFF
        #return bool(self.sound.is_pressed)

    
    # def is_cancel(self):
    #     #Checks to see if cancel button is pressed
    #     if self.cancel.is_pressed:
    #         if(self.cancel_triggered):
    #             if(bool(self.sound.is_pressed)):
    #                 self.engine.say("Process Canceled")
    #                 self.engine.runAndWait()
    #             self.cancel_triggered = False
    #             print('[interface.py] ','Cancel button pressed')
    #             return True
    #     else:
    #         self.cancel_triggered = True
    #         return False
    #     # return bool(self.cancel.is_pressed)

    # def is_play_pause(self):
        # # Checks to see if play/pause button has been pressed
        # # Keeps track of whether the state is to play or to pause 
        # # TODO: Need a method (elsewhere probably) that defaults to pause when print starts
        # if(bool(self.play.is_pressed)):
          #   if(self.play_triggered):
          #       # If sound is on, speak
          #       if(bool(self.sound.is_pressed)):
          #           if(self.is_play):
          #               self.engine.say("Process Continuing")
          #               self.engine.runAndWait()
          #               self.is_play = False
          #           else:
          #               self.engine.say("Process is Paused")
          #               self.engine.runAndWait()
          #               self.is_play = True
          #               self.wait_for_play()
          #       self.play_triggered = False
          #       print('[interface.py] ','play/pause button pressed')
          #       return True
        # else:
          #   self.play_triggered = True
          #   return False

       # return bool(self.play.is_pressed)


    # def is_start_print(self):
    #     #Checks to see if start print button is pressed
    #     if(bool(self.start_print.is_pressed)):
    #         if(self.print_triggered):
    #             # If sound is on, speak
    #             if(bool(self.sound.is_pressed)):
    #                 self.engine.say("Printing")
    #                 self.engine.runAndWait()
    #             self.print_triggered = False
    #             print('[interface.py] ','print button pressed')
    #             return True
    #     else:
    #         self.print_triggered = True
    #         return False

        # return bool(self.start_print.is_pressed)


if __name__ == '__main__':
    import time
    interface = Interface(1)
    #TODO: Right now, the code is taking too long to respond to the below operators. Need to call
    #methods within the methods to make sure that they are called.
    while 1:
        if(interface.is_start_print()):
            print('[interface.py] ','Is start print %s' %interface.is_start_print())
        if(interface.is_sound()):
            print('[interface.py] ','Is sound %s' %interface.is_sound())
        if(interface.is_play()):
            print('[interface.py] ','Is play pause %s' %interface.is_play())
        if(interface.is_cancel()):
            print('[interface.py] ','Is cancel %s' %interface.is_cancel())
        #if interface.is_cancel() or interface.is_play_pause() or interface.is_start_print():

            #interface.signal_ready()
            #time.sleep(.5)
            #interface.resolve_ready()
            #time.sleep(.5)
            
            #interface.signal_error()
            #time.sleep(.5)
            #interface.resolve_error()
            #time.sleep(.5)

