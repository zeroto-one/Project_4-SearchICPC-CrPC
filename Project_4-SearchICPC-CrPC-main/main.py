from tkinter import *
import os
def Onwindow():
    mroot.destroy()
    os.system("Onwindow.py")

def Offwindow():
    mroot.destroy()
    os.system("Offwindow.py")
mroot = Tk()
mroot.title('Samvidhan')
mroot.geometry("800x700")
mroot.configure(background='#b5d9f7')

logoimage1=PhotoImage(file='logo.png')
icon1=Label(image=logoimage1)
icon1.place(x=200,y=30,width=391,height=131)

b1=Button(mroot, text='Go Offline', width=25,height=2, bg='white', fg='blue',relief='solid', activebackground='red', activeforeground='white',command=Offwindow) 
b2=Button(mroot, text='Explore Online', width=25, height=2, bg='white', fg='blue',relief='solid', activebackground='red', activeforeground='white',command=Onwindow) 
b1.place(x=20,y=250) 
b2.place(x=20,y=320)

srcimg=PhotoImage(file='img.png')
imga=Label(image=srcimg)
imga.place(x=250,y=200)

factslabel=Label(mroot,text='Facts:',font=("Cascadia Mono SemiBold",8,'bold')).place(x=20,y=380)
facts=Text(mroot,wrap=WORD,bg='#f5f8fa',fg='black',relief='solid',font=("Arial",10))
facts.place(x=20,y=400,height=200,width=200)
arr=["[1]. COI was handwritten by Prem Behari Narain Raizada\n\n","[2]. Our Constitution is the longest Constitution in the world\n\n", "[3].26 January 1950: The National Emblem of India Was Adopted','COI Amended Only 104 Times since 1950"]
for i in arr:
    facts.insert(INSERT,i)

mroot.resizable(False,False)
mroot.mainloop()