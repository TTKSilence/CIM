#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

#创建数据库与创建数据表
def create_table():
    #连接customer data 数据库
    cd=pymysql.connect(host="127.0.0.1",port=3306,user="CIM",password="pingan1234")
    #创建游标
    cursor=cd.cursor()
    #使用execute()执行SQL
    try:
        cursor.execute("""CREATE DATABASE IF NOT EXISTS customerdata""" )
        print("success to build the connection!")
    except Exception as e:
        print("failed to build the connection!:%s"%e)
    finally:
        #关闭游标连接
        cursor.close()
        #关闭数据库连接
        cd.close()

    #连接customer data 数据库
    cd=pymysql.connect(host="127.0.0.1",port=3306,user="CIM",password="pingan1234",db="customerdata") 
    #创建游标
    cursor=cd.cursor()
    #使用execute()执行SQL
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS eins(
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
        #关闭游标连接
        cursor.close()
        #关闭数据库连接
        cd.close()


#输入数据
def input_data(mes):
    #连接customer data 数据库
    cd=pymysql.connect(host="127.0.0.1",port=3306,user="CIM",password="pingan1234",db="customerdata") 
    #创建游标
    cursor=cd.cursor()
    sql="INSERT INTO eins(carnumber,name,tel,time,item,cost,note) VALUES ('%s','%s','%s',NOW(),'%s','%s','%s')" % (mes[0],mes[1],mes[2],mes[3],mes[4],mes[5])    
    print('halfway')
    try:
        cursor.execute(sql) #执行所写的SQL语句
        print('almost')
        cd.commit()   #提交SQL语句，获得结果
        print('success')
        return 1
    except:
        cd.rollback()  #若发生错误，则回滚到此次操作之前的状态
        print('failure')
        return 0
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
    sql="SELECT * FROM EINS WHERE %s ='%s'" %(sit,sip)
    
    try:
        #执行SQL语句
        cursor.execute(sql)
        #获取所有符合条件的搜索记录
        results=cursor.fetchall()
        return results
        
    except:
        results= "Error:unable to fetch data!"
        return results

    #关闭数据库连接
    cursor.close()
    cd.close()

'''
def main():
    create_table()
    #input_data(mes)
    #search_data('name','平安')

if __name__=="__main__":
    main()
'''



