from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# TODO 1 Labels
label1 = Label(text="Miles")
label2 = Label(text="Km")
label3 = Label(text="is equal to")
label1.grid(column=2, row=0)
label2.grid(column=2, row=1)
label3.grid(column=0, row=1)
# output = Label(text=result)


def calculation():
    result = float(input.get()) * 1.609
    output = Label(text=result.__round__(2))
    output.grid(column=1, row=1)


# TODO 2 Button
button = Button(text="Calculate", command=calculation)
button.grid(column=1, row=2)

# TODO 3 Entry
input = Entry(width=5)
input.grid(column=1, row=0)

window.mainloop()