def hallsensor(input) #read from sensor
power = 16 #GPIO pin

while True
    if input == GPIO.HIGH #if we get an 'on' reading
        GPIO.output(power,GPIO.HIGH) #takes power pin and sets on
    elif input == GPIO.LOW
        GPIO.output(power,GPIO.LOW) #takes power pin and sets off

