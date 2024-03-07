from tkinter import *
import os
from tkinter import messagebox
f=Tk()
f.configure(background="black")
f.title("Offline")
f.geometry("850x500")
canvas_width=850
canvas_height=500
canvas=Canvas(f,width=canvas_width,height=canvas_height,bg="#b5d9f7")
canvas.place(x=0,y=0)
#img=PhotoImage(file="book.png")
#canvas.create_image(1,1,anchor=NW,image=img)


def ser():

    ER=SR.get()   # input from search box
    import re
    print(ER)
    file = open("constitution.txt", "r",encoding="utf8")
    
    s=0
    for each in file:
    
        x=re.findall(ER,each)  
        if (x):
           # print("Yes! match found")
            s=s+1
        else:
            b=0
           # print("No match")
    print(s)
    if(s==0):
        messagebox.showinfo("Results","Search Unsccessfull!")
    else:
        messagebox.showinfo("Results","Yes Search has been found! ")



def con():
    #os.system("const.py")
    f.destroy()
    import Offioc
    
    
def dep():
    f.destroy()
    os.system("main.py")

def qui():
    messagebox.showinfo("CREDITS","This Demo version of Samvidhan is sponsored by Soumya Pradhan,Abhishek Ojha, Shubham Mishra \n Original work is in progress and would be soon available for public use.")
    f.destroy()


logoimage=PhotoImage(file='logo.png')
icon=Label(image=logoimage)
icon.place(x=200,y=10,width=391,height=131)

Label(f,text="Enter known key words to check your knowledge (Refer to the instructions below)",fg="Black",bg="#b5d9f7",font="Book_Antiqua 12 bold italic").place(x=10,y=120)
Label(f,text="* Keep a definate word limit ",fg="red",bg="#b5d9f7",font="Book_Antiqua 10 bold italic").place(x=10,y=142)
Label(f,text="* Accurate words ",fg="red",bg="#b5d9f7",font="Book_Antiqua 10 bold italic").place(x=10,y=165)
Label(f,text="* Article number with proper statement ",fg="red",bg="#b5d9f7",font="Book_Antiqua 10 bold italic").place(x=10,y=185)

SR=StringVar()
Label(f,text="Search Phase",fg="Black",bg="#b5d9f7",font="Book_Antiqua 15 bold italic").place(x=10,y=230)
e1=Entry(f,textvariable = SR,width=50,fg="Red",font="Comissansms 13 italic").place(x=200,y=230)


b1=Button(f,text="Search",fg="white",bg="blue",width=14,bd=3,command=ser)
b1.place(x=700,y=230)

Label(f,text="If you are interested in Reading the whole thing Click on the button just below",fg="Dark Green",bg="#b5d9f7",font="Book_Antiqua 12 bold italic").place(x=10,y=270)

b2=Button(f,text="Constitution of India",width=30,bd=3,bg="blue",fg="white",command=con)
b2.place(x=350,y=310)


b5=Button(f,text="Back",width=10,bd=3,bg="Black",fg="white",command=dep)
b5.place(x=10,y=460)
b6=Button(f,text="Quit",fg="white",bg="Black",width=16,bd=3,command=qui)
b6.place(x=700,y=460)

f.resizable(False,False)
f.mainloop()
