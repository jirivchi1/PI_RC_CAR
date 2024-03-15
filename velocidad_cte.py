import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)

p.start(0)
print("Starting 0")
time.sleep(3)

# Establecer una velocidad constante del 6%
#p.ChangeDutyCycle(7.98)
#print("Speed set to 6%")

try:
    while True:

        i = 6.7
        print('atras')
        p.ChangeDutyCycle(6.7)
        time.sleep(5)

        p.start(0)
        print("Starting 0")
        time.sleep(3)
        
        p.ChangeDutyCycle(7.98)
        time.sleep(5)
        p.start(0)
        print("Starting 0")
        time.sleep(3)

        
        pass
except KeyboardInterrupt:
    # Detener la se�al PWM y limpiar los pines GPIO al presionar Ctrl+C
    p.stop()
    GPIO.cleanup()