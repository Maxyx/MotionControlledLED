class Sensor:
    def __init__(self, io_handler, sensor_pin):
        self.sensor_pin = sensor_pin
        self.io_handler = io_handler
        self.io_handler.set_pin_as_input(self.sensor_pin)

    def is_pin_level_high(self):
        return self.io_handler.is_pin_level_high(self.sensor_pin)
