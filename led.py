class LED:
    def __init__(self, io_handler, led_pin):
        self._io_handler = io_handler
        self._led_pin = led_pin
        self._io_handler.set_pin_as_output(self._led_pin)

    def turn_on(self):
        self._io_handler.set_output_pin_level_to_high(self._led_pin)

    def turn_off(self):
        self._io_handler.set_output_pin_level_to_low(self._led_pin)