from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Motor

hub = PrimeHub()

# https://docs.pybricks.com/en/stable/pupdevices/motor.html

# Initialize the motor.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.CLOCKWISE)

# Choose the "power" level for your train. Negative means reverse.
left_motor.run(-200)
wait(500)
left_motor.stop()

right_motor.run(500)
wait(1000)
right_motor.stop()

