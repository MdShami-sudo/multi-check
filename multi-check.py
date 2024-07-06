import tkinter as tk
from tkinter import ttk

def checkbox_changed(checkbox_name):
    if checkbox_states[checkbox_name].get() == 1:
        lbl_status.config(text=f"{checkbox_name} is checked!")
    else:
        lbl_status.config(text=f"{checkbox_name} is unchecked.")

def create_gradient_background(parent, color1, color2):
    style = ttk.Style()
    style.theme_create("gradient", parent="alt", settings={
        "TFrame": {
            "configure": {"background": f"linear gradient {color1} {color2}"},
        }
    })
    style.theme_use("gradient")
    frame = ttk.Frame(parent, style="TFrame")
    frame.place(relwidth=1, relheight=1)

    return frame

root = tk.Tk()
root.title("Multi Checkbox Example")

gradient_frame = create_gradient_background(root, "#FFC0CB", "#FFFF00")

checkbox_states = {}

checkbox_names = ["Checkbox 1", "Checkbox 2", "Checkbox 3"]

for name in checkbox_names:
    checkbox_states[name] = tk.IntVar()
    chk = ttk.Checkbutton(gradient_frame, text=name, variable=checkbox_states[name], command=lambda n=name: checkbox_changed(n))
    chk.pack(padx=20, pady=10, anchor="w")

lbl_status = ttk.Label(gradient_frame, text="")
lbl_status.pack(pady=10)

root.mainloop()
