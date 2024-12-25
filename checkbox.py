from tkinter import *
window = Tk()
def display():
    if (x.get()==1):
        print("I like Python")
    if (x.get()==0):
        print("I don't like Python")
x= IntVar()
checkbox = Checkbutton(window,text='Python',variable=x,onvalue=1,offvalue=0,command=display)
checkbox.pack()
checkbox.config(font=('Arial'))
checkbox.config(fg='#0000FF')
checkbox.config(bg='#000000')
photo = PhotoImage(file='python_logo.png')
checkbox.config(image=photo,compound=RIGHT)
checkbox.config(padx=25,pady=10)
checkbox.config(anchor='w')

checkbox1 = Checkbutton(window,text='Java',variable=x,onvalue=1,offvalue=0,command=display)
checkbox1.pack()
checkbox1.config(font=('Arial'))
checkbox1.config(fg='#0000FF')
checkbox1.config(bg='#000000')
photo1=PhotoImage(file='java.png',width=250,height=250)
checkbox1.config(image=photo1,compound=RIGHT)
checkbox1.config(padx=25,pady=10)
checkbox1.config(anchor='w')
window.mainloop()