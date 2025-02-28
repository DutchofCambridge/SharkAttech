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

drive_base.settings(straight_speed=300)
drive_base.straight(40)
drive_base.turn(-30)
drive_base.straight(400)
drive_base.straight(-200)
drive_base.turn(20)
drive_base.settings(straight_speed=500)
drive_base.straight(300)
drive_base.straight(-200)
drive_base.settings(straight_speed=500)
drive_base.turn(-14)
drive_base.straight(330)
drive_base.straight(-150)
drive_base.straight(100)
drive_base.turn(20)
drive_base.straight(200)
drive_base.turn(20)
drive_base.straight(-200)
drive_base.turn(20)
drive_base.straight(180)
drive_base.straight(-200)
drive_base.turn(-40)
drive_base.straight(-200)
drive_base.turn(-30)
drive_base.straight(-400)








# UNKNOWN CODE from AVY
# drive_base.straight(400)
# drive_base.turn(25)
# drive_base.straight(440)
# drive_base.turn(46)
# drive_base.straight(240)
# drive_base.straight(-540)
# drive_base.turn(90)
# drive_base.straight(500)