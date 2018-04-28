import unittest
from fake_io_handler import FakeIOHandler
from sensors import Sensor


class SensorTests(unittest.TestCase):
    _sensor_input_pin = 11

    def test_pin_set_as_input(self):
        io_handler = FakeIOHandler()
        Sensor(io_handler, self._sensor_input_pin)
        self.assertTrue(io_handler.is_an_input_pin(self._sensor_input_pin))

    def test_pin_level_is_high(self):
        io_handler = FakeIOHandler()
        io_handler.set_pin_level_to_high(self._sensor_input_pin)
        self.assertTrue(Sensor(io_handler, self._sensor_input_pin).is_pin_level_high())


if __name__ == '__main__':
    unittest.main()
