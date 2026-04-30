import tkinter as tk

def login():
    username = entry_user.get()
    password = entry_pass.get()
    print("Username:", username)
    print("Password:", password)

root = tk.Tk()
root.geometry("300x200")
tk.Label(root, text="Username:").grid(row=0,column=1)
entry_user = tk.Entry(root)
entry_user.grid(row=0,column=3)

tk.Label(root, text="Password:").grid(row=1,column=1)
entry_pass = tk.Entry(root, show="*")
entry_pass.grid(row=1,column=3)

tk.Button(root, text="Login", command=login).grid(row=3,column=3)
root.mainloop()