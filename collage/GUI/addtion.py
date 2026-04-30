import tkinter as tk

#function to ass numbers
def add():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1+num2
    result_l.config(text="Result: "+str(result))

#create window
root=tk.Tk()
root.title("addition of two numbers")
root.geometry("300x200")

#label and entry boxes
label1=tk.Label(root,text="enter first number: ")
label1.pack()

entry1=tk.Entry(root)
entry1.pack()

label2=tk.Label(root,text="enter second number: ")
label2.pack()

entry2=tk.Entry(root)
entry2.pack()

#button
add_button=tk.Button(root,text="ADD",command=add)
add_button.pack()

#result
result_l=tk.Label(root)
result_l.pack()

root.mainloop()