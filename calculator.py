from tkinter import *
from math import *
from tkinter import messagebox

root = Tk()

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="634@Akhil", database="calculator123")
mycursor = mydb.cursor()
# mycursor.execute("create database calculator123")
# mycursor.execute("create table storevalues(value varchar(20))")
root.iconbitmap("C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\icon.ico")
root.title("Scientific Calculator")
root.geometry("290x380")
root.config(bg="#9e9b99")
root.resizable(height=FALSE, width=FALSE)
f1 = Frame(root, width=592, height=1, relief=SUNKEN)
f1.grid(row=0, column=0, sticky="nsew")


####################################

def scientific():
    root.resizable(height=FALSE, width=FALSE)
    root.geometry("592x370")


def default():
    root.resizable(height=FALSE, width=FALSE)
    root.geometry("290x370")


def exitcalci():
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')

    #########################


# mb=Menubutton(f1,text="Mode",bg="white")
# mb.menu=Menu(mb)
# mb["menu"]=mb.menu

# mb.menu.add_command(label="SCIENTIFIC",command=scientific)
# mb.grid(sticky="nsew")
# root.configure(menu=mb)
menubar = Menu(f1)  # name of main menu is menubar
filemenu = Menu(menubar, tearoff=0)  # we are creating submenu named filemenu
filemenu.add_command(label="Default", command=default)  # we are adding commands to submenu
filemenu.add_command(label="Scientific", command=scientific)
filemenu.add_command(label="Exit", command=exitcalci)
filemenu.add_separator()
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

############################
f2 = Frame(root, width=592, height=10, relief=SUNKEN, bg="#9e9b99")
f2.grid(row=1, column=0, sticky="nsew")
result = Entry(f2, highlightthickness=3, width=21)
result.grid(row=0, column=0, padx=4)
# resultwindow.place(x=0,y=0)
result.config(font=("Arial", 18), highlightcolor="black")
result.focus_set()  # Sets focus on the input text area

f3 = Frame(root, width=592, height=320, relief=SUNKEN, bg="#9e9b99")
f3.grid(row=2, column=0, sticky="nsew")


def ins(val):
    result.insert(END, val)


def cancel():
    result.delete(0, 'end')


def delete_all():
    x = result.get()
    result.delete(0, 'end')
    y = x[:-1]
    result.insert(0, y)


def calculate():
    mycursor = mydb.cursor()
    x = result.get()
    answer = eval(x)
    result.delete(0, 'end')
    result.insert(0, answer)
    mycursor.execute("insert into storevalues(value) values (%s)", (result.get(),))
    mydb.commit()


how = 0


def previous():
    global how
    how += 1
    mycursor = mydb.cursor()
    mycursor.execute("select * from storevalues")
    inss = mycursor.fetchall()
    result.delete(0, 'end')
    count = 0
    for i in inss:
        count += 1
    try:
        result.insert(0, inss[count - how])
    except IndexError:
        how = 0
        result.insert(0, "Pre values limit reached!!")

    mydb.commit()


######################
one = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\one.png").subsample(12, 12)

button1 = Button(f3, image=one, compound=CENTER, command=lambda: ins('1'))
button1.grid(row=0, column=0, padx=3, pady=3, )

two = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\two.png").subsample(12, 12)
button2 = Button(f3, image=two, compound=CENTER, command=lambda: ins('2'))
button2.grid(row=0, column=1, padx=3, pady=3)
button2.config(font=("Arial", 18))

three = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\three.png").subsample(12, 12)
button3 = Button(f3, image=three, compound=CENTER, command=lambda: ins('3'))
button3.grid(row=0, column=2, padx=3, pady=3)
button3.config(font=("Arial", 18))

four = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\four.png").subsample(12, 12)
button4 = Button(f3, image=four, command=lambda: ins('4'))
button4.grid(row=1, column=0, padx=3, pady=3)
button4.config(font=("Arial", 18))

five = PhotoImage(file="C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\five.png").subsample(12, 12)
button5 = Button(f3, image=five, compound=CENTER, command=lambda: ins('5'))
button5.grid(row=1, column=1, padx=3, pady=3)
button5.config(font=("Arial", 18))

six = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\six.png").subsample(12, 12)
button6 = Button(f3, image=six, compound=CENTER, command=lambda: ins('6'))
button6.grid(row=1, column=2, padx=3, pady=3)
button6.config(font=("Arial", 18))

seven = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\seven.png").subsample(12, 12)
button7 = Button(f3, image=seven, command=lambda: ins('7'))
button7.grid(row=2, column=0, padx=3, pady=3)
button7.config(font=("Arial", 18))

eight = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\eight.png").subsample(12, 12)
button8 = Button(f3, text="8", image=eight, command=lambda: ins('8'))
button8.grid(row=2, column=1, padx=3, pady=3)
button8.config(font=("Arial", 18))

nine = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\nine.png").subsample(12, 12)
button9 = Button(f3, image=nine, command=lambda: ins('9'))
button9.grid(row=2, column=2, padx=3, pady=3)
button9.config(font=("Arial", 18))

