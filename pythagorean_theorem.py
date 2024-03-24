import tkinter as tk
from tkinter import *
from tkinter import ttk
import math
from PIL import ImageTk, Image, ImageDraw, ImageFont

a = 0
b = 0
c = 0

def pyth_theorem(a,b,c):
    a = str(input("What is the value for a?\n"))
    b = str(input("What is the value for b?\n"))

    if a == "none":
        c = str(input("What is the value for c?\n"))
        c = int(c)
        b = int(b)
        a = (c**2-b**2)
        if a >=0:
            print("The value for a is","%.2f"%math.sqrt(a))
        else:
            print("The value is", a,"and since the square root of a negative number is an imaginary number, please check your entries and try again.")
    if b == "none":
        c = str(input("What is the value for c?\n"))
        c = int(c)
        a =int(a)
        b = (c**2-a**2)
        if b >=0:
            print("The value for a is", "%.2f"%math.sqrt(b))
        else:
            print("The value is", b, "and since the square root of a negative number is an imaginary number, please check your entries and try again.")

    elif b != "none" and a != "none":
        b = int(b)
        a = int(a)
        c = "%.2f"%math.sqrt((a**2+b**2))
        print("The value for c is", c)

root =tk.Tk()
root.geometry("800x600")
root.title("Pythagreon's Theorem")

image_logo = Image.open("pythagreon.jpg").resize((230, 230))
image_tk = ImageTk.PhotoImage(image_logo)
label = ttk.Label(root, text = "Pythagreon Logo", image = image_tk)
label.grid(row=0, column=0, padx=275)

a = Label(root, text= "Enter the value for a:").grid(row=1, column=0, padx=155,sticky=W)
value_a= Entry(root, bd=3)
value_a.grid(row=1,padx=0)

Label(root, text= "Enter the value for b:").grid(row=2, column=0, padx=155,pady=5,sticky=W)
value_b= Entry(root, bd=3)
value_b.grid(row=2,padx=5)

Label(root, text= "Enter the value for c:").grid(row=3, column=0, padx=155,pady=5, sticky=W)
value_c= Entry(root, bd=3)
value_c.grid(row=3,padx=5)

# input_field_a = tk.Entry(root)
# input_field_b = tk.Entry(root)
# input_field_c = tk.Entry(root)
# a = input_field_a.pack(pady=5)
# b = input_field_b.pack(pady=5)
# c = input_field_c.pack(pady=5)

# calculate_button = tk.Button(root, text = "Calculate Value")
# calculate_button.place(x=295,y=400)

# quit_button = tk.Button(root, text= "Close", command=root.quit)
# quit_button.place(x=430, y=400)
root.mainloop()
