from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.3
left_wheel_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_wheel_motor = Motor(Port.A)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=56, axle_track=112)

# Initialize the motor.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.CLOCKWISE)

# change
def rotate_right_motor():
    right_motor.run(350)
    wait(1900)
    right_motor.stop()


# Traverse to the mission shipping lane and position itself
drive_base.straight(530)
drive_base.turn(-50)
drive_base.straight(-220)
drive_base.turn(10)

# rotate motor to change shipping lane
rotate_right_motor()

drive_base.straight(-200)





