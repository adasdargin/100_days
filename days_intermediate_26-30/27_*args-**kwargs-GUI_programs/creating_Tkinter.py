import tkinter


def button_clicked():
    print("Click")
    my_label.config(text=input.get())


window = tkinter.Tk()
window.title("My 1st GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Courier", 24, "bold"))

# configuring text
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)


# button
button = tkinter.Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# entry
input = tkinter.Entry(width=10)
input.grid(column=4, row=3)


window.mainloop()