zero = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\zero.png").subsample(12, 12)
button0 = Button(f3, image=zero, compound=CENTER, command=lambda: ins('0'))
button0.grid(row=3, column=0, padx=3, pady=3)
button0.config(font=("Arial", 18))

dot = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\dot.png").subsample(12, 12)
buttondot = Button(f3, image=dot, compound=CENTER, command=lambda: ins('.'))
buttondot.grid(row=3, column=1, padx=3, pady=3)
buttondot.config(font=("Arial", 18))

button_open = Button(f3, text="(", fg="blue", width=3, command=lambda: ins('('))
button_open.grid(row=3, column=2, padx=3, pady=3)
button_open.config(font=("Arial", 18))

button_close = Button(f3, text=")", width=3, fg="blue", command=lambda: ins(')'))
button_close.grid(row=3, column=3, padx=3, pady=3)
button_close.config(font=("Arial", 18))

# Operations Buttons
plus = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\plus.png").subsample(5, 5)
buttonplus = Button(f3, image=plus, compound=CENTER, command=lambda: ins('+'))
buttonplus.grid(row=0, column=3, padx=3, pady=3)
buttonplus.config(font=("Arial", 18))

minus = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\minus.png").subsample(11, 11)
buttonminus = Button(f3, image=minus, command=lambda: ins('-'))
buttonminus.grid(row=0, column=4, padx=3, pady=3)
buttonminus.config(font=("Arial", 18))

div = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\div.png").subsample(11, 11)
buttondivide = Button(f3, image=div, command=lambda: ins('/'))
buttondivide.grid(row=1, column=3, padx=3, pady=3)
buttondivide.config(font=("Arial", 18))

mul = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\mul.png").subsample(11, 11)
buttonmultiply = Button(f3, image=mul, command=lambda: ins('*'))
buttonmultiply.grid(row=1, column=4, padx=3, pady=3)
buttonmultiply.config(font=("Arial", 18))

power = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\power.png").subsample(5, 5)
buttonpower = Button(f3, image=power, command=lambda: ins('**'))
buttonpower.grid(row=2, column=4, padx=3, pady=3)
buttonpower.config(font=("Arial", 18))

mod = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\mod.png").subsample(11, 11)
buttonroot = Button(f3, image=mod, command=lambda: ins('%'))  # problem in this one "%" is being considered as modulus.
buttonroot.grid(row=2, column=3, padx=3, pady=3)
buttonroot.config(font=("Arial", 18))

fact = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\fact.png").subsample(12, 12)
buttonfact = Button(f3, image=fact, command=lambda: ins('factorial('))
buttonfact.grid(row=3, column=4, padx=3, pady=3)
buttonfact.config(font=("Arial", 18))

##################
sqrt1 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\sqrt.png").subsample(20, 27)
buttonroot = Button(f2, image=sqrt1, command=lambda: ins('sqrt('))
buttonroot.grid(row=0, column=1, padx=5, pady=3)
buttonroot.config(font=("Arial", 18))

buttonrep = Button(f2, text="1/x", width=4, command=lambda: ins('1/'))
buttonrep.grid(row=0, column=2, padx=5, pady=3)
buttonrep.config(font=("Arial", 18))

log1 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\log.png").subsample(10, 12)
buttonlog = Button(f2, image=log1, command=lambda: ins('log('))
buttonlog.grid(row=0, column=3, padx=5, pady=3)
buttonlog.config(font=("Arial", 18))

pi1 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\pi.png").subsample(8, 12)
buttonpi = Button(f2, image=pi1, command=lambda: ins('pi'))
buttonpi.grid(row=0, column=4, padx=3, pady=3)
buttonpi.config(font=("Arial", 18))

# label = Label(f2, text="Unit Convertor",bg="#636b29",fg="#ffffff")
# label.grid(row=0, column=5, padx=3, pady=3,)
# label.config(font=("Arial", 33))

tan1 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\tan.png").subsample(9, 12)
buttontan = Button(f3, image=tan1, command=lambda: ins('tan('))
buttontan.grid(row=0, column=5, padx=3, pady=3)
buttontan.config(font=("Arial", 18))

sin1 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\sin.png").subsample(3, 4)
buttonsin = Button(f3, image=sin1, command=lambda: ins('sin('))
buttonsin.grid(row=0, column=6, padx=3, pady=3)
buttonsin.config(font=("Arial", 18))

cos1 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\cos.png").subsample(4, 5)
buttoncos = Button(f3, image=cos1, command=lambda: ins('cos('))
buttoncos.grid(row=0, column=7, padx=3, pady=3)
buttoncos.config(font=("Arial", 18))

sqr = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\sqr.png").subsample(18, 25)
buttonsqr = Button(f3, image=sqr, command=lambda: ins('**2'))
buttonsqr.grid(row=0, column=8, padx=3, pady=3)
buttonsqr.config(font=("Arial", 18))

