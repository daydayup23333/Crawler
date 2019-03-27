import pymysql
from DBUtils.PooledDB import PooledDB
from ext.dbconfig import mysqlInfo#数据库配置文件
class OPMysql(object):

    __pool = None

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.coon = OPMysql.getmysqlconn()
        self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)


    # 数据库连接池连接
    @staticmethod
    def getmysqlconn():
        if OPMysql.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20, host=mysqlInfo['host'], user=mysqlInfo['user'], passwd=mysqlInfo['passwd'], db=mysqlInfo['db'], port=mysqlInfo['port'], charset=mysqlInfo['charset'])
            #print(__pool)
        return __pool.connection()

    # 插入\更新\删除sql
    def op_insert(self, sql,userid,username,elec):
        #print('op_insert', sql,userid,username,elec)
        insert_num = self.cur.execute(sql,[userid,username,elec])
        #print('mysql sucess ', "userid:",userid, "username:",username,elec)
        self.coon.commit()
        return insert_num

    # 查询
    def op_select(self, sql):
        #print('op_select', sql)
        self.cur.execute(sql)  # 执行sql
        select_res = self.cur.fetchone()  # 返回结果为字典
        #print('op_select', select_res)
        return select_res

    #释放资源
    def dispose(self):
        self.coon.close()
        self.cur.close()


def Sql_insert(userid,username,elec):
    try:
        # 执行sql语句
        sql ='insert into bilibili_elec(userid,username,elec) values (%s, %s, %s)'
        opm = OPMysql()
        res = opm.op_insert(sql,userid,username,elec)
        opm.dispose()
    except:
        # 如果发生错误则回滚
        opm.dispose()

