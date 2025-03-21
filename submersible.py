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

# Traverse to the mission
drive_base.settings(straight_speed=900)
drive_base.straight(200)
drive_base.turn(-30)
drive_base.straight(500)
drive_base.turn(-40)
drive_base.straight(400)
drive_base.turn(30)
drive_base.straight(100)

# Lift
left_motor.run(500)
right_motor.run(500)
wait(200)
left_motor.stop()
right_motor.stop()

wait(500)

left_motor.run(500)
right_motor.run(500)
wait(200)
left_motor.stop()
right_motor.stop()

drive_base.straight(15)

wait(500)

left_motor.run(500)
right_motor.run(500)
wait(200)
left_motor.stop()
right_motor.stop()

drive_base.straight(15)

wait(500)

left_motor.run(500)
right_motor.run(500)
wait(200)
left_motor.stop()
right_motor.stop()

drive_base.straight(10)

left_motor.run(500)
right_motor.run(500)
wait(200)
left_motor.stop()
right_motor.stop()


left_motor.run(500)
right_motor.run(500)
wait(200)
left_motor.stop()
right_motor.stop()

left_motor.run(500)
right_motor.run(500)
wait(200)
left_motor.stop()
right_motor.stop()

# Return to home B
drive_base.straight(-200)
drive_base.turn(-30)
drive_base.straight(-200)
drive_base.turn(30)
drive_base.straight(-600)


# # drive_base.straight(100)
# # left_motor.run(200)
# # wait(1000)



# left_motor.stop()