from tkinter import *
import os
from tkinter import messagebox
f=Tk()
f.configure(background="black")
f.title("Constitution of India")
f.geometry("850x500")


wtext=Text(f,height=500, width=850)
#sc=Scrollbar(f,orient=VERTICAL,command=wtext.xview).pack(side=RIGHT,fill=Y)

file=open("constitution.txt","r",encoding="utf8")
c=file.read()

wtext.insert(END,c)



wtext.pack()
f.resizable(False,False)
f.mainloop()