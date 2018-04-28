import unittest
from fake_io_handler import FakeIOHandler
from sensors import MotionSensor


class MotionSensorTests(unittest.TestCase):
    _sensor_input_pin = 11

    def test_no_motion_detected_by_default(self):
        self.assertFalse(MotionSensor(FakeIOHandler(), self._sensor_input_pin).is_motion_detected())

    def test_motion_detected_when_pin_level_high(self):
        fake_io_handler = FakeIOHandler()
        motion_sensor = MotionSensor(fake_io_handler, self._sensor_input_pin)
        fake_io_handler.simulate_input_pin_level_high(self._sensor_input_pin)
        self.assertTrue(motion_sensor.is_motion_detected())


if __name__ == '__main__':
    unittest.main()
