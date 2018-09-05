import time
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def count(t):
    end = ''
    t = 30
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        clear()
        print timeformat
        time.sleep(1)
        t -= 1

if __name__ == '__main__':
    count(10)
    print('Finish')