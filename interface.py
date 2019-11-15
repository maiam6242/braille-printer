

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





