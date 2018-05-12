import RPi.GPIO as GPIO
from io_handler import IOHandler


class PiIOHandler(IOHandler):
    def __init__(self):
        super().__init__()
        GPIO.setmode(GPIO.BOARD)

    def set_as_input(self, pin_index):
        super().set_as_input(pin_index)
        GPIO.setup(pin_index, GPIO.IN)

    def is_pin_level_high(self, pin_index):
        if self.is_input_pin(pin_index):
            return GPIO.input(pin_index)
        else:
            raise ValueError

    def set_as_output(self, pin_index):
        super().set_as_output(pin_index)
        GPIO.setup(pin_index, GPIO.OUT)

    def set_output_pin_level_to_high(self, pin_index):
        if self.is_output_pin(pin_index):
            GPIO.output(pin_index, GPIO.HIGH)
        else:
            raise ValueError

    def set_output_pin_level_to_low(self, pin_index):
        if self.is_output_pin(pin_index):
            GPIO.output(pin_index, GPIO.LOW)
        else:
            raise ValueError

    @staticmethod
    def clean_up():
        GPIO.cleanup()
