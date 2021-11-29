from tkinter import Label, ttk 
from ttkthemes import ThemedTk
import tkinter as tk
import guicontroller as gc
from tkinter import filedialog

FROM_X = 0
TO_X = 100
SPIN_WIDTH = 10
PADY_BOXES = (0, 5)
BUTTON_PAD = 3
BUTTON_WIDTH = 5
    
def main():
    # Configuring window
    root = ThemedTk(theme="breeze")
    root.title("Root Finding")
    root.geometry('1000x550+250+100')
    root.resizable(False, False) 
    root.iconbitmap("root-icon.ico")

    # Creating the widgets
    input_frame = ttk.LabelFrame(root, text="Input", padding=20)
    output_frame = ttk.LabelFrame(root, text="Output", padding=20)

    button_frame = ttk.Frame(input_frame, padding=20)

    # Input widgets
    enter_label= ttk.Label(input_frame, text="Enter Expression f(x)", width=20)
    entry_string = tk.StringVar()
    entry_string.set("x^2-3*x")
    exp_entry = ttk.Entry(input_frame, textvariable=entry_string, width=40)
    exp_entry.focus()
    exp_entry.icursor(exp_entry.index(tk.END))
    file_btn = ttk.Button(input_frame, text="Choose from a file", command=lambda:gc.choose_file(exp_entry))

    methods = [
        "Bisection",
        "Regula Falsi",
        "Fixed Point",
        "Newton Raphson",
        "Secant"
    ]
    method = tk.StringVar()
    method.set(methods[0])
    method_label = ttk.Label(input_frame, text="Method")
    method_options = ttk.Combobox(input_frame, textvariable=method, values=methods, state="readonly")
    method_options.config(width=20)


    precision_label = ttk.Label(input_frame, text="Precision")
    precision_var = tk.DoubleVar()
    precision_var.set(0.00001)
    precision_spin = ttk.Spinbox(input_frame, textvariable=precision_var, width=SPIN_WIDTH, from_=0, to=1, increment=.00001)

    maxiter_label = ttk.Label(input_frame, text="Max Iterations")
    maxiter_var = tk.IntVar()
    maxiter_var.set(50)
    maxiter_spin = ttk.Spinbox(input_frame, textvariable=maxiter_var, width=SPIN_WIDTH, from_=FROM_X, to=TO_X)

    lowerbound_label = ttk.Label(input_frame, text="Lower Bound")
    lowerbound_var = tk.DoubleVar()
    lowerbound_spin = ttk.Spinbox(input_frame, textvariable=lowerbound_var, width=SPIN_WIDTH, from_=FROM_X, to=TO_X)

    upperbound_label = ttk.Label(input_frame, text="Upper Bound")
    upperbound_var = tk.DoubleVar()
    upperbound_spin = ttk.Spinbox(input_frame, textvariable=upperbound_var, width=SPIN_WIDTH, from_=FROM_X, to=TO_X)

    initialguess_label = ttk.Label(input_frame, text="Initial Guess")
    initialguess_var = tk.DoubleVar()
    initialguess_spin = ttk.Spinbox(input_frame, textvariable=initialguess_var, width=SPIN_WIDTH, from_=FROM_X, to=TO_X)

    firstguess_label = ttk.Label(input_frame, text="First Guess")
    firstguess_var = tk.DoubleVar()
    firstguess_spin = ttk.Spinbox(input_frame, textvariable=firstguess_var, width=SPIN_WIDTH, from_=FROM_X, to=TO_X)

    secondguess_label = ttk.Label(input_frame, text="Second Guess")
    secondguess_var = tk.DoubleVar()
    secondguess_spin = ttk.Spinbox(input_frame, textvariable=secondguess_var, width=SPIN_WIDTH, from_=FROM_X, to=TO_X)

    var_widgets = [
        lowerbound_label, lowerbound_spin,
        upperbound_label, upperbound_spin,
        initialguess_label, initialguess_spin,
        firstguess_label, firstguess_spin,
        secondguess_label, secondguess_spin,
        enter_label
    ]

    vars = [
        exp_entry,
        method,
        lowerbound_var,
        upperbound_var,
        initialguess_spin,
        firstguess_spin,
        secondguess_var
    ]

    method_options.bind('<<ComboboxSelected>>', lambda *args: gc.method_change(var_widgets, method.get(), methods))

    calc_btn = ttk.Button(input_frame, text="Calculate Root", command=lambda: gc.calc(vars))

    notes = "Notes for expression entry: \n \
        - You can enter expression using keyboard, provided buttons, or by uploading a txt file \n \
        - Exponential must be written as 'E' \n \
        - Multiplication must be done as '2*x' not 2x \n \
        - You can evaluate square root using 'sqrt()' \n \
        - You can evaluate powers using '^'"
    notes_label = ttk.Label(input_frame, text=notes, foreground="#808080")

    # creating some buttons to help the user
    clear_btn = ttk.Button(button_frame, text="clear", width=BUTTON_WIDTH, command=lambda *args: gc.clear(exp_entry))
    x_button = ttk.Button(button_frame, text="x", width=BUTTON_WIDTH, command=lambda *args: gc.x(exp_entry))
    plus_button = ttk.Button(button_frame, text="+", width=BUTTON_WIDTH, command=lambda *args: gc.plus(exp_entry))
    minus_button = ttk.Button(button_frame, text="-", width=BUTTON_WIDTH, command=lambda *args: gc.minus(exp_entry))
    mult_button = ttk.Button(button_frame, text="*", width=BUTTON_WIDTH, command=lambda *args: gc.mult(exp_entry))
    div_button = ttk.Button(button_frame, text="/", width=BUTTON_WIDTH, command=lambda *args: gc.div(exp_entry))
    pwr_button = ttk.Button(button_frame, text="^", width=BUTTON_WIDTH, command=lambda *args: gc.pwr(exp_entry))
    sqrt_button = ttk.Button(button_frame, text="sqrt()", width=BUTTON_WIDTH, command=lambda *args: gc.sqrt(exp_entry))
    leftbracket_button = ttk.Button(button_frame, text="(", width=BUTTON_WIDTH, command=lambda *args: gc.leftbracket(exp_entry))
    rightbracket_button = ttk.Button(button_frame, text=")", width=BUTTON_WIDTH, command=lambda *args: gc.rightbracket(exp_entry))


    # Output widgets
    # output_txt = ttk.Entry(output_frame, state=tk.DISABLED, width=40)
    output_txt = ttk.Label(output_frame, width=40)

    # Styling 
    # style = ttk.Style()
    # style.configure("Red.TCheckbutton", foreground="red")

    # Displaying the widgets
    input_frame.grid(column=0, row=0, padx=20, pady=20)
    output_frame.grid(column=1, row=0, padx=20, pady=20. , sticky=tk.N+tk.S+tk.W)

    button_frame.grid(column=3, row=2, rowspan=6)

    enter_label.grid(column=0, row=0, sticky=tk.W)
    exp_entry.grid(column=0, row=1, columnspan=3, sticky=tk.W, pady=PADY_BOXES)
    file_btn.grid(column=3, row=1)

    method_label.grid(column=0, row=2, sticky=tk.W)
    method_options.grid(column=0, row=3, columnspan = 2, sticky=tk.W, pady=PADY_BOXES)

    precision_label.grid(column=0, row=4, sticky=tk.W)
    maxiter_label.grid(column=1, row=4, sticky=tk.W)

    precision_spin.grid(column=0, row=5, sticky=tk.W, pady=PADY_BOXES)
    maxiter_spin.grid(column=1, row=5, sticky=tk.W, pady=PADY_BOXES)

    lowerbound_label.grid(column=0, row=6, sticky=tk.W)
    upperbound_label.grid(column=1, row=6, sticky=tk.W)

    lowerbound_spin.grid(column=0, row=7, sticky=tk.W, pady=PADY_BOXES)
    upperbound_spin.grid(column=1, row=7, sticky=tk.W, pady=PADY_BOXES)

    calc_btn.grid(column=3, row=8, padx=10, pady=10)
    notes_label.grid(column=0, row=9, columnspan=4, pady=PADY_BOXES)

    clear_btn.grid(column=0, row=0, padx=BUTTON_PAD, pady=BUTTON_PAD)
    x_button.grid(column=1, row=0, padx=BUTTON_PAD, pady=BUTTON_PAD)
    plus_button.grid(column=0, row=1, padx=BUTTON_PAD, pady=BUTTON_PAD)
    minus_button.grid(column=1, row=1, padx=BUTTON_PAD, pady=BUTTON_PAD)
    mult_button.grid(column=0, row=2, padx=BUTTON_PAD, pady=BUTTON_PAD)
    div_button .grid(column=1, row=2, padx=BUTTON_PAD, pady=BUTTON_PAD)
    pwr_button.grid(column=0, row=3, padx=BUTTON_PAD, pady=BUTTON_PAD)
    sqrt_button.grid(column=1, row=3, padx=BUTTON_PAD, pady=BUTTON_PAD)
    leftbracket_button.grid(column=0, row=4, padx=BUTTON_PAD, pady=BUTTON_PAD)
    rightbracket_button.grid(column=1, row=4, padx=BUTTON_PAD, pady=BUTTON_PAD)

    output_txt.grid(column=0, row=0, sticky=tk.N+tk.S)

    root.protocol("WM_DELETE_WINDOW", lambda:gc.destroyer(root))
    root.mainloop()

main()