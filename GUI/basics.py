import tkinter as tk
root = tk.Tk()

root.title("My First App")

root.geometry("400x300")

label = tk.Label(root, text = "AAAAAAAAAAAA!")
label.place(x=150, y=130)

button = tk.Button(root, text="Click Me", command = lambda: label.config(text="Button Clicked!"))
button.place(x=110, y= 80)

root.mainloop()