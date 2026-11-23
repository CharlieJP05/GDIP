from machine import PWM,Pin
pwm0 = PWM(Pin(16,Pin.OUT),freq=50,duty_u16=8192)
pwm1 = PWM(Pin(17,Pin.OUT),freq=50,duty_u16=8192)
pwm2 = PWM(Pin(18,Pin.OUT),freq=50,duty_u16=8192)
pwm3 = PWM(Pin(19,Pin.OUT),freq=50,duty_u16=8192)
pwm4 = PWM(Pin(20,Pin.OUT),freq=50,duty_u16=8192)
pwm5 = PWM(Pin(21,Pin.OUT),freq=50,duty_u16=8192)
pwms = [pwm0,pwm1,pwm2,pwm3,pwm4,pwm5]
def set_servo_duty(s,point):
    duty = int(point * (8192-1024) + 1024)
    pwms[s].duty_u16(duty)
    print(f"{s}: {duty}")
    # match MODE:
    #     case 0: # sim
    #         print(f"set Servo {s} to {pwm}% duty")
    #     case 1: # pca
    #         print("NI")
    #     case 2: # pins
    #         


