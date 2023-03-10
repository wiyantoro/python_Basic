from tkinter import *


root= Tk()
root.title("simpel calculator")

e= Entry(root, width=35,bg="#d1d1d1", borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click (number):
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))
    
def button_clear():
    e.delete(0,END)
    
def button_add():
    frirst_number=e.get()
    global f_num
    f_num=int(frirst_number)
    e.delete(0,END)

def button_minus():
    first_number=e.get()
    global f_num
    global counting
    counting='minus'
    f_num=int(first_number)
    e.delete(0, END)


def pangkat():
    nomor_awal = e.get()
    global f_num
    global counting
    counting='pangkat'
    f_num = int(fist_number)
    e.delete(0,END)
    e.insert(0,n_awal **2)

def button_bagi():
    first_number=e.get()
    global f_num
    global counting
    counting='pembagian'
    f_num=int(first_number)
    e.delete(0, END)

def button_pangkat():
    first_number=e.get()
    global f_num
    global counting
    counting='2x'
    f_num=int(first_number)
    e.delete(0, END)
    e.insert(0,f_num **2)
   
def button_sisabagi():
    first_number=e.get()
    global f_num
    global counting
    counting ='sisabagi'
    f_num=int(first_number)
    e.delete(0, END)
    
def button_kali():
    first_number=e.get()
    global f_num
    global counting
    counting='kali'
    f_num=int(first_number)
    e.delete(0, END)
    
def button_equal():
    second_number=e.get()
    e.delete(0, END)
    if counting=='add':
        e.insert(0, f_num + int(second_number))
    else:
        if counting=='minus':
            e.insert(0, f_num - int(second_number))
        else:
                if counting=='kali':
                    e.insert(0, f_num * int(second_number))
                else:
                    if counting=='pembagian':
                        e.insert(0, f_num / int(second_number))
                    else:
                       if counting=='sisabagi':
                            e.insert(0, f_num % int(second_number))
                   
      
button_1= Button(root, text="1", padx=40, pady=20, bg='#00d4ff',command=lambda: button_click(1))
button_2= Button(root, text="2", padx=40, pady=20, bg='#00d4ff',command=lambda: button_click(2))
button_3= Button(root, text="3", padx=40, pady=20, bg='#00d4ff',command=lambda: button_click(3))
button_4= Button(root, text="4", padx=40, pady=20, bg='#00d4ff',command=lambda: button_click(4))
button_5= Button(root, text="5", padx=40, pady=20, bg='#00d4ff',command=lambda: button_click(5))
button_6= Button(root, text="6", padx=40, pady=20, bg='#00d4ff',command=lambda: button_click(6))
button_7= Button(root, text="7", padx=40, pady=20, bg='#00d4ff',command=lambda: button_click(7))
button_8= Button(root, text="8", padx=40, pady=20, bg='#00d4ff',command=lambda: button_click(8))
button_9= Button(root, text="9", padx=40, pady=20, bg='#00d4ff',command=lambda: button_click(9))
button_0= Button(root, text="0", padx=40, pady=20, bg='#00d4ff',command=lambda: button_click(0))
button_sisabagi=Button(root,text="%",padx=39,pady=20,bg="#ff0000",command=button_sisabagi)
button_pangkat=Button(root,text="x2",padx=39,pady=20,bg="#ff0000",command=button_pangkat)
button_pembagian=Button(root, text="/", padx=39, pady=20,bg='#ff0000', command=button_bagi)
button_kali=Button(root, text="*", padx=39, pady=20,bg='#ff0000', command=button_kali)
button_minus=Button(root, text="-", padx=39, pady=20,bg='#ff0000', command=button_minus)
button_add=Button(root, text="+", padx=39, pady=20, bg='#ff0000', command=button_add)
button_equal=Button(root, text="=", padx=91, pady=20, bg='#ffc400', command=button_equal)
button_clear=Button(root, text="c", padx=39, pady=20,bg='#ffc400', command=button_clear)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)
button_sisabagi.grid(row=5,column=0)
button_pangkat.grid(row=1,column=4)
button_pembagian.grid(row=5,column=1)
button_kali.grid(row=5,column=2)
button_add.grid(row=4,column=0)
button_minus.grid(row=4,column=2)
button_clear.grid(row=1, column=5)
button_equal.grid(row=2, column=4,columnspan=2)
root.mainloop()