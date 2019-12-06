#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy
import database
import popup_withouthistory
import popup_withhistory


#主页面，初始页面； 有 搜索对象选择、搜索框、查询、添加 等插件
class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master) 
        self.grid()
        self.srinfo=[]
        self.sr=0         
        self.createWidgets()
        self.addButton
        self.searchitem()
        self.searchentry()
        self.item
         
        
        
    #使用combobox来加入搜索对象的下拉选项框
    def searchitem(self):
        self.item=ttk.Combobox(self,values=('车牌号码','客户姓名','电话号码'),
        textvariable='车牌号码',exportselection=1,font=14,width=10) 
        self.item.current([0])
        self.item.grid(row=5,rowspan=5,column=1,columnspan=4,padx=5,pady=30,sticky=tk.E)

    #使用entry来添加用户输入框
    def searchentry(self):
        self.search_entry = tk.Entry(self, font=16)
        self.search_entry.grid(row=5,rowspan=3,column=6,columnspan=3,pady=30,sticky=tk.W)
        
    #创建功能按钮（查询、添加）与显示模块treeview，并实现其功能
    def createWidgets(self):   
        self.searchButton = ttk.Button(self, text='查询',command=self.search_data)  #主页 查询 接口调用
        self.searchButton.grid(row=5,column=10,padx=10,pady=30) 

        self.addButton=ttk.Button(self,text='添加',command=self.addButt)   #主页 添加 接口调用
        self.addButton.grid(row=5,column=15,padx=5,pady=30)

        #添加treeview模块，提供数据库查询结果的显示区域          
        self.tree=ttk.Treeview(show="headings")  #将第一列空列删除
        tree=self.tree
        #创建表格的每一列，名称不显示
        tree["columns"]=("number","name","tel","time","item","cost","note")     
        tree.column("number",width=100)
        tree.column("name",width=100)
        tree.column("tel",width=100)
        tree.column("time",width=100)
        tree.column("item",width=100)
        tree.column("cost",width=100)
        tree.column("note",width=100)            
        #绑定每一列的显示名称
        tree.heading("number",text="车牌号码")      
        tree.heading("name",text="客户姓名")
        tree.heading("tel",text="电话号码")
        tree.heading("time",text="时   间")
        tree.heading("item",text="项   目")   
        tree.heading("cost",text="金   额")
        tree.heading("note",text="备   注")

        '''
        #添加竖直滚动条，debug没问题，合理性/正确性待验证
        vbar=ttk.Scrollbar(orient=VERTICAL,command=tree.yview)
        tree.configure(yscrollcommand=tree.set)
        tree.grid(row=0,column=0,sticky=NSEW)
        vbar.grid(row=0,column=1,sticky=NS) 
        '''   
        #tree区域的显示调节
        tree.grid(row=10,column=0,columnspan=20,sticky=tk.SW)

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

        #根据数据库给出的搜索结果，来选择显示历史数据；还是没有历史数据，然后给出添加选项
        if sr:           
            #将输出的results中的结果按行插入到显示区域的栏目中
            #若treeview中已有显示数据，则先删除，再导入新数据
            if self.tree.item:
                x=self.tree.get_children()
                for item in x:
                    self.tree.delete(item)
            for i in range(len(sr)):
                self.tree.insert("",i,values=(sr[i]))
            self.tree.grid() 
            l=len(sr)-1
            self.srinfo=[sr[l][0],sr[l][1],sr[l][2]]  #在添加的时候，自动填充当前用户的基本信息
            self.sr=sr  #用来判断是否有历史纪录的判决值
        else:
            answer=messagebox.askokcancel('提示','没有历史记录！是否需要新建记录？')
            if answer:
                self.add_record_new()

    def addButt(self):
        if self.sr==0:
            self.add_record_new()
        else:
            self.add_record()
        self.sr=0
      
    #调用弹窗，添加数据
    def add_record_new(self):
        ar=popup_withouthistory.MyDialog(self.master,title='添加')
        self.wait_window(ar)  #等待窗口，等待popup中的窗口销毁之后把所输入的值传回来
        #在数据表中插入从popup窗口中输入的数据,并且根据数据库操作的结果提示用户数据插入操作是否成功
       
        #若弹窗中给出确定添加的命令，则在数据库中执行添加操作，否则不执行
        if ar.ju==1:
            if database.input_data(ar.mess):  
                success=messagebox.showinfo('提示','数据以成功保存！')
            else:
                failure=messagebox.showinfo('提示','数据保存失败！，请重新尝试。')
        self.search_data()
        
    def add_record(self):
        ar=popup_withhistory.MyDialog(self.master,title='添加',info=self.srinfo)
        self.wait_window(ar)  #等待窗口，等待popup中的窗口销毁之后把所输入的值传回来
        #在数据表中插入从popup窗口中输入的数据,并且根据数据库操作的结果提示用户数据插入操作是否成功
        #若弹窗中给出确定添加的命令，则在数据库中执行添加操作，否则不执行
        if ar.ju==1:
            if database.input_data(ar.mess):  
                success=messagebox.showinfo('提示','数据以成功保存！')
            else:
                failure=messagebox.showinfo('提示','数据保存失败！，请重新尝试。')
        self.search_data()
                      
       
app = Application() 
app.master.title('客户服务信息记录系统') 
app.mainloop()