###########
# atan=PhotoImage(file=r"C:\\Users\Hp\\Desktop\\jassipy\\atan.png").subsample(4,5)
buttonatan = Button(f3, text="atan", command=lambda: ins('atan('))
buttonatan.grid(row=1, column=5, padx=3, pady=3)
buttonatan.config(font=("Arial", 18))

buttonasin = Button(f3, text="asin", command=lambda: ins('asin('))
buttonasin.grid(row=1, column=6, padx=3, pady=3)
buttonasin.config(font=("Arial", 18))

buttonacos = Button(f3, text="acos", command=lambda: ins('acos('))
buttonacos.grid(row=1, column=7, padx=3, pady=3)
buttonacos.config(font=("Arial", 18))

buttonsec = Button(f3, text="sec", width=4, command=lambda: ins('sec('))
buttonsec.grid(row=1, column=8, padx=3, pady=3)
buttonsec.config(font=("Arial", 18))

exp1 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\exp.png").subsample(4, 5)
buttoncot = Button(f3, image=exp1, command=lambda: ins('exp('))
buttoncot.grid(row=2, column=5, padx=3, pady=3)
buttoncot.config(font=("Arial", 18))

floor1 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\floor.png").subsample(5, 4)
buttonfloor = Button(f3, image=floor1, command=lambda: ins('floor('))
buttonfloor.grid(row=2, column=6, padx=3, pady=3)
buttonfloor.config(font=("Arial", 18))

buttonceil = Button(f3, text="ceil", width=4, command=lambda: ins('ceil('))
buttonceil.grid(row=2, column=7, padx=3, pady=3)
buttonceil.config(font=("Arial", 18))

absu = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\absu.png").subsample(20, 20)
buttonabs = Button(f3, image=absu, command=lambda: ins('abs('))
buttonabs.grid(row=2, column=8, padx=3, pady=3)
buttonabs.config(font=("Arial", 18))

com = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\com.png").subsample(4, 5)
buttonfact = Button(f3, image=com, command=lambda: ins(','))
buttonfact.grid(row=3, column=5, padx=3, pady=3)
buttonfact.config(font=("Arial", 18))

gcd1 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\gcd.png").subsample(5, 8)
buttongcd = Button(f3, image=gcd1, command=lambda: ins('gcd'))
buttongcd.grid(row=3, column=6, padx=5, pady=3)
buttongcd.config(font=("Arial", 18))

deg = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\deg.png").subsample(8, 9)
buttondeg = Button(f3, image=deg, command=lambda: ins('degrees('))
buttondeg.grid(row=3, column=7, padx=5, pady=3)
buttondeg.config(font=("Arial", 18))

rad = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\rad.png").subsample(5, 5)
buttonrad = Button(f3, image=rad, command=lambda: ins('radians('))
buttonrad.grid(row=3, column=8, padx=5, pady=3)
buttonrad.config(font=("Arial", 18))

buttonlog2 = Button(f3, text="log2", width=4, bg="white", command=lambda: ins('log2('))
buttonlog2.grid(row=4, column=5, padx=5, pady=3)
buttonlog2.config(font=("Arial", 18))

powe = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\pow.png").subsample(4, 5)
buttonpow = Button(f3, image=powe, command=lambda: ins('pow('))
buttonpow.grid(row=4, column=6, padx=5, pady=3)
buttonpow.config(font=("Arial", 18))

mod2 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\mod2.png").subsample(4, 5)
buttonmod = Button(f3, image=mod2, command=lambda: ins('remainder('))
buttonmod.grid(row=4, column=7, padx=5, pady=3)
buttonmod.config(font=("Arial", 18))

buttonfabs = Button(f3, text="fabs", width=4, bg="white", command=lambda: ins('fabs('))
buttonfabs.grid(row=4, column=8, padx=5, pady=3)
buttonfabs.config(font=("Arial", 18))
####################

c = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\c.png").subsample(11, 11)
buttoncancel = Button(f3, image=c, command=lambda: cancel())
buttoncancel.grid(row=4, column=2, padx=3, pady=3)
# buttoncancel.place(x=4,y=250)
buttoncancel.config(font=("Arial", 18))

del1 = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\del1.png").subsample(11, 11)
buttondeleteall = Button(f3, image=del1, command=lambda: delete_all())
buttondeleteall.grid(row=4, column=3, padx=3, pady=3)
# buttondeleteall.place(x=94,y=250)
buttondeleteall.config(font=("Arial", 18))

pre = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\pre.png").subsample(11, 11)
buttonpre = Button(f3, image=pre, command=previous)
buttonpre.grid(row=4, column=4, padx=3, pady=3)
# buttonpre.place(x=184,y=250)
buttonpre.config(font=("Arial", 18))

equ = PhotoImage(file=r"C:\\Users\\akhil\\OneDrive\\Desktop\\scientific\\equ.png").subsample(5, 11)
buttonresult = Button(f3, image=equ, command=lambda: calculate())
# buttonresult.grid(row=7, column=0, padx=3, pady=3,)
buttonresult.place(x=3, y=245)
buttonresult.config(font=("Arial", 18))
################################

########################
root.mainloop()
