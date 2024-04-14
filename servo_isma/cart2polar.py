import time
import board
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import math

# Initialization of I2C and PCA9685
i2c = board.I2C()
pca = PCA9685(i2c)
pca.frequency = 50

# Servo configuration
servo7 = servo.Servo(pca.channels[1], min_pulse=550, max_pulse=2450)

# Inverse kinematics function to convert cartesian coordinates to angle
def cart2polar(x, y):
    r = math.hypot(x, y)
    if r == 0:
        return 0  # Returns 0 degrees if the vector is zero
    c = x / r
    s = y / r
    theta = math.acos(c) if s >= 0 else -math.acos(c)
    return math.degrees(theta)

# Example of desired position (x, y) -> (0, 1)
desired_x = -1
desired_y = 0

# Calculate the angle for the servo based on the coordinates
angle = cart2polar(desired_x, desired_y)
print(f'angulo es: {angle}º')

# Move the servo to the calculated angle
servo7.angle = angle
time.sleep(1)  # Wait one second to allow the servo to move

# Cleanup
pca.deinit()

