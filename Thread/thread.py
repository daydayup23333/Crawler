import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,Func,*numbers):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.Func=Func
        self.args=numbers
    def run(self):
        print ("开始线程：" + self.name)
        self.Func(self.args)
        #print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def test(*numbers):
    a=numbers[0][0]
    b=numbers[0][1]
    for i in range(a):
        print("name:",threading.current_thread().name)
        time.sleep(b)

if __name__=='__main__':
    # 创建新线程
    thread1 = myThread(2, "Thread-2", 2,test,5,1)

    # 开启新线程
    thread1.start()
    thread1.join()
    print("退出主线程")