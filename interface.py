

class Interface:


    def __init__(self):
        from gpiozero import LED, Button

        self.error = LED(2)
        self.ready = LED(3)
        self.startPrint = Button(4)
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
        self.startPrint.wait_for_press()
    def is_sound(self):
        if self.sound.is_pressed:
            return True
        else:
            return False
    def is_cancel(self):
        if self.cancel.is_pressed:
            return True
        else:
            return False
    def is_play_pause(self):
        if self.play.is_pressed:
            return True
        else:
            return False





