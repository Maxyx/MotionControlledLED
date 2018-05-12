from led import LED
from pi_io_handler import PiIOHandler
from sensors import MotionSensor


motionSensorPin = 11
LEDPin = 12


def main():
    io_handler = PiIOHandler()
    motion_sensor = MotionSensor(io_handler, motionSensorPin)
    led = LED(io_handler, LEDPin)

    try:
        while True:
            if motion_sensor.is_motion_detected():
                led.turn_on()
            else:
                led.turn_off()
    except KeyboardInterrupt:
        pass
    finally:
        io_handler.clean_up()


if __name__ == '__main__':
    main()
