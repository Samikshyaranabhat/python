from tkinter import *
count = 0
def click():
    global count
    count += 1
    print(count)
    print("You clicked the button")
window = Tk()
button = Button(window,
                text = 'Click Me!',
                command = click,
                fg='green',
                bg='black',
                activeforeground='green',
                activebackground='black',
                # state=DISABLED, no any occurence of stuff even we click the button

                )
button.pack()
window.mainloop()