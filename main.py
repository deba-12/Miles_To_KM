from tkinter import *

# Create the main window
window = Tk()
window.title("Mile/Km Converter")
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)

# Entry widget for input
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Function to convert based on user selection
def action():
    value = float(entry.get())
    if conversion_type.get() == 1:  # Miles to Km
        converted_value = value * 1.60934
        result_label.config(text=f"{converted_value:.2f}")
        unit_label.config(text="Km")
    else:  # Km to Miles
        converted_value = value / 1.60934
        result_label.config(text=f"{converted_value:.2f}")
        unit_label.config(text="Miles")

# Radio buttons to choose conversion type
conversion_type = IntVar()
conversion_type.set(1)  # Default to Miles to Km

miles_to_km = Radiobutton(text="Miles to Km", value=1, variable=conversion_type)
miles_to_km.grid(column=0, row=0)

km_to_miles = Radiobutton(text="Km to Miles", value=2, variable=conversion_type)
km_to_miles.grid(column=0, row=1)

# Button to trigger conversion
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

# Labels
input_label = Label(text="Enter value")
input_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=3)

result_label = Label(text="0")
result_label.grid(column=1, row=3)

unit_label = Label(text="")
unit_label.grid(column=2, row=3)

# Run the Tkinter event loop
window.mainloop()
