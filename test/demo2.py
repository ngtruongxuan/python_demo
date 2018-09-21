import time
import os
from __builtin__ import round
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
def round(num):
    print num
    numTemp = int(num)
    print numTemp
    if num>numTemp:
        numTemp+=1
    return numTemp
if __name__ == '__main__':
#     count(10)
    print round(2.1)
    print('Finish')