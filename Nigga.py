from machine import Pin,PWM
from utime import sleep
import time
trigger_pin = Pin(26, Pin.OUT)
echo_pin = Pin(27, Pin.IN)

PWM1 = 14
AIN2 = 15
AIN1 = 16
BIN1 = 17
BIN2 = 18
PWM2 = 19

def pwmWrite(pin,duty):
    pwm = PWM(Pin(pin))
    pwm.freq(1000)
    pwm.duty_u16(int(duty/1023*65535))

def fd():
    Pin(AIN1,Pin.OUT).value(1)
    Pin(AIN2,Pin.OUT).value(0)
    Pin(BIN1,Pin.OUT).value(0)
    Pin(BIN2,Pin.OUT).value(1)
    pwmWrite(PWM1,1023)
    pwmWrite(PWM2,1023)

def dick():
    Pin(AIN1,Pin.OUT).value(0)
    Pin(AIN2,Pin.OUT).value(1)
    Pin(BIN1,Pin.OUT).value(1)
    Pin(BIN2,Pin.OUT).value(0)
    pwmWrite(PWM1,1023)
    pwmWrite(PWM2,1023)

def stop():
    Pin(AIN1,Pin.OUT).value(0)
    Pin(AIN2,Pin.OUT).value(0)
    Pin(BIN1,Pin.OUT).value(0)
    Pin(BIN2,Pin.OUT).value(0)
    pwmWrite(PWM1,0)
    pwmWrite(PWM2,0)
def L():
    Pin(AIN1,Pin.OUT).value(0)
    Pin(AIN2,Pin.OUT).value(1)
    Pin(BIN1,Pin.OUT).value(0)
    Pin(BIN2,Pin.OUT).value(1)
    pwmWrite(PWM1,1023)
    pwmWrite(PWM2,1023)
# 
def R():
    Pin(AIN1,Pin.OUT).value(1)
    Pin(AIN2,Pin.OUT).value(0)
    Pin(BIN1,Pin.OUT).value(1)
    Pin(BIN2,Pin.OUT).value(0)
    pwmWrite(PWM1,1023)
    pwmWrite(PWM2,1023)
    
def measure_distance():
    trigger_pin.on()
    time.sleep_us(10)
    trigger_pin.off()


    while not echo_pin.value():
        pass
    start_time = time.ticks_us()


    while echo_pin.value():
        pass
    end_time = time.ticks_us()


    duration = time.ticks_diff(end_time, start_time)
    distance_cm = duration / 58

    return distance_cm

def ultrg():
    while int(measure_distance()) > 12:
        fd()
        sleep(0.05)

def dogL():
    Pin(AIN1,Pin.OUT).value(0)
    Pin(AIN2,Pin.OUT).value(1)
    Pin(BIN1,Pin.OUT).value(0)
    Pin(BIN2,Pin.OUT).value(1)
    pwmWrite(PWM1,350)
    pwmWrite(PWM2,950)
    sleep(0.45)
    stop()
    
def dogR():
    Pin(AIN1,Pin.OUT).value(1)
    Pin(AIN2,Pin.OUT).value(0)
    Pin(BIN1,Pin.OUT).value(1)
    Pin(BIN2,Pin.OUT).value(0)
    pwmWrite(PWM1,950)
    pwmWrite(PWM2,350)
    sleep(0.45)
    stop()

sleep(3)
ultrg()
sleep(0.1)
stop()
sleep(0.1)
dogL()
stop()
#sleep(0.1)
#fd()
ultrg()
sleep(0.1)
stop()
dogL()
stop()
ultrg()
sleep(0.1)
stop()
dogR()
stop()
sleep(0.1)
ultrg()
sleep(0.1)
stop()
dogR()
stop()
fd()
sleep(7)
stop()