"""Interface class for GPIO """

class Interface:
    """Creates interface to the raspi GPIO pins to control the buttons and leds of the UI"""
    def __init__(self):
        from gpiozero import LED, Button
        self.error = LED(20) #checked
        self.ready = LED(16) #checked
        self.start_print = Button(6) #checked
        self.play = Button(13) #checked
        self.cancel = Button(26) #checked
        self.sound = Button(19) #checked

    def signal_error(self):
        self.error.on()
    def resolve_error(self):
        self.error.off()
    def signal_ready(self):
        self.ready.on()
    def resolve_ready(self):
        self.ready.off()
    def wait_for_play(self):
        self.play.wait_for_press()
    def wait_for_print(self):
        self.start_print.wait_for_press()
    def is_sound(self):
        print('Start Print is True')
        return bool(self.sound.is_pressed)
    def is_cancel(self):
        print('Cancel is True')
        return bool(self.cancel.is_pressed)
    def is_play_pause(self):
        print('Play Pause is True')
        return bool(self.play.is_pressed)
    def is_start_print(self):
        print('Start Print is True')
        return bool(self.start_print.is_pressed)


# if __name__ == "__main__":
#     import time
#     interface = Interface()
#     while 1:
#         if(interface.is_start_print()):
#             print('Is start print %s' %interface.is_start_print())
#         if(interface.is_sound()):
#             print('Is sound %s' %interface.is_sound())
#         if(interface.is_play_pause()):
#             print('Is play pause %s' %interface.is_play_pause())
#         if(interface.is_cancel()):
#             print('Is cancel %s' %interface.is_cancel())
#         if interface.is_cancel() or interface.is_play_pause() or interface.is_start_print():

#             interface.signal_ready()
#             time.sleep(.5)
#             interface.resolve_ready()
#             time.sleep(.5)
            
#             interface.signal_error()
#             time.sleep(.5)
#             interface.resolve_error()
#             time.sleep(.5)

