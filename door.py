import RPi.GPIO as GPIO
import os, time

pin = 7

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def send_off_req(attempts = 0):
    if attempts > 5:
        return 

    if GPIO.input(pin):
        state = "true"
    else:
        state = "false"

    string = "curl --data-urlencode sensors='{\"state\":{\"open\":%(state)s}}' --data key=%(key)s https://spaceapi.net/new/space/cssa_common_room/sensor/set" % {"state": state, "key": os.environ['KEY']}
    print('running: ' + string)

    if os.system(string) == 0:
        print('done')
    else: # Keep on trying until it succeeds, or after 100 attempts
        attempts += 1
        time.sleep(5)
        send_off_req(attempts)



while True:
    GPIO.wait_for_edge(pin, GPIO.BOTH)
    print('I changed!')
    send_off_req()
    time.sleep(1) # to give the door time to settle
