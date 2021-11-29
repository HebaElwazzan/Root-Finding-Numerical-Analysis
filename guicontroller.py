import json
from math import exp
import os
import sys
from exceptions import *

from sympy.core import symbol
import parse
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

DECIMAL_NUM = 18

i = 0
def choose_file(exp_entry):
    filename = filedialog.askopenfilename(initialdir="", title="Choose a file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    try:
        with open(filename) as f:
            text = f.readline()
        exp_entry.delete(0,"end")
        exp_entry.insert(0, text)
    except FileNotFoundError:
        pass

def destroyer(root):
    if messagebox.askquestion("Quit", "Are you sure you want to quit?") == "yes":
        root.quit()
        root.destroy()
        sys.exit()

def method_change(all_widgets, method_name, methods_list):
    # receive list of widgets and the method name chosen
    # remove visible widgets from grid
    # if name is bisection or regula falsi: show widgets for lowerbound and upperbound
    # if name is newton raphson or fixed point: show widgets for initial guess
    # if name is secant: show widgets for first guess and second guess
    # Extra: for fixed point and secant, specify that user enters g(x), f(x) otherwise

    for widget in all_widgets[:len(all_widgets) - 1]:
        widget.grid_remove()
    
    if method_name == methods_list[0] or method_name == methods_list[1]:
        all_widgets[0].grid(column=0, row=6, sticky=tk.W)
        all_widgets[2].grid(column=1, row=6, sticky=tk.W)

        all_widgets[1].grid(column=0, row=7, sticky=tk.W, pady=(0, 5))
        all_widgets[3].grid(column=1, row=7, sticky=tk.W, pady=(0, 5))

    if method_name == methods_list[2] or method_name == methods_list[3]:
        all_widgets[4].grid(column=0, row=6, sticky=tk.W)

        all_widgets[5].grid(column=0, row=7, sticky=tk.W, pady=(0, 5))

    if method_name == methods_list[4]:
        all_widgets[6].grid(column=0, row=6, sticky=tk.W)
        all_widgets[8].grid(column=1, row=6, sticky=tk.W)

        all_widgets[7].grid(column=0, row=7, sticky=tk.W, pady=(0, 5))
        all_widgets[9].grid(column=1, row=7, sticky=tk.W, pady=(0, 5))

    if method_name == methods_list[0] or method_name == methods_list[1] or method_name == methods_list[3]:
        all_widgets[-1].config(text="Enter Expression f(x)")

    if method_name == methods_list[2] or method_name == methods_list[4]:
        all_widgets[-1].config(text="Enter Expression g(x)")

def button_click(exp_entry, symbol):
    current = exp_entry.get()
    exp_entry.insert(exp_entry.index(tk.INSERT), symbol)
    exp_entry.focus()
    if "()" in symbol:
        exp_entry.icursor(exp_entry.index(tk.INSERT) - 1)

def x(exp_entry):
    button_click(exp_entry, "x")

def plus(exp_entry):
    button_click(exp_entry, "+")

def minus(exp_entry):
    button_click(exp_entry, "-")

def mult(exp_entry):
    button_click(exp_entry, "*")

def div(exp_entry):
    button_click(exp_entry, "/")

def pwr(exp_entry):
    button_click(exp_entry, "^")

def sqrt(exp_entry):
    button_click(exp_entry, "sqrt()")

def leftbracket(exp_entry):
    button_click(exp_entry, "()")

def rightbracket(exp_entry):
    button_click(exp_entry, ")")

def cos(exp_entry):
    button_click(exp_entry, "cos()")

def sin(exp_entry):
    button_click(exp_entry, "sin()")

def e(exp_entry):
    button_click(exp_entry, "E")

def clear(exp_entry):
    exp_entry.delete(0, tk.END)
    exp_entry.focus()

def update_output(output, text, color="black"):
    output.configure(state='normal', foreground=color)
    output.delete("1.0", tk.END)
    output.insert('1.0', text)
    output.configure(state='disabled')

def calc(input_list, out):
    update_output(out, "Calculating...")
    vars = {
        'expression': input_list[0].get(),
        'method': input_list[1].get(),
        'error tolerance': input_list[2].get(),
        'max step': input_list[3].get(),
        'lower bound': input_list[4].get(),
        'upper bound': input_list[5].get(),
        'initial guess': float(input_list[6].get()),
        'first guess': float(input_list[7].get()),
        'second guess': input_list[8].get(),
        'file path': 'out.json'
    }
    with open("input.json", "w") as outfile:
        json.dump(vars, outfile)

    if os.path.isfile("out.json"):
        os.remove("out.json")

    try: 
        parse.call_from_file()
    except (notConvergent, noRootInInterval, badExpression, cannotDiffererntiate, badDictionary) as e:
        update_output(out, e, color="red")
        return 
    except Exception as e:
        # update_output(out, "Unexpected error!", color="red")
        print(e)

    
    out.after(1000, lambda *args: check(out))
    


def check(out):
    if os.path.isfile("out.json"):
        try:
            output = parse.fileToDict("out.json")
            update_output(out, format_dict(output))
        except FileNotFoundError as e:
            update_output(out, "")
            print(e)
    else:
        update_output(out, "Calculating...")
        out.after(1000, lambda *args: check(out))


def format_dict(dict):
    output = ""
    for key, value in dict.items():
        if isinstance(value, list):
            output += key + ":\n"
            for item in value:
                output += str(item) + "\n"
        else: 
            output += key + ": " + str(value) +"\n"
    return output
