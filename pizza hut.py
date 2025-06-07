import tkinter as tk
from tkinter import ttk

def place_order():
    pizza = pizza_var.get()
    quantity = quantity_var.get()
    size = size_var.get()

    size_text = {
        'S': 'Small',
        'M': 'Medium',
        'L': 'Large'
    }

    result = f"You ordered {quantity} {pizza} {size_text[size]} Size Pizza(s)"
    result_label.config(text=result)

#screen
screen = tk.Tk()
screen.title("Pizza hut app")
screen.geometry("400x250")


title_label = tk.Label(screen, text="Welcome to Pizza Hut", font=("Arial", 14))
title_label.pack(pady=10)

frame = tk.Frame(screen)
frame.pack()

tk.Label(frame, text="Select Your Fav Pizza:").grid(row=0, column=0, padx=5, pady=5)
pizza_var = tk.StringVar()
pizza_menu = ttk.Combobox(frame, textvariable=pizza_var)
pizza_menu['values'] = ("Veg Extravaganza", "Pepperoni", "Margherita", "Farmhouse")
pizza_menu.current(0)
pizza_menu.grid(row=0, column=1, padx=5, pady=5)


tk.Label(frame, text="Enter Quantity:").grid(row=1, column=0, padx=5, pady=5)
quantity_var = tk.StringVar()
quantity_menu = ttk.Combobox(frame, textvariable=quantity_var)
quantity_menu['values'] = [str(i) for i in range(1, 11)]
quantity_menu.current(0)
quantity_menu.grid(row=1, column=1, padx=5, pady=5)


size_var = tk.StringVar(value='S')
tk.Radiobutton(frame, text='S', variable=size_var, value='S').grid(row=0, column=2, padx=10)
tk.Radiobutton(frame, text='M', variable=size_var, value='M').grid(row=1, column=2, padx=10)
tk.Radiobutton(frame, text='L', variable=size_var, value='L').grid(row=2, column=2, padx=10)


order_btn = tk.Button(screen, text="Order", command=place_order)
order_btn.pack(pady=10)


result_label = tk.Label(screen, text="", fg="green", font=("Arial", 10))
result_label.pack(pady=5)

# Run app
screen.mainloop()
