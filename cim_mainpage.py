#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy
#import database
#import popup_withouthistory
import pymysql


#主页面，初始页面； 有 搜索对象选择、搜索框、查询、添加 等插件
class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master) 
        self.grid() 
        self.searchitem()
        self.searchentry()
        self.createWidgets()
        self.data()
        #self.Searchachievement()
        self.item
        #self.sitem
        #self.user_input
        #self.search_data()
        


    #使用combobox来加入搜索对象的下拉选项框
    def searchitem(self):
        self.item=ttk.Combobox(self,values=('车牌号码','客户姓名','电话号码'),
        textvariable='车牌号码',exportselection=1) 
        self.item.current([0])
        self.item.grid(row=1,column=1)

        
        
        
        #print(sitem)
        #return sitem
        


        #使用entry来添加用户输入框
    def searchentry(self):
        self.search_entry = tk.Entry(self, font=16)
        self.search_entry.grid(row=1, column=2)
        
        
        
        #print(user_input)
        #return user_input
        

    def createWidgets(self):


        def search_data():
            #连接customer data 数据库
            cd=pymysql.connect(host="127.0.0.1",port=3306,user="CIM",password="pingan1234",db="customerdata") #,charset="utf-8"
            #创建游标
            cursor=cd.cursor()
            #查询语句

            #将输入框中产生的数据导出
            #选定的输入项目
            sitem=self.item.get()
            if sitem=='车牌号码':
                sitem='carnumber'
            elif sitem=='客户姓名':
                sitem='name'
            else:
                sitem='tel'
        
            #self.sitem=sitem


            #输入内容
            user_input=self.search_entry.get()


        
            sit=sitem
            sip=user_input
            print(sit)
            print(sip)
    
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
                    print("carnumber=%s,name=%s,tel=%s,time=%s,item=%s,cost=%s,note=%s"% \
                        (carnumber,name,tel,time,item,cost,note))
        
            except:
                print( "Error:unable to fetch data!")

            #关闭数据库连接
            cursor.close()
            cd.close()


        self.searchButton = ttk.Button(self, text='查询',command=search_data)  #主页 查询 接口调用
        self.searchButton.grid() 





        self.addButton=ttk.Button(self,text='添加',command=self.add_record)   #主页 添加 接口调用
        self.addButton.grid()




    '''
    def search_data(self):
        #连接customer data 数据库
        cd=pymysql.connect(host="127.0.0.1",port=3306,user="CIM",password="pingan1234",db="customerdata") #,charset="utf-8"
        #创建游标
        cursor=cd.cursor()
        #查询语句

        #将输入框中产生的数据导出
        #选定的输入项目
        sitem=self.item.get()
        if sitem=='车牌号码':
            sitem='carnumber'
        elif sitem=='客户姓名':
            sitem='name'
        else:
            sitem='tel'
        
        self.sitem=sitem


        #输入内容
        self.user_input=self.search_entry.get()


        
        sit=self.sitem
        sip=self.user_input
        print(sit)
        print(sip)
    
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
                print("carnumber=%s,name=%s,tel=%s,time=%s,item=%s,cost=%s,note=%s"% \
                    (carnumber,name,tel,time,item,cost,note))
        
        except:
            print( "Error:unable to fetch data!")

        #关闭数据库连接
        cursor.close()
        cd.close()

    '''









    '''
    #搜索功能的实现
    def Searchachievement(self):
        sit=self.sitem
        sip=self.user_input
        print(sit)
        print(sip)
        srch=database.search_data(self.sitem,self.user_input)
    '''


    #调用弹窗，添加数据
    def add_record(self):
        ar=popup_withouthistory.MyDialog(self.master,title='添加')


 
    #使用label，在其上输出从数据库来的数据
    def data(self):
        area=ttk.Label(self,background='green')
        area.text=self.createWidgets()
        area.grid()
   
       


app = Application() 
app.master.title('客户服务信息记录系统') 
app.mainloop()






'''
        #将输入框中产生的数据导出
        #选定的输入项目
        sitem=item.get()
        if sitem=='车牌号码':
            sitem='carnumber'
        elif sitem=='客户姓名':
            sitem='name'
        else:
            sitem='tel'
        
        #输入内容
        user_input=self.search_entry.get()
        
        #将数据通过返回值导出
        result=[sitem,user_input]
        print(result)
        return result
'''
