from tkinter import *
value=""
def operate(num):
    global value
    value=value+str(num)
    s.set(value)

def equalpress():
    try:
        global value
        total=str(eval(value))
        s.set(total)
        value=""

    except :
        s.set("Error")
        value=""

def clear():
    global value
    value=""
    s.set("")

if __name__ == '__main__':
    root=Tk()
    root.geometry("444x500")
    root.maxsize(444,500)
    root.option_add('*Font','arial 20 bold')
    root.title("CALCULATOR-Sukalyan Adhikary")
    root.wm_iconbitmap("12.ico")
    root.configure(background="white")

    s=StringVar()
    s.set(" ")
    display=Entry(root,relief=RIDGE,textvariable=s,justify='left',bd=30,bg='grey',font="arial 30 bold")
    display.pack(side=TOP,expand=YES,fill=BOTH)


    f=Frame(root)
    button1 = Button(f, text=' + ', fg='white', bg='red', height=1,bd=5, width=4,command=lambda :operate('+'))
    button1.pack(side=LEFT)


    button1 = Button(f, text=' - ', fg='white', bg='red', height=1, bd=5, width=4,command=lambda :operate('-'))
    button1.pack(side=LEFT)


    button1 = Button(f, text=' *', fg='white', bg='red', height=1,bd=5, width=4,command=lambda :operate('*'))
    button1.pack(side=LEFT)


    button1 = Button(f, text=' /', fg='white', bg='red', height=1, bd=5, width=4,command=lambda :operate('/'))
    button1.pack(side=LEFT)


    button1 = Button(f, text=' C', fg='White', bg='blue' ,height=1,bd=5, width=6,command=clear)
    button1.pack(side=LEFT)

    f.pack()


    f = Frame(root)
    button1 = Button(f, text=' 9 ', fg='white', bg='black', height=1,bd=5, width=8,command=lambda :operate('9'))
    button1.pack(side=LEFT)


    button1 = Button(f, text=' 8 ', fg='white', bg='black', height=1,bd=5, width=8,command=lambda :operate('8'))
    button1.pack(side=LEFT)


    button1 = Button(f, text=' 7 ', fg='white', bg='black', height=1,bd=5, width=8,command=lambda :operate('7'))
    button1.pack(side=LEFT)

    f.pack()

    f = Frame(root)
    button1 = Button(f, text=' 6 ', fg='white', bg='black', height=1,bd=5, width=8,command=lambda :operate('6'))
    button1.pack(side=LEFT)


    button1 = Button(f, text=' 5 ', fg='white', bg='black', height=1,bd=5, width=8,command=lambda :operate('5'))
    button1.pack(side=LEFT)

    button1 = Button(f, text=' 4 ', fg='white', bg='black', height=1,bd=5, width=8,command=lambda :operate('4'))
    button1.pack(side=LEFT)

    f.pack()

    f = Frame(root)
    button1 = Button(f, text=' 3 ', fg='white', bg='black', height=1,bd=5, width=8,command=lambda :operate('3'))
    button1.pack(side=LEFT)


    button1 = Button(f, text=' 2 ', fg='white', bg='black', height=1,bd=5, width=8,command=lambda :operate('2'))
    button1.pack(side=LEFT)


    button1 = Button(f, text=' 1 ', fg='white', bg='black', height=1,bd=5, width=8,command=lambda :operate('1'))
    button1.pack(side=LEFT)

    f.pack()

    f = Frame(root)
    button1 = Button(f, text=' 00 ', fg='white', bg='black', height=1, bd=5, width=6,command=lambda :operate('00'))
    button1.pack(side=LEFT)

    button1 = Button(f, text=' .', fg='white', bg='black', height=1, bd=5, width=6,command=lambda :operate('.'))
    button1.pack(side=LEFT)

    button1 = Button(f, text=' 0 ', fg='white', bg='black', height=1, bd=5, width=12,command=lambda :operate('0'))
    button1.pack(side=LEFT)

    f.pack()

    f=Frame(root)
    button1=Button(f,text="=",fg='white',bg='orange',height=1,width=25,bd=5,command=equalpress)
    button1.pack()

    f.pack(fill=Y)

    root.mainloop()

