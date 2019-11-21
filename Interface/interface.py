"""Interface class for GPIO """

class Interface:
    """Creates interface to the raspi GPIO pins to control the buttons and leds of the UI"""
    def __init__(self):
        from gpiozero import LED, Button
        self.error = LED(2)
        self.ready = LED(3)
        self.start_print = Button(4)
        self.play = Button(14)
        self.cancel = Button(15)
        self.sound = Button(18)

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
        return bool(self.sound.is_pressed)
    def is_cancel(self):
        return bool(self.cancel.is_pressed)
    def is_play_pause(self):
        return bool(self.play.is_pressed)
    def is_start_print(self):
        return bool(self.start_print.is_pressed)


if __name__ == "__main__":
    import time
    interface = Interface()
    while 1:
        # print(interface.is_sound())
        if interface.is_cancel() or interface.is_play_pause() or interface.is_start_print():

            interface.signal_ready()
            time.sleep(.5)
            interface.resolve_ready()
            time.sleep(.5)

