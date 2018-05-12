class IOHandler:
    def __init__(self):
        self._inputPins = []
        self._outputPins = []

    def set_as_input(self, pin_index):
        self._inputPins.append(pin_index)
        if self.is_output_pin(pin_index):
            print("Changing pin from output to input")
            self._outputPins.remove(pin_index)

    def is_input_pin(self, pin_index):
        return pin_index in self._inputPins

    def set_as_output(self, pin_index):
        self._outputPins.append(pin_index)
        if self.is_input_pin(pin_index):
            print("Changing pin from input to output")
            self._inputPins.remove(pin_index)

    def is_output_pin(self, pin_index):
        return pin_index in self._outputPins
