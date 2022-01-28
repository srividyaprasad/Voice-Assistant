from tkinter import *
from tkinter import messagebox

def main():
     root = Tk() 
     root.title("CALCULATOR")

     e = Entry(root , width = 35, borderwidth = 5)
     e.grid(row = 0 , column = 0 , columnspan = 3 , padx = 10, pady = 10)

     def click(number):
          current = e.get()
          e.delete(0,END)
          e.insert(0, str(current) + str(number))

     def clear():
          e.delete(0,END)

     def add():
          try:
               f_n = e.get()
          except ValueError:
     
               window=Tk()
               window.eval('tk::PlaceWindow %s centre' % window.winfo_toplevel())
               window.withdraw()
               messagebox.showinfo('Enter Valid Number!') 
          global f_num
          global math
          math = "addition"
          f_num = int(f_n)
          e.delete(0,END)

     def sub():
          try:
               f_n = e.get()
          except ValueError:
     
               window=Tk()
               window.eval('tk::PlaceWindow %s centre' % window.winfo_toplevel())
               window.withdraw()
               messagebox.showinfo('Enter Valid Number!') 
          global f_num
          global math
          math = "subtraction"
          f_num = int(f_n)
          e.delete(0,END)

     def mul():
          try:
               f_n = e.get()
          except ValueError:
     
               window=Tk()
               window.eval('tk::PlaceWindow %s centre' % window.winfo_toplevel())
               window.withdraw()
               messagebox.showinfo('Enter Valid Number!') 
          global f_num
          global math
          math = "multiplication"
          f_num = int(f_n)
          e.delete(0,END)

     def div():
          try:
               f_n = e.get()
          except ValueError:
     
               window=Tk()
               window.eval('tk::PlaceWindow %s centre' % window.winfo_toplevel())
               window.withdraw()
               messagebox.showinfo('Enter Valid Number!') 
          global f_num
          global math
          math = "division"
          f_num = int(f_n)
          e.delete(0,END)
          
     def equal():
          try:
               s_num = int(e.get())
          except ValueError:
     
               window=Tk()
               window.eval('tk::PlaceWindow %s centre' % window.winfo_toplevel())
               window.withdraw()
               messagebox.showinfo('Enter Valid Number!') 

          e.delete(0, END)
          if math == "addition":
               e.insert(0 , f_num + s_num)
          elif math == "subtraction":
               e.insert(0 , f_num - s_num)
          elif math == "multiplication":
               e.insert(0 , f_num * s_num)
          elif math == "division":
               e.insert(0 , f_num / s_num)

     bt1 = Button(root, text = "1", padx = 20 , pady = 10, command = lambda : click(1))#callback
     bt2 = Button(root, text = "2", padx = 20 , pady = 10, command = lambda : click(2))#callback
     bt3 = Button(root, text = "3", padx = 20 , pady = 10, command = lambda : click(3))#callback
     bt4 = Button(root, text = "4", padx = 20 , pady = 10, command = lambda : click(4))#callback
     bt5 = Button(root, text = "5", padx = 20 , pady = 10, command = lambda : click(5))#callback
     bt6 = Button(root, text = "6", padx = 20 , pady = 10, command = lambda : click(6))#callback
     bt7 = Button(root, text = "7", padx = 20 , pady = 10, command = lambda : click(7))#callback
     bt8 = Button(root, text = "8", padx = 20 , pady = 10, command = lambda : click(8))#callback
     bt9 = Button(root, text = "9", padx = 20 , pady = 10, command = lambda : click(9))#callback
     bt0 = Button(root, text = "0", padx = 20 , pady = 10, command = lambda : click(0))#callback
     btadd = Button(root, text = "+", padx = 10 , pady = 10, command = add)#callback
     btsub = Button(root, text = "-", padx = 10 , pady = 10, command = sub)#callback
     btmul = Button(root, text = "*", padx = 10 , pady = 10, command = mul)#callback
     btdiv = Button(root, text = "/", padx = 10 , pady = 10, command = div)#callback

     btEquals = Button(root, text = "=", padx = 20 , pady = 10, command = equal)#callback
     btClear = Button(root, text = "C", padx = 20 , pady = 10, command = clear)#callback

     bt1.grid(row=1, column=0)
     bt2.grid(row=1, column=1)
     bt3.grid(row=1, column=2)

     bt4.grid(row=2, column=0)
     bt5.grid(row=2, column=1)
     bt6.grid(row=2, column=2)

     bt7.grid(row=3, column = 0)
     bt8.grid(row=3, column = 1)
     bt9.grid(row=3, column = 2)

     bt0.grid(row=4, column=1)
     btadd.grid(row=4, column=3)
     btEquals.grid(row=4, column=2)
     btClear.grid(row=4, column=0)
     btsub.grid(row=3, column=3)
     btmul.grid(row=2, column=3)
     btdiv.grid(row=1, column=3)
     root.mainloop()

main()