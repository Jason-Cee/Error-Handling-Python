# importing tkinter module
from tkinter import *
from tkinter import messagebox

# configuration of the tkinter window
root = Tk()
root.title("Authentication")
root.geometry("400x400")
root.config(bg="#f9826c")
# labels and entry fields for the username and password
label = Label(root, text="Please Enter Login Details Below", bg="#f9826c")
label.place(x=90, y=5)
input_user = Label(root, text="Username", bg="#f9826c")
input_user.place(x=160, y=70)
user_entry = Entry(root)
user_entry.place(x=115, y=100)

input_pass = Label(root, text="Password", bg="#f9826c")
input_pass.place(x=160, y=150)
pass_entry = Entry(root)
pass_entry.place(x=115, y=180)


# functions for login details and to clear and exit the program
def check():
    username = ["Jason", "Yamkela", "Devin", "Shuaib"]
    passwords = ["1234", "abcd", "9876", "1020"]
    found = False
    for x1 in range(len(username)):
        if user_entry.get() == username[x1] and pass_entry.get() == passwords[x1]:
            found = True
        if found == True:
            messagebox.showinfo("STATUS", "Access granted")
        root.destroy()
        import next
    else:
        messagebox.showinfo("ERROR INFO", "Access denied")


def clear():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)


def exit_program():
    root.destroy()


# placement of all the buttons needed for the program
login_btn = Button(root, text="Login", fg="red", command=check)
login_btn.place(x=30, y=250)
clear_btn = Button(root, text="Clear", fg="red", command=clear)
clear_btn.place(x=170, y=250)
exit_btn = Button(root, text="Exit", fg="Red", command=exit_program)
exit_btn.place(x=300, y=250)

root.mainloop()
