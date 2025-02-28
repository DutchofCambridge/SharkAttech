from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


def left_motor_forward():
    left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    left_motor.run(100)
    wait(1800)
    left_motor.stop()
    left_motor.close()

    # left_motor.stop()

def left_motor_backward():
    left_motor = Motor(Port.B, Direction.CLOCKWISE)
    left_motor.run(100)
    wait(2000)
    left_motor.stop()



hub = PrimeHub()

left_motor_forward();

wait(1000)

left_motor_backward();

wait(1000)
