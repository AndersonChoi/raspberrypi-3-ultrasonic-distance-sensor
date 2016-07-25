import RPi.GPIO as GPIO                    #Import GPIO library 기본라이브러리 입니다.
import time                                #Import time library 기본라이브러리 입니다.
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

TRIG = 23                                  #Associate pin 23 to TRIG 초음파센서
ECHO = 24                                  #Associate pin 24 to ECHO 초음파센서
LED = 25                                   #Associate pin 25 to LED LED센서를 밝히기 위한 포트

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)                 
GPIO.setup(ECHO,GPIO.IN)                   
GPIO.setup(LED,GPIO.OUT)                   #LED를 밝히기 위한 GPIO

while True:

  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  time.sleep(0.1)                            #0.1초마다 거리를 측정합니다.

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 2 and distance < 400:      #Check whether the distance is within range
    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
      if distance-0.5 < 10 :
        GPIO.output(LED,True)
      else
        GPIO.output(LED,False)
  else:
    print "Out Of Range"                   #display out of range
