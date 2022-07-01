# The classic FizzBuzz program

import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

user_input = simpledialog.askstring(title = '',prompt = 'Please enter a number')
print_num = True
for x in range(int(user_input)):
    if(x % 3 == 0):
        print('Fizz', end='')
        print_num = False
    if(x % 5  == 0):
        print('Buzz', end='')
        print_num = False
    if(print_num):
        print(x, end='')
    print()
    print_num = True


