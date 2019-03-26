
from urllib import error
import urllib.request as urllib2
import re
from tqdm import tqdm
from test_sql import Sql_insert
from test_sql import *
import pymysql

row=0
#判空函数
def IsNone(S):
    if (len(S)):
        return False
    else:
        return True

#爬取充电人数和up主名字
def crawbilibili(*numbers):
    global row
    print('numbers',numbers[0][0])
    userid=numbers[0][0]
    cursor=numbers[0][1]
    db=numbers[0][2]
    url_elec = 'https://elec.bilibili.com/api/query.rank.do?mid=' + str(userid)
    url_name= 'https://space.bilibili.com/' + str(userid)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://space.bilibili.com/6758258/',
        'Origin': 'http://space.bilibili.com',
        'Host': 'space.bilibili.com',
        'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }
    try:
        #request = urllib2.Request(url,headers = headers)
        request_elec = urllib2.Request(url_elec)
        response_elec = urllib2.urlopen(request_elec)
        response_name = urllib2.urlopen(url_name)
        content_elec = response_elec.read().decode('utf-8')
        content_name = response_name.read().decode('UTF-8')
        pattern_elec = re.compile('"total_count":(.*?),"list"', re.S)
        items_elec = re.findall(pattern_elec,content_elec)
        if(IsNone(items_elec)):
            items_elec='0'
       # print(items_elec[0])
        pattern_name = re.compile('<title>(.*?)的个人空间 - 哔哩哔哩', re.S)
        items_name = re.findall(pattern_name, content_name)
        Sql_insert(cursor,db,userid,items_name[0],items_elec[0])

        #print(items_name[0])
        #sheet.write(row, 0, userid)
        #sheet.write(row, 1, items_name[0])
        #sheet.write(row, 2, items_elec[0])
        row+=1
        if(row%1000==0):
            #book.save('test.xls')
            print("save as ",row)
    except error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)


if __name__ == '__main__':

    db = pymysql.connect("118.25.176.50", "daydayup", "233333", "daydayup",charset="utf8")
    cursor = db.cursor()
    #book = xlwt.Workbook()  # 新建一个excel
    #sheet = book.add_sheet('case1_sheet')  # 添加一个sheet页
    for i in tqdm(range(1,400)):
        crawbilibili(i,cursor,db)
    db.close()
