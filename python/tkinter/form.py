from tkinter import *
from tkinter import messagebox
window =  Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')
def login():
 username="Samikshya RanaBhat"
 password='09876'
 if username_entry.get()==username and password_entry.get()==password:
  
  messagebox.showinfo(title="LogIn Success", message="You succesfullt logged in")
 else:
  messagebox.showerror(title="Error", message="Invalid Login")
frame = Frame(bg="#333333")
# label = Label(window,
#                       text="LogIn")
# label.pack() #yo garyo vani tyo text comes at middle
# but if we use label.grid(row=0, column=0) the text comes at the left side of the screen.

# Creating widgets
login_label = Label(frame, text="Login" ,bg='#333333',fg='white', font=("Arial", 30))
username_label = Label(frame, text="Username" ,bg='#333333', fg='white', font=('Arial, 16'))
username_entry= Entry(frame, font=("Arial, 16"))
password_entry=Entry(frame, show="*", font=("Arial, 16"))
password_label=Label(frame, text="Password", bg='#333333', fg='white', font=("Arial, 16"))
login_button = Button(frame, text="Login",bg="#FF3399", fg='white', font=("Arial, 16"), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()
window.mainloop()
