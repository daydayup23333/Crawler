import pymysql
from tqdm import tqdm
from Thread.thread import  *
from bilibili_Crawler import crawbilibili


def main():
    Thread_list=[]
    max_threads=15
    for j in tqdm(range(1,200000)):
        while(len(Thread_list)>=max_threads):
            for i in Thread_list:
                if not i.is_alive():
                    Thread_list.remove(i)
        thread1=myThread(j,"Thread-"+str(j),j,crawbilibili,j)
        Thread_list.append(thread1)
        thread1.start()

if __name__=='__main__':
    main()