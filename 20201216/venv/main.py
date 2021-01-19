from tkinter import *
from tkinter import messagebox


class zhuce(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text='用户名')
        self.label01.grid(row=0, column=0)

        v1 = StringVar()  # 用户名输入
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1, columnspan=2)

        self.label02 = Label(self, text='密码')
        self.label02.grid(row=1, column=0)

        v2 = StringVar()  # 密码输入
        self.entry02 = Entry(self, textvariable=v2, show='*')
        self.entry02.grid(row=1, column=1, columnspan=2)

        self.label03 = Label(self, text='确认密码')
        self.label03.grid(row=2, column=0)

        v2 = StringVar()  # 确认密码输入
        self.entry03 = Entry(self, textvariable=v2, show='*')
        self.entry03.grid(row=2, column=1, columnspan=2)

        Button(self, text='确定', command=self.login1) \
            .grid(row=3, column=1, padx=10, sticky=NSEW)
        Button(self, text='取消', command=self.cancel) \
            .grid(row=3, column=2, sticky=NSEW)

    def login1(self):
        pass

    def cancel(self):
        pass


class Applicantion(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text='用户名')
        self.label01.grid(row=0, column=0)

        v1 = StringVar()  # 用户名输入
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1,columnspan=2)

        self.label02 = Label(self, text='密码')
        self.label02.grid(row=1, column=0)

        v2 = StringVar()  # 密码输入
        self.entry02 = Entry(self, textvariable=v2, show='*')
        self.entry02.grid(row=1, column=1, columnspan=2)

        # 登录 注册 按钮事件绑定
        Button(self, text='登录', command=self.login)\
            .grid(row=2, column=1, padx=10, sticky=NSEW)
        Button(self, text='注册', command=self.set)\
            .grid(row=2, column=2, sticky=NSEW)

    def login(self):  # 登录事件
        username = self.entry01.get()
        pwd = self.entry02.get()

        if username == '123' and pwd == '123456':
            messagebox.showinfo('登录系统', '登录成功')
        else:
            messagebox.showinfo('登录系统', '登录失败，用户名或密码错误')

    def set(self):  # 注册事件
        root1 = Tk()
        root1.geometry('300x100+210+310')
        root1.title('注册系统')
        table = zhuce(master=root1)
        root1.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.geometry('300x100+200+300')
    root.title('用户登录系统')
    app = Applicantion(master=root)
    root.mainloop()