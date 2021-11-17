import tkinter as tk

def init_tkinter(title):
    root = tk.Tk();
    root.title(title)
    return root;

def on_click(root,entry_string):
    #do something
    msg = "Evaluating:"+entry_string.get()
    label = tk.Label(root,text=msg)
    label.grid(column=2,row=3)
    return
    
def main():
    root = init_tkinter("Root Finding")
    root.geometry('720x720')

    label=tk.Label(root,text = "Enter the expression:",font = ("Calibre Bold",15))
    label.grid(column=1,row=1)

    entry_string = tk.StringVar()
    entry = tk.Entry(root,width = 50,textvariable=entry_string)
    entry.grid(column=2,row=1)
    entry.focus()

    btn = tk.Button(root,text = "Start",command=lambda:on_click(root,entry_string),font=("Arial Bold",15))
    btn.grid(column=2,row=2)

    root.mainloop()

main()