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


# get into postion
drive_base.settings(straight_speed=300)
drive_base.straight(200)
drive_base.turn(-30)
drive_base.straight(450)
drive_base.turn(30)
drive_base.straight(225)
drive_base.turn(-20)
drive_base.settings(straight_speed=80)


# sonar1
drive_base.turn(-25)
# drive_base.brake()
drive_base.settings(straight_speed=80)
drive_base.straight(-50)
drive_base.turn(-10)
drive_base.straight(-10)
drive_base.turn(-15)
drive_base.brake()
drive_base.straight(40)

# get into position for sonar2
drive_base.straight(-50)
drive_base.turn(-30)
drive_base.settings(straight_speed=200)
drive_base.straight(500)
drive_base.turn(150)
drive_base.straight(150)
drive_base.settings(straight_speed=80)


# sonar2
drive_base.turn(-25)
drive_base.straight(-10)
drive_base.turn(-10)
drive_base.straight(20)
drive_base.turn(-10)
drive_base.straight(20)
# turn and return to home B

drive_base.settings(straight_speed=300)
# drive_base.turn(-35)
drive_base.turn(-50)
drive_base.straight(-800)










