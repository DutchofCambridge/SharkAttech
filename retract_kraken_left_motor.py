from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


# Initialize the motor.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)


# Left motor retract
# # Choose the "power" level for your train. Negative means reverse.
left_motor.run(-200)
wait(1400)
left_motor.stop()