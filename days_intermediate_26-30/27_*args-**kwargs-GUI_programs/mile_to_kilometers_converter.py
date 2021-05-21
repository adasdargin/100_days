from tkinter import *


def convert():
    miles_to_km = round(float(user_input.get()) * 1.609, 2)
    label_answer.config(text=f"{miles_to_km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# label
label_miles = Label(text="Miles", font=("Courier", 12, "normal"))
label_miles.grid(column=3, row=0)

label_km = Label(text="Km", font=("Courier", 12, "normal"))
label_km.grid(column=3, row=1)

label_is_equal = Label(text="is equal to", font=("Courier", 12, "normal"))
label_is_equal.grid(column=0, row=1)

label_answer = Label(text=0, font=("Courier", 12, "normal"))
label_answer.grid(column=1, row=1)

# button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)

# entry
user_input = Entry(width=10)
user_input.grid(column=1, row=0)


window.mainloop()