from tkinter import *
window = Tk()
entry=Entry()
entry.pack()
entry.config(font=('Arial',50))
#entry.config(show='*')
entry.config(bg="green")
entry.insert(0,'Type')
entry.config(width=10)
#entry.config(state=DISABLED)
def submit():
    username= entry.get()
    print(username)
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete((len(entry.get())-1),END)
submit= Button(window,text="Submit",command=submit)
delete = Button(window,text="delete",command=delete)
backspace=Button(window,text="backspace",command=backspace)
backspace.pack(side=RIGHT)
delete.pack(side=LEFT)
submit.pack(side = RIGHT)

window.mainloop()