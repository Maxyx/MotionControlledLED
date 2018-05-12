import unittest

from fake_io_handler import FakeIOHandler
from led import LED


class LEDTests(unittest.TestCase):
    _led_pin = 5

    def test_pin_assigned_to_LED_set_as_output(self):
        io_handler = FakeIOHandler()
        LED(io_handler, self._led_pin)
        self.assertTrue(io_handler.is_an_output_pin(self._led_pin))

    def test_pin_level_high_when_turning_led_on(self):
        io_handler = FakeIOHandler()
        LED(io_handler, self._led_pin).turn_on()
        self.assertTrue(io_handler.is_pin_level_high(self._led_pin))

    def test_pin_level_low_when_turning_led_off(self):
        io_handler = FakeIOHandler()
        led = LED(io_handler, self._led_pin)
        led.turn_on()
        self.assertTrue(io_handler.is_pin_level_high(self._led_pin))

        led.turn_off()
        self.assertFalse(io_handler.is_pin_level_high(self._led_pin))


if __name__ == '__main__':
    unittest.main()
