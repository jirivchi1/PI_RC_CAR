from gpiozero import Servo

from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(5, min_pulse_width = 1/1000, max_pulse_width=1.5/1000, pin_factory = factory)

print('Empieza en el medio')
servo.mid()
sleep(5)
print('va al minimo')
servo.min()
sleep(5)
print('va al maximo')
servo.max()
sleep(5)
print('vuelve al medio')
servo.mid()
sleep(5)
servo.value = None;