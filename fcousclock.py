import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        time_left = end_time - time.time()
        mins, secs = divmod(time_left, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        print(timer, end="\r")
        time.sleep(1)
    print('Time is up! Take a break.')

# Example usage: focus for 25 minutes
focus_timer(25*60)
