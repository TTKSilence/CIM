#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class MyDialog(Toplevel):
    # 定义构造方法
    def __init__(self, parent, title = None, modal=True):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        # 设置标题
        if title: self.title(title)
        self.parent = parent
        self.result = None
        # 创建对话框的主体内容
        frame = Frame(self)
        # 调用init_widgets方法来初始化对话框界面
        self.initial_focus = self.init_widgets(frame)
        frame.pack(padx=5, pady=5)
        # 调用init_buttons方法初始化对话框下方的按钮
        self.init_buttons()
        # 根据modal选项设置是否为模式对话框
        if modal: self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self
        # 为"WM_DELETE_WINDOW"协议使用self.cancel_click事件处理方法
        self.protocol("WM_DELETE_WINDOW", self.cancel_click)
        # 根据父窗口来设置对话框的位置
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
            parent.winfo_rooty()+50))
        print( self.initial_focus)
        # 让对话框获取焦点
        self.initial_focus.focus_set()
        self.wait_window(self)
    # 通过该方法来创建自定义对话框的内容
    def init_widgets(self, master):
        # 创建并添加Label
        Label(master, text='车牌号码', font=12,width=10).grid(row=1, column=0)
        # 创建并添加Entry,用于接受用户输入的用户名
        self.number_entry = Entry(master, font=16)
        self.number_entry.grid(row=1, column=1)
        # 创建并添加Label
        Label(master, text='客户姓名', font=12,width=10).grid(row=2, column=0)
        # 创建并添加Entry,用于接受用户输入的密码
        self.name_entry = Entry(master, font=16)
        self.name_entry.grid(row=2, column=1)
        # 创建并添加Label
        Label(master, text='电话号码', font=12,width=10).grid(row=3, column=0)
        # 创建并添加Entry,用于接受用户输入的密码
        self.phone_entry = Entry(master, font=16)
        self.phone_entry.grid(row=3, column=1)
        # 创建并添加Label
        Label(master, text='项    目', font=12,width=10).grid(row=4, column=0)
        # 创建并添加Entry,用于接受用户输入的密码
        self.item_entry = Entry(master, font=16)
        self.item_entry.grid(row=4, column=1)
                # 创建并添加Label
        Label(master, text='金    额', font=12,width=10).grid(row=5, column=0)
        # 创建并添加Entry,用于接受用户输入的密码
        self.cost_entry = Entry(master, font=16)
        self.cost_entry.grid(row=5, column=1)
                # 创建并添加Label
        Label(master, text='备    注', font=12,width=10).grid(row=6, column=0)
        # 创建并添加Entry,用于接受用户输入的密码
        self.note_entry = Entry(master, font=16)
        self.note_entry.grid(row=6, column=1)
        
    # 通过该方法来创建对话框下方的按钮框
    def init_buttons(self):
        f = Frame(self)
        # 创建"确定"按钮,位置绑定self.ok_click处理方法
        w = Button(f, text="添加", width=10, command=self.ok_click, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        # 创建"确定"按钮,位置绑定self.cancel_click处理方法
        w = Button(f, text="取消", width=10, command=self.cancel_click)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok_click)
        self.bind("<Escape>", self.cancel_click)
        f.pack()
    # 该方法可对用户输入的数据进行校验
    def validate(self):
        # 可重写该方法
        return True
    # 该方法可处理用户输入的数据
    def process_input(self):
        user_number=self.number_entry.get()
        user_name=self.name_entry.get()
        user_phone=self.phone_entry.get()
        user_item = self.item_entry.get()
        user_cost = self.cost_entry.get()
        user_note = self.note_entry.get()
        messagebox.showinfo(message='''
        车牌号码：%s
        客户姓名：%s
        电话号码：%s
        项       目: %s
        金       额: %s
        备       注: %s'''
            % (user_number,user_name,user_phone,user_item,user_cost,user_note))
    def ok_click(self, event=None):
        print('确定')
        # 如果不能通过校验，让用户重新输入
        if not self.validate():
            self.initial_focus.focus_set()
            return
        self.withdraw()
        self.update_idletasks()
        # 获取用户输入数据
        self.process_input()
        # 将焦点返回给父窗口
        self.parent.focus_set()
        # 销毁自己
        self.destroy()
    def cancel_click(self, event=None):
        print('取消')
        # 将焦点返回给父窗口
        self.parent.focus_set()
        # 销毁自己
        self.destroy()


'''
#测试工具代码
class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master) 
        self.grid() 
        self.createWidgets()
        #self.searchitem()
        #self.data()
        #self.popup()
        

    def createWidgets(self):  #插入按钮
        self.searchButton = ttk.Button(self, text='查询',command=self.quit)  #主页 查询 接口调用
        self.searchButton.grid() 

        self.addButton=ttk.Button(self,text='添加',command=self.add_record)   #主页 添加 接口调用
        self.addButton.grid()
    
    def add_record(self):
        ar=MyDialog(self.master,title='添加')   

app = Application() 
app.master.title('客户服务信息记录系统') 
app.mainloop()
'''