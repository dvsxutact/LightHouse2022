from machine import Pin, PWM
from time import sleep
from time import sleep_ms

ledPins = [0, 1, 2, 11, 12, 13, 14, 15]
currentPwmLevel = 1;

# Create a function to set our LED duty cycle (brightness)
# Parameters:
#            targetLed: this is the LED we want to set the brightness of
#            targetDuty: this is a value between 0 and 65535 to describe brightness
# Note: 0 is Off of Extremely dim, 65535 is full brightness.
def setLed_Duty(targetLed, targetDuty):
    targetLed.duty_u16(targetDuty)

## This just turns on all pins defined above
for ledPin in ledPins:
    led = PWM(Pin(ledPin))
    led.freq(1000)
    led.duty_u16(65000)
    
## This is the main worker code, it's commented
## while i work on the wiring
# while True:
#     # loop through all of our LED's
#     # While setting the brightness for the target
#     # we need to also degress brightness
#     # for the previous led
#     
#     for index, ledPin in enumerate(ledPins):
#         led = PWM(Pin(ledPin))
#         led.freq(1000)
#         
#         prevLed = PWM(Pin(ledPins[index-1]))
#         if index == 0:
#             prevLed = PWM(Pin(ledPins[7]))
#             print("using special index")
#         prevLed.freq(1000)
#         
#         maxVal = 65535
#             
#         for duty in range(0,65535):
#             prevLed.duty_u16(maxVal)            
#             led.duty_u16(duty)
#             
#             maxVal = maxVal - 1
#             sleep(0.0001)
            


