from tkinter import *
from random import randint, shuffle, choice
from tkinter import messagebox #another module of the code not a class
import pyperclip #to copy to clipboard
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list1=[choice(letters) for i in range(randint(8, 10))]
    list2=[choice(symbols) for i in range(randint(2, 4))]
    list3=[choice(numbers) for i in range(randint(2, 4))]
    password_list=list1+list2+list3
    shuffle(password_list)

    password = "".join(password_list) #to make the list into a string directly
    input3.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=input1.get()
    mail=input2.get()
    password=input3.get()

    new_data={
        website:{
            "email":mail,
            "password":password,
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="cant leave any fields empty")
    else:
        try:
            with open("Password_File.json","r") as pass_file:
                data=json.load(pass_file)#stores the file data to the data variable
        except :#if the file does not preexist then we create one
            with open("Password_File.json","w") as pass_file:
                json.dump(new_data , pass_file , indent=4)
        else:
            data.update(new_data)  # appends the new data to the existing data
            with open("Password_File.json","w")as pass_file:
                json.dump(data , pass_file , indent=4)
        finally:
            input1.delete(0,END)
            input3.delete(0,END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website=input1.get()
    try:
        with open("Password_File.json","r") as pass_file:
            data = json.load(pass_file)  # stores the file data to the data variable
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website not in data:
                messagebox.showinfo(title="Oops",message="No details for the website exist")
        else:
            x=data[website]["email"]
            y=data[website]["password"]
            messagebox.showinfo(title="Password exist",message=f"Email:{x} \nPassword:{y}")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas=Canvas(width=200, height=200)
lock_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)#args are the x and y of the center of the image
canvas.grid(row=0,column=1)


website_label=Label(text="Website:")
website_label.grid(row=1, column=0)
input1=Entry(width=32)
input1.focus()
input1.grid(row=1, column=1)

email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)
input2=Entry(width=51)
input2.insert(0,"Vinaayakbhardwaj@gmail.com")
input2.grid(row=2, column=1, columnspan=2)

Password_label=Label(text="Password:")
Password_label.grid(row=3, column=0)
input3=Entry(width=32)
input3.grid(row=3, column=1)


pass_button=Button(text="Generate Password",command=generate)
pass_button.grid(column=2 ,row=3)

add_button=Button(text="ADD", width=44, command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text="Search",width=15,command=find_password)
search_button.grid(row=1,column=2)
window.mainloop()