import tkinter as tk

window = tk.Tk()
window.title("Widget examples")
window.minsize(500, 300)

my_label = tk.Label(text="I Am a Label")
my_label.pack()

input_field = tk.Entry(width=10)
input_field.insert(0, string="email")


def button_click():
    my_label.config(text=f"{input_field.get()}")


button = tk.Button(text="click me", command=button_click)
button.pack()
input_field.pack()
text_box = tk.Text(height=5, width=30)
text_box.insert("1.0", "Example of multi-lane text.")
text_box.pack()
spinbox = tk.Spinbox(from_=0, to=12, width=5)
spinbox.pack()
scale = tk.Scale(from_=0, to=100, width=5)
scale.pack()
checked_state = tk.IntVar()
checkbox = tk.Checkbutton(text="Is On?", variable=checked_state)
checkbox.pack()
radio_state = tk.IntVar()
option1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state)
option2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state)
option1.pack()
option2.pack()

cars = ["Honda", "Nissan", "Opel"]
lisbox = tk.Listbox(height=3)
for car in cars:
    lisbox.insert(cars.index(car), car)
lisbox.pack()

window.mainloop()
