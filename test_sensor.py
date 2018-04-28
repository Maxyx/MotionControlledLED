import unittest

import FakeIOHandler
from Sensor import Sensor


class SensorTests(unittest.TestCase):
    def test_pin_set_as_input(self):
        sensor_input_pin = 11
        fake_io_handler = FakeIOHandler.FakeIOHandler()
        Sensor(fake_io_handler, sensor_input_pin)
        self.assertTrue(fake_io_handler.is_an_input_pin(sensor_input_pin))


if __name__ == '__main__':
    unittest.main()
