import unittest
from io_handler import IOHandler


class IOHandlerTests(unittest.TestCase):
    def test_set_pin_as_input(self):
        input_pin = 6
        io_handler = IOHandler()
        io_handler.set_as_input(input_pin)
        self.check_pin_is_input(io_handler, input_pin)

    def test_set_pin_as_output(self):
        output_pin = 15
        io_handler = IOHandler()
        io_handler.set_as_output(output_pin)
        self.check_pin_is_output(io_handler, output_pin)

    def test_pin_can_change_between_input_and_output(self):
        pin = 8
        io_handler = IOHandler()
        io_handler.set_as_input(pin)
        self.check_pin_is_input(io_handler, pin)

        io_handler.set_as_output(pin)
        self.check_pin_is_output(io_handler, pin)

        io_handler.set_as_input(pin)
        self.check_pin_is_input(io_handler, pin)

    def check_pin_is_input(self, io_handler, pin):
        self.assertTrue(io_handler.is_input_pin(pin))
        self.assertFalse(io_handler.is_output_pin(pin))

    def check_pin_is_output(self, io_handler, pin):
        self.assertFalse(io_handler.is_input_pin(pin))
        self.assertTrue(io_handler.is_output_pin(pin))


if __name__ == '__main__':
    unittest.main()
