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


# Drive forward 
drive_base.straight(300)
drive_base.turn(30)
drive_base.straight(300)
drive_base.turn(55)
drive_base.straight(150)

drive_base.brake()
wait(100)
drive_base.straight(30)
drive_base.brake()
wait(100)
drive_base.straight(10)
drive_base.brake()

# # # # # Choose the "power" level for your train. Negative means reverse.
# left_motor.run(200)
# wait(1800)
# left_motor.stop()

# # # Left motor retract
# # # # Choose the "power" level for your train. Negative means reverse.
# # left_motor.run(-200)
# # wait(1500)
# # left_motor.stop()

# forward
# drive_base.straight(30)
# drive_base.brake()
# drive_base.straight(40)
# drive_base.brake()


# right motor
# right_motor.run(200) 
# wait(1500)
# right_motor.stop()

# # right motor retract
# right_motor.run(-200)
# wait(1500)
# right_motor.stop()

# drive_base.straight(-10)
# drive_base.brake()
# drive_base.straight(-10)
# drive_base.brake()
# drive_base.straight(-100)

# drive_base.brake()
# wait(100)
# drive_base.straight(-20)
# drive_base.brake()
# wait(100)
# drive_base.straight(-20)



# drive_base.turn(-55)
# drive_base.straight(-230)
# drive_base.turn(-30)
# drive_base.straight(-350)
