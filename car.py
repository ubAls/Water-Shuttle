from spike import PrimeHub, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
from hub import BT_VCP, button

hub=PrimeHub()
motor_a=Motor('A')
pair=MotorPair('C','D')
motor_d=Motor('D')
msgBox=BT_VCP(0)

while True:

   if msgBox.any() :
       msg = msgBox.readline()
       text = msg.decode()

       if text == '루트1':
           pair.move(20, 'cm', speed=30)
           wait_for_seconds(3)
           motor_d.run_for_degrees(-360)
           wait_for_seconds(3)
	   pair.move(10, 'cm', speed=30)
           motor_a.run_for_degrees(-90)
           wait_for_seconds(2)
           pair.move(-10, 'cm', speed=30)
	   motor_a.run_for_degrees(90)
           motor_d.run_for_degrees(360)
           wait_for_seconds(2)
           pair.move(-20, 'cm', speed=30)
           wait_for_seconds(2)


       if text == '루트2':
           pair.move(30, 'cm', speed=30)
           wait_for_seconds(3)
           motor_a.run_for_degrees(-90)
           wait_for_seconds(2)
           pair.move(30, 'cm', speed=30)	   motor_a.run_for_degrees(90)

       if text == '루트3':
           pair.move(20, 'cm', speed=30)
           wait_for_seconds(3)
           motor_d.run_for_degrees(360)
           wait_for_seconds(3)
           motor_a.run_for_degrees(-90)
           wait_for_seconds(2)
           motor_d.run_for_degrees(-360)
           pair.move(-20, 'cm', speed=30)
           wait_for_seconds(2)


       if text == '정지1' :
           pair.stop()

       if text == '정지2':
           pair.stop()

pair.stop()

