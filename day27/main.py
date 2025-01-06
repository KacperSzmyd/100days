import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def calculate_miles():
    miles = input_field.get()
    calculated_km.config(text=round(int(miles) * 1.609344))


miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

calculated_km = tk.Label(text="0")
calculated_km.grid(column=1, row=1)

calculate_button = tk.Button(text="Calculate", command=calculate_miles)
calculate_button.grid(column=1, row=2)

input_field = tk.Entry(width=10)
input_field.insert(0, string="0")
input_field.grid(column=1, row=0)


window.mainloop()
