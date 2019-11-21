#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy
import database
#import popup_withouthistory


#主页面，初始页面； 有 搜索对象选择、搜索框、查询、添加 等插件
class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master) 
        self.grid() 
        self.searchitem()
        self.searchentry()
        self.createWidgets()
        self.data()
        self.item
        

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
        
    #创建功能按钮（查询、添加），并实现其功能
    def createWidgets(self):

        def search_data():
            #将输入框中产生的数据导出
            #选定的输入项目
            sitem=self.item.get()
            if sitem=='车牌号码':
                sitem='carnumber'
            elif sitem=='客户姓名':
                sitem='name'
            else:
                sitem='tel'       
            #输入内容
            user_input=self.search_entry.get()
            #调用数据库的搜索功能
            database.search_data(sitem,user_input)

        self.searchButton = ttk.Button(self, text='查询',command=search_data)  #主页 查询 接口调用
        self.searchButton.grid() 

        self.addButton=ttk.Button(self,text='添加',command=self.add_record)   #主页 添加 接口调用
        self.addButton.grid()


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
