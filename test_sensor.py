import unittest
from fake_io_handler import FakeIOHandler
from sensors import Sensor


class SensorTests(unittest.TestCase):
    _sensor_input_pin = 11

    def test_pin_set_as_input(self):
        io_handler = FakeIOHandler()
        Sensor(io_handler, self._sensor_input_pin)
        self.assertTrue(io_handler.is_input_pin(self._sensor_input_pin))

    def test_pin_level_is_high(self):
        io_handler = FakeIOHandler()
        sensor = Sensor(io_handler, self._sensor_input_pin)
        io_handler.simulate_input_pin_level_high(self._sensor_input_pin)
        self.assertTrue(sensor.is_pin_level_high())


if __name__ == '__main__':
    unittest.main()
