from tkinter import*
from tkinter import ttk
import csv


GUI = Tk()
GUI.title('Calculator')
GUI.geomatry('700*700')


F1 =Frame(GUI)
F1.place(x=70,y=40)


def Calculate(even=None):
    quntity=v_quntity.get()
    price=v_price.get()
    totlal



L=ttk.Label(F1,text='ปริมาณของเนื้อ')
v_quantity=StringVar()

E1=ttk.Entry(F1,textvariable=v_quantity)
E1.pack

L=ttk.Label(F1,text='ราคา')
v_price=StringVar

E2=ttk.Entry(F1,textvariable=v_price)
E2.pack()

B=ttk.Button(F1,text='คำนวณ',command)
B.pack(ipadx=50,ipady=20)


GUI.mainloop()
