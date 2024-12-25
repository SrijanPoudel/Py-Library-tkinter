from tkinter import *
food=['Pizza',"HamBurger","HotDogs"]
window=Tk()
window.title("Food Menu")
x=IntVar()
def order():
    if (x.get()==0):
        print("You order Pizza")
    elif(x.get()==1):
        print("You order HamBurger")
    else:
        print("You order HotDogs")
pizza_image = PhotoImage(file='pizza.png').subsample(7, 7)  # Reduce size by 5x
hamburger_image = PhotoImage(file='Hamburger.png').subsample(7, 7)
hotdog_image = PhotoImage(file='Hotdog.png').subsample(5, 3)
food_image=[pizza_image,hamburger_image,hotdog_image]
for index in range(len(food)):
    radiobutton=Radiobutton(window,
                            text=food[index],fg='Black',
                            variable=x, #grouping differe value together
                            value=index, # giving seperate index to eaach value
                            padx=25,# padding in x axis
                            font= ("Impact",50),
                            image=food_image[index],
                            compound=LEFT,
                            indicatoron=0,width=390,command=order) #circle indicator eliminator
    
    radiobutton.pack(anchor=W)
window.mainloop()