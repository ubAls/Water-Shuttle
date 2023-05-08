from spike import PrimeHub, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
motor_a = Motor('A')
motor_c = Motor('C')

while True:
   motor_c.run_for_degrees(40, 10)
   wait_for_seconds(1)
   motor_c.run_for_degrees(-40, 10)
   wait_for_seconds(1)
   motor_c.run_for_degrees(-100, 10)
   wait_for_seconds(1)
   motor_a.run_for_degrees(100, 10)
   wait_for_seconds(1)
   motor_c.run_for_degrees(40, 10)
