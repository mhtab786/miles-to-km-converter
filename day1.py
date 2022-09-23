from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles*1.609
    km_result_label.config(text=f"{km}")

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Kilo Meter")
km_label.grid(column=2, row=1)

calculate_btn = Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2)

window.mainloop()
