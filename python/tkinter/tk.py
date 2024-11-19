from tkinter import*
window = Tk() #instantiate an instance of window
window.geometry("800x420") #for width and breadth of the window
window.title("First GUI Program")
# window.config(background="white")

photo = PhotoImage(file='tkinter/pngimg.com - fanta_PNG39.png')

label = Label(window,
               text="Have a break,Have a fanta", 
               font=('Arial',40,'bold'),
               fg='brown',
               bg='white',
               relief=RAISED,
               bd=10,
               padx=20,
               pady=20,
               image = photo,
               compound = 'bottom',#left,right..........


               )
label.place(x=0, y=0)   #places the text or anything accordifing to the give value for x and y
#label.pack() places the text or anything at the middle of the window


window.mainloop() #place window on cmputer screen, listen for events

#label :An area widgwt that holds text and/or an image within a window
#button :You click it,then it does stuff