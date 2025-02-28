from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Initialize the motor.
right_motor = Motor(Port.D, Direction.CLOCKWISE)


# right motor retract
right_motor.run(-200)
wait(1500)
right_motor.stop()