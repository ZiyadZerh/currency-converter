import requests
import tkinter as tk
from tkinter import Tk, StringVar

window = Tk()
window.title("Currency converter")
window.configure(bg='grey')

window.geometry("500x175")
class CurrencyConverter():
	def __init__(self,url):
		self.data= requests.get(url).json()
		self.currencies = self.data['rates']

	def convert(self, from_currency, to_currency, amount=1): 
	    initial_amount = amount
	    from_currency = from_currency.upper()
	    to_currency = to_currency.upper()
	    amount = round(amount, 5)
	    if from_currency != 'USD' : 
	        amount = amount / self.currencies[from_currency]
	    amount = amount * self.currencies[to_currency]
	    return amount

url = 'https://api.exchangerate-api.com/v4/latest/USD'

default_choice1 = StringVar(window)
default_choice1.set("USD")

default_choice2 = StringVar(window)
default_choice2.set("EUR")

label_displayed = False

def get_currency_value():
	return float(first_currency_amount.get("1.0", tk.END))

def get_currency():
	return [default_choice1.get(), default_choice2.get()]

def converter():
	global first, second, third, result
	first = get_currency()[0]
	second = get_currency()[1]
	third = get_currency_value()
	result = round(CurrencyConverter("https://api.exchangerate-api.com/v4/latest/USD").convert(first, second, third), 5)
	return result

def display_result():
	global label_displayed
	label_displayed = True
	converter()
	if label_displayed:
		final.config(text=f" {third} {first} = {result} {second}")
		final.grid(row=3, column=2)
		label_displayed = False

options = [i for i in CurrencyConverter(url).currencies]

first_currency_choice = tk.OptionMenu(window, default_choice1, *options)
second_currency_choice = tk.OptionMenu(window, default_choice2, *options)

first_currency_amount = tk.Text(window)

get_result = tk.Button(window, text="convert", command=display_result)

final = tk.Label(window)

first_currency_choice.config(width=7, height=1, relief=tk.FLAT, bg="#ffe1c9", font=("Helvetica", 15))
second_currency_choice.config(width=7, height=1, relief=tk.FLAT, bg="#ffe1c9", font=("Helvetica", 15))

first_currency_amount.config(width=15, height=1.2, relief=tk.FLAT, font=("Helvetica", 15))

get_result.config(width=10, font=("Helvetica", 15))

final.config(font=("Helvetica", 15))

first_currency_choice.grid(row=1, column=1, pady=10, padx=2)
second_currency_choice.grid(row=2, column=1, pady=10, padx=2)

first_currency_amount.place(x=130, y=16)

get_result.grid(row=3, column=1, columnspan=1)

window.mainloop()