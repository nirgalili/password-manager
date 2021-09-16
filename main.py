from tkinter import *
from tkinter import messagebox

# enter your personal email
MY_EMAIL = "nirgalili1@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
# function for press add
def press_add():
    # open file data.txt
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                     f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                # add new line to file
                file.write(f"{website} | {email} | {password}\n")
            # clear field in UI
            input_website.delete(0, END)
            input_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img) # 100,100 is the center of canvas were we want the center of the pic to be
canvas.grid(column=1, row=0)

# labels
website = Label(text="Website:", bg="white")
website.grid(column=0, row=1)

email = Label(text="Email/Username:", bg="white")
email.grid(column=0, row=2)

password = Label(text="Password:", bg="white")
password.grid(column=0, row=3)

# Entry
input_website = Entry(width=51)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_email = Entry(width=51)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, string=MY_EMAIL)

input_password = Entry(width=32)
input_password.grid(column=1, row=3)


# buttons
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=press_add)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()