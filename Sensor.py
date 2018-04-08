class Sensor:
    def __init__(self, io_handler, sensor_pin):
        io_handler.set_pin_as_input(sensor_pin)
