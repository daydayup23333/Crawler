
def Sql_insert(cursor,db,a,b,c):
    try:
        # 执行sql语句
        sql ='insert into bilibili_elec(userid,username,elec) values (%s, %s, %s)'
    #cursor.execute("insert into bilibili_elec (id, name) values (%s, %s)', [a,b,c]")
        cursor.execute(sql,[a,b,c])
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

