import requests
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

apiKey = 'API_KEY'
url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_f1xgKdu36Sp7LCw7gHOtLMgbByHrZXWO5ML4Tier'

response = requests.get(url)
data_menu = response.json()

currencies = list(data_menu['data'].keys())


def convert_currencies():
    selected_currency1 = variable1.get()
    selected_currency2 = variable2.get()

    value1 = entry1.get()

    if not value1 or not value1.isdigit():
        messagebox.showerror("Error", "Please enter a valid numeric value.")
        return

    value1 = float(value1)

    if selected_currency1 == selected_currency2:
        messagebox.showerror("Invalid Conversion", "Please select different currencies.")
        return

    base_currency = data_menu['data'][selected_currency2] / data_menu['data'][selected_currency1]
    result_currency = base_currency * value1

    result_label.config(text=f"{value1} {selected_currency1} equals to {result_currency:.2f} {selected_currency2}")

    entry1.delete(0, END)

    if not selected_currency1 or not selected_currency2:
        messagebox.showerror("Select Valid Input", "Please select valid currencies.")


window = Tk()
window.title("CURRENCY CONVERTER")

title_label = Label(window, text="CURRENCY CONVERTER", font=('Helvetica', 14, 'italic'), bg='yellow')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

label1 = Label(window, text="Select a currency:")
label1.grid(row=1, column=0)
label1.configure(bg='red', font=('Helvetica', 10, 'bold'))

variable1 = StringVar(window)
variable1.set('')
w1 = Combobox(window, textvariable=variable1, values=currencies)
w1.grid(row=1, column=1, pady=5)

gap_label = Label(window, text="", width=0)
gap_label.grid(row=1, column=2)

entry1 = Entry(window, width=10)
entry1.grid(row=1, column=3, pady=5)

label2 = Label(window, text="Select the currency to be converted:")
label2.grid(row=2, column=0, pady=5)
label2.configure(bg='red', font=('Helvetica', 10, 'bold'))

variable2 = StringVar(window)
variable2.set('')
w2 = Combobox(window, textvariable=variable2, values=currencies)
w2.grid(row=2, column=1, pady=1)


convert_button = Button(window, text="Convert", command=convert_currencies)
convert_button.grid(row=3, column=0, columnspan=4, pady=5)

result_label = Label(window, text="")
result_label.grid(row=4, column=0, columnspan=4, pady=5)

window.mainloop()
