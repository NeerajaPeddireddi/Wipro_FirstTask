import tkinter
root=tkinter.Tk()
root.title("Hello World")
lbl=tkinter.Label(root,text="Enter text")
lbl.grid(row=0,column=0)
entry=tkinter.Entry(root)
entry.grid(row=0,column=1)
def click():
    print("Banana")
btn=tkinter.Button(root,text="Submit",command=click)

btn.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
var=tkinter.StringVar()
options=["apple","banana","mango"]
menu=tkinter.OptionMenu(root,var,*options)
menu.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
#To set default value
var.set("apple")
root.mainloop()
