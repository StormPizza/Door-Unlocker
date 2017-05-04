import RPi.GPIO as GPIO
import time
import New_Read
last_open_time = time.time() - 25

GPIO.setmode(GPIO.BOARD)
#  Assign READY light   ////////////////////////////////
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, False)
# /////////////////////////////////////////
def move_to(out_num, set_value, wait_time):
        #for i in range(wait_time*interval):

        pi.set_servo_pulsewidth(out_num, set_value)
        time.sleep(wait_time)
        return

def jiggle(servo_num):
        move_to(servo_num, grip_mid+20, wait_period_jiggle)
        move_to(servo_num, grip_mid-20, wait_period_jiggle)
        move_to(servo_num, grip_mid, wait_period_jiggle)

def input_changed(input_state):
        global prev_state
        if input_state != prev_state:
                prev_state = input_state
                return True
        return False
#   ASSIGN SERVO TO 4 and 18  /////////////////////////////////////
took_pic = 0

import pigpio
pi = pigpio.pi()

pi.set_mode(4, pigpio.OUTPUT)
pi.set_mode(18, pigpio.OUTPUT)
# ////////////////////////////////////////////
grip_low = 580  # 530
grip_mid = 1360
grip_high = 2170  # 2200

arm_lo = 550
arm_hi = 1970

servo1 = 4  # Servo Arm
servo2 = 18   # Servo Twist
wait_period = 1.5  # 0.25
wait_period2 = wait_period * 2  # 0.5
wait_period_short = 1
wait_period_jiggle = 0.5

cool_down = wait_period * 20
# Starting State  ///////////////////////////
move_to(servo1, arm_lo, 0)
move_to(servo2, grip_mid, wait_period)
print("\n Beginning...")

# ////////////////////////////////////////////
def work_the_lock(target_status):
    move_to(servo1, arm_hi*0.95, wait_period)  # Arm - to lock
    move_to(servo1, arm_hi, wait_period)  # Arm - to lock
    jiggle(servo2)
    # if input_state is True:
    if target_status == "UNLOCK":
        print("Servo ON - Unlocking...")
        move_to(servo2, grip_high-400, wait_period_short) # Twist -Unlock
        move_to(servo2, grip_high, wait_period_short) # Twist -Unlock
    else:
        print("-------------Servo OFF - Locking...")
        move_to(servo2, grip_low+400, wait_period_short) # Twist -Lock
        move_to(servo2, grip_low, wait_period_short) # Twist -Lock
    move_to(servo1, arm_lo*0.90, wait_period_short)  # test
    move_to(servo1, arm_lo, wait_period)  # Arm - from lock
    jiggle(servo2)
    if target_status == "UNLOCK":
        print("Servo ON - DONE")
    else:
        print("-------------Servo OFF - DONE")
# ////////////////////////////////////////////
try:
    while True:
        if time.time() - last_open_time > cool_down:
            work_the_lock("LOCK")
            if New_Read.begin_read():
                work_the_lock("UNLOCK")
                last_open_time = time.time()

except KeyboardInterrupt:
    GPIO.cleanup()
    print ('program stopped')

