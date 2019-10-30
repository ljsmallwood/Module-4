import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) #ignore warning for now
GPIO.setmode(GPIO.BOARD) #use physical pin for numbering

TRIG = 13 #define i/o pins
ECHO = 22

#set up the i/o pins
GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,False)
GPIO.setup(ECHO,GPIO.IN)

time.sleep(0.5) #let sensor initialize

def movingAverage(IN,n):
sum = 0:

#FIND TIME FUNCTION TO SET 1-SEC INTERVALS
for i = 1,5 #number of 10-sec loops
    while time<=10 #10 sec loop
        for j=0,3 #3-pt moving avg
            sum = sum + IN[j]
        result sum/n

        #trigger a reading
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)

        #find start and end of ultrasonic pulse
        while GPIO.input(ECHO) == 0:
            start_time = time.time()
        while GPIO.input(ECHO) == 1:
            end_time = time.time()

        #speed of sound 34300 cm/sec
        total_distance = (end_time - start_time) * 34300
        #divide by 2, acct for return trip for sig
        distance = round(total_distance/2,1)
        print ("Distance Away:",distance, "cm")

GPIO.cleanup() #reset the GPIO
