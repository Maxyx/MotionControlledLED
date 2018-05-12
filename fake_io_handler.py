from io_handler import IOHandler


class FakeIOHandler(IOHandler):
    def __init__(self):
        super().__init__()
        self._pin_with_level_high = []

    def is_pin_level_high(self, pin_index):
        return pin_index in self._pin_with_level_high

    def set_output_pin_level_to_high(self, pin_index):
        if self.is_output_pin(pin_index):
            self._pin_with_level_high.append(pin_index)
        else:
            raise ValueError

    def set_output_pin_level_to_low(self, pin_index):
        if self.is_output_pin(pin_index):
            self._pin_with_level_high.remove(pin_index)
        else:
            raise ValueError

    def simulate_input_pin_level_high(self, pin_index):
        if self.is_input_pin(pin_index):
            self._pin_with_level_high.append(pin_index)
        else:
            raise ValueError
