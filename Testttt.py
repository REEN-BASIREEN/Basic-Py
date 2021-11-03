from tkinter import *
from tkinter import ttk

GUI = Tk() #Tk() คือหน้าจอหลักโปรแกรม
GUI.geometry('700x750')


def Save():
    print(B1)

ttk.Label(GUI,text='รายการ').pack()
v_expense=StringVar()

a=ttk.Entry(GUI)
a.pack()

B1=ttk.Button(GUI,text='Save',command=Save)
B1.pack()








GUI.mainloop()