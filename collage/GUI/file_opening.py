import tkinter as tk
from tkinter import filedialog as fd

def file_opening():
    file_path=fd.askopenfilename()
    if file_path:
        try :
            with open(file_path,"r") as f:
                content=f.read()
                text_box.delete(1.0,tk.END)
                text_box.insert(tk.END,content)
        except FileNotFoundError as e:
            print("file not found! ",e)

root=tk.Tk()
root.title("file opener")

but=tk.Button(root,text="select file",command=file_opening)
but.pack()

text_box=tk.Text(root,height=20,width=60)
text_box.pack()
root.mainloop()