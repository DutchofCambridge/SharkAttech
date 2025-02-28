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

# Initialize the motor.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.CLOCKWISE)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
# drive_base.use_gyro(True)

# move to mission postion
drive_base.straight(690)
drive_base.turn(43)
drive_base.straight(180)

# Release the krill to whale mouth
left_motor.run(-200)
wait(1800)
left_motor.stop()

# Return to home
drive_base.settings(straight_speed=500)
drive_base.straight(-180)
drive_base.turn(-43)
drive_base.straight(-690)
