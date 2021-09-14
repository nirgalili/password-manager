from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

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

#Entry
input_website = Entry(width=50)
input_website.grid(column=1, row=1, columnspan=2)

input_email = Entry(width=50)
input_email.grid(column=1, row=2, columnspan=2)

input_password = Entry(width=32)
input_password.grid(column=1, row=3)

# buttons
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43)
add_button.grid(column=1, row=4, columnspan=2)

# r = Label(bg="red", width=20, height=5)
# r.grid(row=0, column=0)
#
# g = Label(bg="green", width=20, height=5)
# g.grid(row=1, column=1)
#
# b = Label(bg="blue", width=40, height=5)
# b.grid(row=2, column=0, columnspan=2)

window.mainloop()