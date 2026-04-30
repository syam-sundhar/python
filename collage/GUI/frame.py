import tkinter as tk
root=tk.Tk()
root.title("hi all")
frame=tk.Frame(root)
frame.pack()
label=tk.Label(frame,text="inside frame ")
label.pack()
root.mainloop()