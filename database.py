#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
#import cim_mainpage

#创建数据库

'''
#连接数据库与创建数据表
def create_table():
    #连接customer data 数据库
    cd=pymysql.connect(host="127.0.0.1",port=3306,user="CIM",password="pingan1234",db="customerdata") #,charset="utf-8"
    #创建游标
    cursor=cd.cursor()
    #cursor.execute("DROP TABLE IF EXISTS eins")
    #使用execute()执行SQL
    try:
        cursor.execute("""CREATE TABLE eins(
            carnumber char(20),
            name char(20),
            tel char(20),
            time DATE,
            item char(20),
            cost char(20),
            note char(20))""")

        print("success to build the connection!")
    except Exception as e:
        print("failed to build the connection!:%s"%e)
    finally:
        #cursor.execute("SHOW DATABASES")
        #for x in cursor:
        #   print(x)
        #关闭游标连接
        cursor.close()
        #关闭数据库连接
        cd.close()
'''

#输入数据
def input_data():
    #连接customer data 数据库
    cd=pymysql.connect(host="127.0.0.1",port=3306,user="CIM",password="pingan1234",db="customerdata") #,charset="utf-8"
    #创建游标
    cursor=cd.cursor()
    #sql="INSERT INTO eins(carnumber,name,tel,time,item,cost,note) VALUES ('%s','%s','%s',NOW(),'%s','%s','%s')" 
    #data=('皖ADH985','平安','12345678901','日常保养','300','无')

    sql="INSERT INTO eins(carnumber,name,tel,time,item,cost,note) VALUES('皖ADH985','平安','12345678901',NOW(),'日常保养','300','无')"
    
    print('halfway')
    try:
        cursor.execute(sql)
        print('almost')
        cd.commit()
        print('success')
    except:
        cd.rollback()
        print('failure')
    #关闭连接
    cursor.close()
    cd.close()



#查询数据
def search_data(sit,sip):
    #连接customer data 数据库
    cd=pymysql.connect(host="127.0.0.1",port=3306,user="CIM",password="pingan1234",db="customerdata") #,charset="utf-8"
    #创建游标
    cursor=cd.cursor()
    #查询语句
    #sit='name'
    #sip='平安'
    sql="SELECT * FROM EINS WHERE %s ='%s'" %(sit,sip)
    
    try:
        #执行SQL语句
        cursor.execute(sql)
        #获取所有符合条件的搜索记录
        results=cursor.fetchall()
        #return results
        
        for row in results:
            carnumber=row[0]
            name=row[1]
            tel=row[2]
            time=row[3]
            item=row[4]
            cost=row[5]
            note=row[6]
            #打印结果
            results= "carnumber=%s,name=%s,tel=%s,time=%s,item=%s,cost=%s,note=%s"% \
                (carnumber,name,tel,time,item,cost,note)
            return results
        
    except:
        results= "Error:unable to fetch data!"
        return results

    #关闭数据库连接
    cursor.close()
    cd.close()



'''
def main():
    #create_table()
    #input_data()
    search_data()

if __name__=="__main__":
    main()

'''


