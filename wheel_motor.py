from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# https://docs.pybricks.com/en/stable/robotics.html


# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_wheel_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_wheel_motor = Motor(Port.A)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=56, axle_track=112)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
# drive_base.use_gyro(True)

# Drive forward by 500mm (half a meter).
drive_base.straight(200)

# Turn around clockwise by 180 degrees.
drive_base.turn(83)

# Drive forward again to get back to the start.
drive_base.straight(400)
#empty vessel
# drive_base.turn(-7)
#
drive_base.turn(-10)

drive_base.straight(780)

# Turn around counterclockwise.
# drive_base.turn(-180)