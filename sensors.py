class Sensor:
    def __init__(self, io_handler, sensor_pin):
        self._sensor_pin = sensor_pin
        self._io_handler = io_handler
        self._io_handler.set_pin_as_input(self._sensor_pin)

    def is_pin_level_high(self):
        return self._io_handler.is_pin_level_high(self._sensor_pin)


class MotionSensor(Sensor):
    def __init__(self, io_handler, sensor_pin):
        super().__init__(io_handler, sensor_pin)

    def is_motion_detected(self):
        return super().is_pin_level_high()
