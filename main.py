from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letter = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols)for _ in range(nr_symbols)]


    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)

    passwordtxt = "".join(password_list)
    password_entry.insert(0,passwordtxt)
    pyperclip.copy(text=passwordtxt)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def validation():
    emailtxt = email_entry.get()
    websitetxt = website_entry.get()
    passwordtxt = password_entry.get()
    if len(emailtxt)==0 or len(websitetxt)==0 or len(passwordtxt)==0 or "@" not in emailtxt or ".com" not in emailtxt:
        messagebox.showinfo(title="Oops", message="The Email, Password, and website fields cannot be empty\n The email should contain '@' and '.com'")
    else:
        writetofile()  
    
        
        
def del_entry():
    website_entry.delete(0,END)
    password_entry.delete(0,END)
    website_entry.focus()

def writetofile():
    
    yes_or_no = messagebox.askokcancel(title="website", message=f"These are the details entered\nEmail : {email_entry.get()}\n Password : {password_entry.get()}\n is it ok to save?")
    if yes_or_no:
        with open("./python/pass/passwd.txt","a") as f:
            f.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            del_entry()
    else:
        return

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="./python/pass/logo.png")
canvas.create_image(100,100,image = lock_img)
canvas.grid(row=0,column=1)

website = Label(text="Website", )
website.grid(row=1,column=0)

website_entry = Entry(width=36)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()

email = Label(text="Email/Username",)
email.grid(row=2,column=0)

email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)


password = Label(text="Password", )
password.grid(row=3,column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

gen_pass = Button(text="Generate Password", width=14, command=gen_pass)
gen_pass.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=validation)
add_btn.grid(row=4,column=1, columnspan=2)



window.mainloop()


