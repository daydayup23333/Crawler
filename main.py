import pymysql
from Thread.thread import  *
from bilibili_Crawler import crawbilibili

def main():
    db = pymysql.connect("118.25.176.50", "daydayup", "233333", "daydayup",charset="utf8")
    cursor = db.cursor()
    #book = xlwt.Workbook()  # 新建一个excel
    #sheet = book.add_sheet('case1_sheet')  # 添加一个sheet页
    for i in tqdm(range(1,400)):
        crawbilibili(i,cursor,db)
    db.close()

if __name__=='__main__':
    main()