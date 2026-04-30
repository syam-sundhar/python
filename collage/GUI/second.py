import tkinter as tk

root=tk.Tk()
root.title("hi all")
root.geometry("300x200")

#entry the data
entry=tk.Entry(root)
entry.pack()

#click button
def click():
    b=entry.get()
    print("button clicked! by ",b)

button=tk.Button(root,text="click",command=click())
button.pack()

#radio button
radio1=tk.Radiobutton(root,text="option 1",value=1)
radio2=tk.Radiobutton(root,text="option 2",value=2)
radio1.pack()
radio2.pack()

#check button


"""#rows and coloumns
entry1=tk.Entry(root)
entry1.grid(row=1,column=3)
entry2=tk.Entry(root)
entry2.grid(row=0,column=1)"""

root.mainloop()