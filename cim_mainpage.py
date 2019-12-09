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
        self.top=NONE 
        self.item=NONE 
        self.searchitem()        
        self.sitem=0       
        self.user_input=None    
        self.createWidgets()
        self.addButton        
                
    #添加搜索对象的下拉选项框（Combobox）和输入框（Entry）
    def searchitem(self):
        #设置随主窗口尺寸改变，各插件跟随调整       
        self.top=self.winfo_toplevel()
        top=self.top
        top.rowconfigure(0,weight=5)
        top.rowconfigure(1,weight=1)
        top.rowconfigure(2,weight=14)
        top.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=5)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=14)
        self.columnconfigure(0,weight=1)
        #搜索对象的下拉选项框
        self.item=ttk.Combobox(self,values=('车牌号码','客户姓名','电话号码'),
        textvariable='车牌号码',exportselection=0,font=('宋体',12,'bold'),width=10) 
        self.item.current([1])
        self.item.grid(row=1,column=0,columnspan=3,padx=5,pady=5,sticky=NSEW)         
        #使用entry来添加用户输入框
        self.search_entry = tk.Entry(self, font=('宋体',12,'bold'),width=25)
        self.search_entry.grid(row=1,column=3,columnspan=5,pady=5,sticky=NSEW)
        
    #创建功能按钮（查询、添加）与显示模块treeview，并实现其功能
    def createWidgets(self):
        #添加标题
        self.lf=ttk.Label(self,text='平  安  汽  车  服  务  中  心',font=('华文行楷',20,'bold'),foreground='white',background='#407EC9')#,image=self.img,compound=tk.CENTER)
        self.lf.grid(row=0,column=0,columnspan=20,sticky=N)

        #添加'查询'和'添加'button
        tb=ttk.Style()
        tb.configure('TButton',font=('宋体',12,'bold'),foreground='#EA7600')
        self.searchButton = ttk.Button(self, text='查询',command=self.process_data,width=8,style='TButton')  #主页 查询 接口调用
        self.searchButton.grid(row=1,column=8,columnspan=2,pady=5,sticky=NSEW) 
        tb.configure('A.TButton',font=('宋体',12,'bold'),foreground='#0095C8')
        self.addButton=ttk.Button(self,text='添加',command=self.addButt,width=8,style='A.TButton')   #主页 添加 接口调用
        self.addButton.grid(row=1,column=10,columnspan=2,padx=5,pady=5,sticky=NSEW)
        
        #添加treeview模块，提供数据库查询结果的显示区域          
        self.tree=ttk.Treeview(show="headings",height=22)  #将第一列空列删除
        self.vbar=ttk.Scrollbar(orient=VERTICAL,command=self.tree.yview)  #添加竖直滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
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
        #tree区域的显示调节
        tree.grid(row=2,column=0,columnspan=20,sticky=NSEW)
        self.vbar.grid(row=2,column=1,sticky=NS)

    #对输入数据进行处理
    def process_data(self):
        #选定的输入项目
        sitem=self.item.get()
        if sitem=='车牌号码':
            sitem='carnumber'
        elif sitem=='客户姓名':
            sitem='name'
        else:
            sitem='tel'  
        self.sitem=sitem     
        #输入的内容
        self.user_input=self.search_entry.get()
        self.search_data()
    
    #实现数据库内的搜索功能，以及搜索结果的输出
    def search_data(self):
        sr=NONE
        #调用数据库的搜索功能
        print(self.sitem)
        print(self.user_input)
        database.search_data(self.sitem,self.user_input)
        sr=database.search_data(self.sitem,self.user_input)

        #根据数据库给出的搜索结果，来选择显示历史数据（treeview）；若没有历史数据，弹出'添加'提示框
        if sr:                  
            #若treeview中已有显示数据，则先删除，再导入新数据
            if self.tree.item:
                x=self.tree.get_children()                
                for item in x:
                    self.tree.delete(item)
            #按行插入新搜索得到的数据   
            for i in range(len(sr)):
                self.tree.insert("",i,values=(sr[i]))
            
            self.tree.grid() 
            #对于有历史记录的的用户，选择添加新数据时，自动填充用户基本信息
            l=len(sr)-1
            self.srinfo=[sr[l][0],sr[l][1],sr[l][2]]  #以最新的历史记录中的基本信息为准
            self.sr=sr  #用来判断是否有历史纪录的判决值
        else:
            answer=messagebox.askokcancel('提示','没有历史记录！是否需要新建记录？')
            #若选择确定天机，则调用新用户的添加数据函数
            if answer:
                self.add_record_new()
    
    #'添加'按钮的命令实现
    def addButt(self):
        if self.sr==0:  #无历史记录
            self.add_record_new()
        else:  #有历史记录
            self.add_record()
        self.sr=0 #重置判决值
      
    #对无历史数据的新用户，添加数据的实现
    def add_record_new(self):
        ar=popup_withouthistory.MyDialog(self.master,title='添加')
        self.wait_window(ar)  #等待窗口，等待popup中的窗口销毁之后把所输入的值传回来
        #在数据表中插入从popup窗口中输入的数据,并且根据数据库操作的结果提示用户数据插入操作是否成功
       
        #若弹窗中给出确定添加的命令，则在数据库中执行添加操作，否则不执行
        if ar.ju==1:   #在添加窗口点击添加
            if database.input_data(ar.mess):  
                success=messagebox.showinfo('提示','数据以成功保存！')
            else:
                failure=messagebox.showinfo('提示','数据保存失败！，请重新尝试。')
            #添加完毕后刷新列表
            if self.sitem=='carnumber':
                self.user_input=ar.mess[0]
            elif self.sitem=='name':
                self.user_input=ar.mess[1]
            elif self.sitem=='tel':
                self.user_input=ar.mess[2]
            self.search_data()
        else:   #在添加窗口点击取消
            self.sr=0  #返回到主页面，并在下次点击添加时，弹窗新用户添加窗口

    #对于有历史数据的用户，添加数据的实现      
    def add_record(self):
        ar=popup_withhistory.MyDialog(self.master,title='添加',info=self.srinfo)
        self.wait_window(ar)  #等待窗口，等待popup中的窗口销毁之后把所输入的值传回来
        #在数据表中插入从popup窗口中输入的数据,并且根据数据库操作的结果提示用户数据插入操作是否成功
        #若弹窗中给出确定添加的命令，则在数据库中执行添加操作，否则不执行
        if ar.ju==1:  #在添加窗口点击添加
            if database.input_data(ar.mess):  
                success=messagebox.showinfo('提示','数据以成功保存！')
            else:
                failure=messagebox.showinfo('提示','数据保存失败！，请重新尝试。')
            #添加完毕后刷新列表
            if self.sitem=='carnumber':
                self.user_input=ar.mess[0]
            elif self.sitem=='name':
                self.user_input=ar.mess[1]
            elif self.sitem=='tel':
                self.user_input=ar.mess[2]
            self.search_data()
        else:   #在添加窗口点击取消
            self.sr=0  #返回到主页面，并在下次点击添加时，弹窗新用户添加窗口
              
#实例app的运行                           
app = Application() 
app.master.title('客户服务信息记录系统') 
app.mainloop()
