class FakeIOHandler:
    def __init__(self):
        self._inputPins = []

    def set_pin_as_input(self, pin_index):
        self._inputPins.append(pin_index)

    def is_an_input_pin(self, pin_index):
        return pin_index in self._inputPins
