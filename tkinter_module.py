import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I'm a label", font=("Arial", 24, "bold"))
# my_label.pack(side="bottom")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

def button_click():
    my_label.config(text=input.get())
    print("I got clicked")


button = tkinter.Button(text="Click Me", command=button_click)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="Do not click me")
new_button.grid(column=2, row=0)

input = tkinter.Entry()
# input.pack()
input.grid(column=3, row=4)         # Cannot use pack() and grid() together
# input.get()



window.mainloop()
