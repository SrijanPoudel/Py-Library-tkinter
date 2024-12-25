from tkinter import *
window = Tk()
photo = PhotoImage(file='shrijan.png')
window.geometry('400x400')
label=Label(window,text='Hey',font=('Arial',40,'bold'),fg='Green',bg='white',relief=RAISED,bd=10,padx=20,pady=20,image=photo)
label.pack()
window.mainloop()
