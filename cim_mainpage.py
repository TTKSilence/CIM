#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy
import database
import popup_withouthistory


#主页面，初始页面； 有 搜索对象选择、搜索框、查询、添加 等插件
class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master) 
        self.grid() 
        self.searchitem()
        self.searchentry()
        self.createWidgets()
        self.item  
        
    #使用combobox来加入搜索对象的下拉选项框
    def searchitem(self):
        self.item=ttk.Combobox(self,values=('车牌号码','客户姓名','电话号码'),
        textvariable='车牌号码',exportselection=1) 
        self.item.current([0])
        self.item.grid(row=1,column=1)

    #使用entry来添加用户输入框
    def searchentry(self):
        self.search_entry = tk.Entry(self, font=16)
        self.search_entry.grid(row=1, column=2)
        
    #创建功能按钮（查询、添加），并实现其功能
    def createWidgets(self):   
        self.searchButton = ttk.Button(self, text='查询',command=self.search_data)  #主页 查询 接口调用
        self.searchButton.grid() 

        self.addButton=ttk.Button(self,text='添加',command=self.add_record)   #主页 添加 接口调用
        self.addButton.grid()
        
    #实现数据库内的搜索功能，以及搜索结果的输出
    def search_data(self):
        sr=NONE
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
        sr=database.search_data(sitem,user_input)        

        #添加treeview模块，提供数据库查询结果的显示区域
        tree=ttk.Treeview(show="headings")  #将第一列空列删除
        #创建表格的每一列，名称不显示
        tree["columns"]=("number","name","tel","time","item","cost","item")     
        tree.column("number",width=100)
        tree.column("name",width=100)
        tree.column("tel",width=100)
        tree.column("time",width=100)
        tree.column("item",width=100)
        tree.column("cost",width=100)
        tree.column("item",width=100)
        
        #绑定每一列的显示名称
        tree.heading("number",text="车牌号码")      
        tree.heading("name",text="客户姓名")
        tree.heading("tel",text="电话号码")
        tree.heading("time",text="时   间")
        tree.heading("item",text="项   目")
        tree.heading("cost",text="金   额")
        tree.heading("item",text="备   注")
        #将输出的results中的结果按行插入到显示区域的栏目中
        for i in range(len(sr)):
            tree.insert("",i,values=(sr[i]))

        tree.grid()

        #添加竖直滚动条，debug没问题，合理性/正确性待验证
        vbar=ttk.Scrollbar(orient=VERTICAL,command=tree.yview)
        tree.configure(yscrollcommand=tree.set)
        tree.grid(row=0,column=0,sticky=NSEW)
        vbar.grid(row=0,column=1,sticky=NS)          
    
    #调用弹窗，添加数据
    def add_record(self):
        ar=popup_withouthistory.MyDialog(self.master,title='添加')
        self.wait_window(ar)  #等待窗口，等待popup中的窗口销毁之后把所输入的值传回来
        #在数据表中插入从popup窗口中输入的数据,并且根据数据库操作的结果提示用户数据插入操作是否成功
        if database.input_data(ar.mess):  
            success=messagebox.showinfo('提示','数据以成功保存！')
        else:
            failure=messagebox.showinfo('提示','数据保存失败！，请尝试重新添加。')
        
    
       
app = Application() 
app.master.title('客户服务信息记录系统') 
app.mainloop()
