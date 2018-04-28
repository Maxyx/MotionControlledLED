class FakeIOHandler:
    def __init__(self):
        self._inputPins = []
        self._ouputPins = []
        self._pin_with_level_high = []

    def set_pin_as_input(self, pin_index):
        self._inputPins.append(pin_index)

    def is_an_input_pin(self, pin_index):
        return pin_index in self._inputPins

    def is_pin_level_high(self, pin_index):
        return pin_index in self._pin_with_level_high

    def set_pin_level_to_high(self, pin_index):
        self._pin_with_level_high.append(pin_index)

    def set_pin_as_output(self, pin_index):
        self._ouputPins.append(pin_index)

    def is_an_output_pin(self, pin_index):
        return pin_index in self._ouputPins
