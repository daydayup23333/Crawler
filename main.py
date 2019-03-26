import pymysql
from tqdm import tqdm
from Thread.thread import  *
from bilibili_Crawler import crawbilibili

def main():
    db = pymysql.connect("118.25.176.50", "daydayup", "233333", "daydayup",charset="utf8")
    cursor = db.cursor()
    #book = xlwt.Workbook()  # 新建一个excel
    #sheet = book.add_sheet('case1_sheet')  # 添加一个sheet页
    for i in tqdm(range(1,100)):
        thread1=myThread(i,"Thread-"+str(i),i,crawbilibili,i,cursor,db)
        #crawbilibili(i,cursor,db)
        thread1.start()
    db.close()

if __name__=='__main__':
    main()