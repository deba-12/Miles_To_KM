from tkinter import *

# Create the main window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)

# Entry widget for input
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Function to convert miles to kilometers
def action():
    miles = float(entry.get())
    km = miles * 1.60934
    result_label.config(text=f"{km:.2f}")

# Button to trigger conversion
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Run the Tkinter event loop
window.mainloop()
