import pwmio
import board
pwm0 = pwmio.PWMOut(board.GP27,frequency=50,duty_cycle=0)
def set_servo_duty(s,pwm):
    pwm0.duty_cycle = pwm
    print("did it")
    # match MODE:
    #     case 0: # sim
    #         print(f"set Servo {s} to {pwm}% duty")
    #     case 1: # pca
    #         print("NI")
    #     case 2: # pins
    #         