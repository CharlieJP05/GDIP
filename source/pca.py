from main import SIM
def set_servo_duty(s,pwm):
    if SIM:
        print(f"set Servo {s} to {pwm}% duty")
    elif PCA:
        print("NI")
    else:
        
