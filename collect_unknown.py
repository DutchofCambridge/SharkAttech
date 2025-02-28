# From avy

# unidentified program


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


# move the left motor to lift the red part
left_motor.run(200)
wait(5000)
left_motor.stop()


# # drive_base.settings(straight_speed=1000, straight_acceleration=570)
# drive_base.straight(370)
# drive_base.turn(-46)
# drive_base.straight(440)
# drive_base.straight(-170)
# drive_base.turn(-48)
# drive_base.straight(610)
# drive_base.turn(78)
# drive_base.straight(175)
# drive_base.curve(385,-59)
# drive_base.straight(415)
# drive_base.curve(385,-75)
# drive_base.straight(700)