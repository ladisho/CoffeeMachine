from tkinter import *

window = Tk()
window.title("Miles_To_Kilometers_Converter")
# window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

#Padding is adding more space around your program

def calculate():
    miles = float(input.get())
    km = round(miles * 1.609)
    num_label.config(text=f"{km}")


#Entry
input = Entry(width=10)
input.grid(column=1, row=0)


#Labels
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=0)
# miles_label.config(padx=0, pady=0)


equal_to_label = Label(text="is equal to", font=("Arial", 10))
equal_to_label.grid(column=0, row=1)
# equal_to_label.config(padx=0, pady=0)

num_label = Label(text=0, font=("Arial", 10))
num_label.grid(column=1, row=1)
# num_label.config(padx=0, pady=0)

kilo_label = Label(text="Km", font=("Arial", 10))
kilo_label.grid(column=2, row=1)
# kilo_label.config(padx=0, pady=0)

#Button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=3)
# calculate_button.config(padx=0, pady=0)


window.mainloop()