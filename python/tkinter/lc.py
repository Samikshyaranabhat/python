from tkinter import *
import random

window = Tk()
window.geometry('500x500')
window.title('Love Calculator')

def calculate_love():
    st = '0123456789'
    digit = 2
    temp = " ".join(random.sample(st, digit))
    result.config(text=temp)

# Set up the GUI components
heading = Label(window, text='Love Calculator\n How much is he/she onto you?')
heading.pack()

slot1 = Label(window, text="Enter your Name:")
slot1.pack()
name1 = Entry(window, border=5)
name1.pack()

slot2 = Label(window, text="Enter your partner's Name:")
slot2.pack()
name2 = Entry(window, border=5)
name2.pack()

bt = Button(window, text='Calculate', height=1, width=8, command=calculate_love)
bt.pack()

result = Label(window, text='Love percentage between both of you:')
result.pack()

window.mainloop()