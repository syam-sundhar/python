import tkinter as tk

root=tk.Tk()
root.title("hi all")
root.geometry("300x200")

#entry the data
entry=tk.Entry(root)
entry.pack()

#click button
def click(en):
    print(en)

button=tk.Button(root,text="click",command=click(entry))
button.pack()

#radio button 
radio1=tk.Radiobutton(root,text="option 1",value=1)
radio2=tk.Radiobutton(root,text="option 2",value=2)
radio1.pack()
radio2.pack()

root.mainloop()