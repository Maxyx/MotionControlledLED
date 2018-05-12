import RPi.GPIO as GPIO


class PiIOHandler:
    _HIGH = 1
    _LOW = 0

    def __init__(self):
        self._inputPins = []
        self._outputPins = []

        GPIO.setmode(GPIO.BOARD)

    def set_pin_as_input(self, pin_index):
        self._inputPins.append(pin_index)
        GPIO.setup(pin_index, GPIO.IN)

    def is_an_input_pin(self, pin_index):
        return pin_index in self._inputPins

    def is_pin_level_high(self, pin_index):
        if self.is_an_input_pin(pin_index):
            return GPIO.input(pin_index)
        else:
            raise ValueError

    def set_pin_as_output(self, pin_index):
        self._outputPins.append(pin_index)
        GPIO.setup(pin_index, GPIO.OUT)

    def is_an_output_pin(self, pin_index):
        return pin_index in self._outputPins

    def set_output_pin_level_to_high(self, pin_index):
        if self.is_an_output_pin(pin_index):
            GPIO.output(pin_index, self._HIGH)
        else:
            raise ValueError

    def set_output_pin_level_to_low(self, pin_index):
        if self.is_an_output_pin(pin_index):
            GPIO.output(pin_index, self._LOW)
        else:
            raise ValueError

    @staticmethod
    def clean_up():
        GPIO.cleanup()
