import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('时间到! 休息一下再开始新的倒计时吧.')

while True:
    # 番茄钟时间设为25分钟
    countdown(25 * 60)
    time.sleep(5)
