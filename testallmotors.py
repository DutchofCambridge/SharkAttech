from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the hub
hub = PrimeHub()

# Initialize drive motors
left_wheel_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_wheel_motor = Motor(Port.F)

# Initialize the drive base with wheel diameter (56mm) and axle track (112mm)
drive_base = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=56, axle_track=106)

# Set drive base speed
drive_base.settings(200, 200)  # Speed: 200 mm/s, Acceleration: 200 mm/s²

# Initialize attachment motors
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)

# Drive forward for 5 seconds (200 mm/s * 5s = 1000 mm)
drive_base.straight(1000)

# Drive backward for 5 seconds (200 mm/s * 5s = 1000 mm)
drive_base.straight(-1000)

# Drive forward for 5 seconds
drive_base.straight(1000)

# Turn 180 degrees
drive_base.turn(180)

# Drive forward for 5 seconds
drive_base.straight(1000)

# Pause for 2 seconds
wait(2000)

# Turn left attachment motor clockwise for 10 seconds
left_motor.run(500)  # Speed in deg/sec
wait(10000)
left_motor.stop()

# Pause for 2 seconds
wait(2000)

# Turn left attachment motor counterclockwise for 10 seconds
left_motor.run(-500)
wait(10000)
left_motor.stop()

# Pause for 2 seconds
wait(2000)

# Turn right attachment motor clockwise for 10 seconds
right_motor.run(500)
wait(10000)
right_motor.stop()

# Pause for 2 seconds
wait(2000)

# Turn right attachment motor counterclockwise for 10 seconds
right_motor.run(-500)
wait(10000)
right_motor.stop()

# Pause for 2 seconds
wait(2000)