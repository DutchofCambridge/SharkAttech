from pybricks.tools import hub_menu
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.tools import StopWatch




# Put your colors in a list or tuple.
my_colors = (Color.GREEN, Color.MAGENTA, Color.BROWN, Color.RED, Color.NONE)

DEBUG=True

if DEBUG:
    stopwatch = StopWatch()

# Initialize the sensor.
sensor = ColorSensor(Port.F)
# Save your colors.
sensor.detectable_colors(my_colors)

while True:
    # Read the color and reflection
    color = sensor.color()
    reflection = sensor.reflection()


    # Print the measured color and reflection.
    if DEBUG:
        print(color, reflection)

   
 

    if color == Color.NONE and reflection == 6:
        if DEBUG:
            print("None")
        pass
        # Color.MAGENTA and reflection > 30 and reflection < 40:
    elif color == Color.BLUE and reflection > 30 and reflection < 42:
        if DEBUG:
            print("feed_the_whale")
        import feed_the_whale
    elif color == Color.GREEN and reflection > 48 and reflection < 60:
        if DEBUG:
            print("submersible")
        import submersible
    elif color == Color.RED and reflection > 37 and reflection < 40:
        if DEBUG:
            print("change shipping lane")
        import change_ship_lane
        # color == Color.BROWN and reflection > 16 and reflection < 20:
    elif color == Color.GREEN and reflection > 16 and reflection < 20:
        if DEBUG:
            print("research vessel")
        import research_vessel
    elif color == Color.WHITE and reflection > 40 and reflection < 49:
        if DEBUG:
            print("kraken")
        import kraken
        # color == Color.RED and reflection > 72 and reflection < 78:
    elif color == Color.RED and reflection > 72 and reflection < 78:
        if DEBUG:
            print("sonar_discovery")
            start_time = stopwatch.time()
            print(start_time)
        import sonar_discovery
        if DEBUG:
            stop_time = stopwatch.time()
            print(stop_time)
            calc_time = stop_time - start_time
            print("sonar discovery took %s sec", calc_time/1000)
            # color == Color.GREEN and reflection > 98 and reflection < 103:
    elif color == Color.GREEN and reflection > 98 and reflection < 103:
        if DEBUG:
            print("collect_krills")
        import collect_krills
    # Move the sensor around and see how
    # well you can detect colors.

    # Wait so we can read the value.
    wait(1000)
