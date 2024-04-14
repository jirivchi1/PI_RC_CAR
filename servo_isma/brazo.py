import time
import board
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = board.I2C()  # uses board.SCL and board.SDA


pca = PCA9685(i2c)

pca.frequency = 50

servo7 = servo.Servo(pca.channels[1], min_pulse=550, max_pulse=2450)

# We sleep in the loops to give the servo time to move into position.
for i in range(180):
    servo7.angle = i
    time.sleep(0.05)
for i in range(180):
    servo7.angle = 180 - i
    time.sleep(0.05)

pca.deinit()

