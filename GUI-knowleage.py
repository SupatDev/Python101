from tkinter import *
from tkinter import ttk #them of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x700') #ขนาดโปรแกรม

#สร้างป้ายชื่อโปรแกรม
L1 = Label(GUI,text='โปรแกรมบันทึกแจ้งเตือนกิจกรรม',font=('AngsanaNew',20,'bold'),
           fg='#fffafa',bg='#2561d9', width=25, height=2)
L1.pack(pady=50)
#สร้างฟังก์ชั่นกำหนดคุณสมบัติของปุ่ม
def Button1(): #fuction1
    text = 'แพคของ','ขายของ'
    messagebox.showinfo('กิจกรรม',text)
    
FB1 = LabelFrame(GUI,text='1 สัปดาห์',font=('AngsanaNew',15)
      ,fg='#fffafa',bg='#597aff') #กระดาน
FB1.pack() #กำหนดตำแหน่ง
B1 = ttk.Button(FB1,text='วันจันทร์',command=Button1)
B1.pack(ipadx=10,ipady=10,padx=5,pady=10)
##########################

def Button2(): #fuction2
    text = 'เรียน Python'
    messagebox.showinfo('กิจกรรม',text)
B2 = ttk.Button(FB1,text='วันอังคาร',command=Button2)
B2.pack(ipadx=10,ipady=10,padx=5,pady=10)

def Button3(): #fuction3
    text = 'เรียน Html,CSS'
    messagebox.showinfo('กิจกรรม',text)
B2 = ttk.Button(FB1,text='วันพุธ',command=Button3)
B2.pack(ipadx=10,ipady=10,padx=5,pady=10)

def Button4(): #fuction4
    text = 'เรียน Python101'
    messagebox.showinfo('กิจกรรม',text)
B2 = ttk.Button(FB1,text='วันพฤหัสบดี',command=Button4)
B2.pack(ipadx=10,ipady=10,padx=5,pady=10)

def Button5(): #fuction5
    text = 'เรียนความรู้ทั่วไป'
    messagebox.showinfo('กิจกรรม',text)
B2 = ttk.Button(FB1,text='วันศุกร์',command=Button4)
B2.pack(ipadx=10,ipady=10,padx=5,pady=10)

def Button5(): #fuction6
    text = 'เรียนความรู้ทั่วไป'
    messagebox.showinfo('กิจกรรม',text)
B2 = ttk.Button(FB1,text='วันเสาร์',command=Button4)
B2.pack(ipadx=10,ipady=10,padx=5,pady=10)

def Button5(): #fuction7
    text = 'เรียนความรู้ทั่วไป'
    messagebox.showinfo('กิจกรรม',text)
B2 = ttk.Button(FB1,text='วันอาฑิตย์',command=Button4)
B2.pack(ipadx=10,ipady=10,padx=5,pady=10)



GUI.mainloop()
