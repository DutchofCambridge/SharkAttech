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



# Drive forward and lift mast
drive_base.straight(300)
drive_base.turn(30)
drive_base.straight(290)
drive_base.turn(55)
#160
drive_base.straight(160)
drive_base.brake()
drive_base.straight(30)
drive_base.brake()


# move the left motor to lift the red part
left_motor.run(200)
wait(1500)
left_motor.stop()


# forward slightly
drive_base.straight(60)
drive_base.brake()
wait(500)


# # right motor to grab tresure
right_motor.run(200) 
wait(1500)
right_motor.stop()


# # pull and reverse
drive_base.straight(-10)
drive_base.brake()
drive_base.straight(-10)
drive_base.brake()
drive_base.straight(-200)
drive_base.turn(-60)
drive_base.straight(-500)
