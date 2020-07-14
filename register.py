from datetime import *
from tkinter import *
from tkinter.ttk import Combobox
from  tkinter import StringVar
import time;
import tkinter.messagebox
import openpyxl
root1 = Tk()
root1.resizable(0,0)
root1.title("Student Attendance Register")
root1.iconbitmap(r"attendance.ico")
width = root1.winfo_screenwidth()
height = root1.winfo_screenheight()
root1.geometry("%dx%d+0+0" % (width, height))
wb = openpyxl.load_workbook("student management system.xlsx")
sheet = wb.active
def save():
    v1 = a4.get()
    v2 = b4.get()
    v3 = c4.get()
    v4 = d4.get()
    v5 = e4.get()
    v6 = f4.get()
    v7 = g4.get()
    v8 = h4.get()
    v9 = i4.get()
    v10 = j4.get()
    v11 = k4.get()
    v12 = l4.get()
    v13 = m4.get()
    s = date.get()
    if s == "4/10/20":
        sheet["D2"] = date.get()
        sheet['D3'] = v1
        sheet['D4'] = v2
        sheet['D5'] = v3
        sheet['D6'] = v4
        sheet['D7'] = v5
        sheet['D8'] = v6
        sheet['D9'] = v7
        sheet['D10'] = v8
        sheet['D11'] = v9
        sheet['D12'] = v10
        sheet['D13'] = v11
        sheet['D14'] = v12
        sheet['D15'] = v13
    elif s == "11/10/20":
        sheet["E2"] = date.get()
        sheet['E3'] = v1
        sheet['E4'] = v2
        sheet['E5'] = v3
        sheet['E6'] = v4
        sheet['E7'] = v5
        sheet['E8'] = v6
        sheet['E9'] = v7
        sheet['E10'] = v8
        sheet['E11'] = v9
        sheet['E12'] = v10
        sheet['E13'] = v11
        sheet['E14'] = v12
        sheet['E15'] = v13
    elif s == "18/10/20":
        sheet["F2"] = date.get()
        sheet['F3'] = v1
        sheet['F4'] = v2
        sheet['F5'] = v3
        sheet['F6'] = v4
        sheet['F7'] = v5
        sheet['F8'] = v6
        sheet['F9'] = v7
        sheet['F10'] = v8
        sheet['F11'] = v9
        sheet['F12'] = v10
        sheet['F13'] = v11
        sheet['F14'] = v12
        sheet['F15'] = v13
    elif s == "25/10/20":
        sheet["G2"] = date.get()
        sheet['G3'] = v1
        sheet['G4'] = v2
        sheet['G5'] = v3
        sheet['G6'] = v4
        sheet['G7'] = v5
        sheet['G8'] = v6
        sheet['G9'] = v7
        sheet['G10'] = v8
        sheet['G11'] = v9
        sheet['G12'] = v10
        sheet['G13'] = v11
        sheet['G14'] = v12
        sheet['G15'] = v13
    elif s == "1/11/20":
        sheet["H2"] = date.get()
        sheet['H3'] = v1
        sheet['H4'] = v2
        sheet['H5'] = v3
        sheet['H6'] = v4
        sheet['H7'] = v5
        sheet['H8'] = v6
        sheet['H9'] = v7
        sheet['H10'] = v8
        sheet['H11'] = v9
        sheet['H12'] = v10
        sheet['H13'] = v11
        sheet['H14'] = v12
        sheet['H15'] = v13
    elif s == "8/11/20":
        sheet["I2"] = date.get()
        sheet['I3'] = v1
        sheet['I4'] = v2
        sheet['I5'] = v3
        sheet['I6'] = v4
        sheet['I7'] = v5
        sheet['I8'] = v6
        sheet['I9'] = v7
        sheet['I10'] = v8
        sheet['I11'] = v9
        sheet['I12'] = v10
        sheet['I13'] = v11
        sheet['I14'] = v12
        sheet['I15'] = v13
    elif s == "15/11/20":
        sheet["J2"] = date.get()
        sheet['J3'] = v1
        sheet['J4'] = v2
        sheet['J5'] = v3
        sheet['J6'] = v4
        sheet['J7'] = v5
        sheet['J8'] = v6
        sheet['J9'] = v7
        sheet['J10'] = v8
        sheet['J11'] = v9
        sheet['J12'] = v10
        sheet['J13'] = v11
        sheet['J14'] = v12
        sheet['J15'] = v13
    elif s == "22/11/20":
        sheet["K2"] = date.get()
        sheet['K3'] = v1
        sheet['K4'] = v2
        sheet['K5'] = v3
        sheet['K6'] = v4
        sheet['K7'] = v5
        sheet['K8'] = v6
        sheet['K9'] = v7
        sheet['K10'] = v8
        sheet['K11'] = v9
        sheet['K12'] = v10
        sheet['K13'] = v11
        sheet['K14'] = v12
        sheet['K15'] = v13
    elif s == "29/11/20":
        sheet["L2"] = date.get()
        sheet['L3'] = v1
        sheet['L4'] = v2
        sheet['L5'] = v3
        sheet['L6'] = v4
        sheet['L7'] = v5
        sheet['L8'] = v6
        sheet['L9'] = v7
        sheet['L10'] = v8
        sheet['L11'] = v9
        sheet['L12'] = v10
        sheet['L13'] = v11
        sheet['L14'] = v12
        sheet['L15'] = v13
    elif s == "6/12/20":
        sheet["M2"] = date.get()
        sheet['M3'] = v1
        sheet['M4'] = v2
        sheet['M5'] = v3
        sheet['M6'] = v4
        sheet['M7'] = v5
        sheet['M8'] = v6
        sheet['M9'] = v7
        sheet['M10'] = v8
        sheet['M11'] = v9
        sheet['M12'] = v10
        sheet['M13'] = v11
        sheet['M14'] = v12
        sheet['M15'] = v13
    elif s == "13/12/20":
        sheet["N2"] = date.get()
        sheet['N3'] = v1
        sheet['N4'] = v2
        sheet['N5'] = v3
        sheet['N6'] = v4
        sheet['N7'] = v5
        sheet['N8'] = v6
        sheet['N9'] = v7
        sheet['N10'] = v8
        sheet['N11'] = v9
        sheet['N12'] = v10
        sheet['N13'] = v11
        sheet['N14'] = v12
        sheet['N15'] = v13
    elif s == "20/12/20":
        sheet["O2"] = date.get()
        sheet['O3'] = v1
        sheet['O4'] = v2
        sheet['O5'] = v3
        sheet['O6'] = v4
        sheet['O7'] = v5
        sheet['O8'] = v6
        sheet['O9'] = v7
        sheet['O10'] = v8
        sheet['O11'] = v9
        sheet['O12'] = v10
        sheet['O13'] = v11
        sheet['O14'] = v12
        sheet['O15'] = v13
    elif s == "27/12/20":
        sheet["P2"] = date.get()
        sheet['P3'] = v1
        sheet['P4'] = v2
        sheet['P5'] = v3
        sheet['P6'] = v4
        sheet['P7'] = v5
        sheet['P8'] = v6
        sheet['P9'] = v7
        sheet['P10'] = v8
        sheet['P11'] = v9
        sheet['P12'] = v10
        sheet['P13'] = v11
        sheet['P14'] = v12
        sheet['P15'] = v13
    elif s == "3/1/21":
        sheet["Q2"] = date.get()
        sheet['Q3'] = v1
        sheet['Q4'] = v2
        sheet['Q5'] = v3
        sheet['Q6'] = v4
        sheet['Q7'] = v5
        sheet['Q8'] = v6
        sheet['Q9'] = v7
        sheet['Q10'] = v8
        sheet['Q11'] = v9
        sheet['Q12'] = v10
        sheet['Q13'] = v11
        sheet['Q14'] = v12
        sheet['Q15'] = v13
    elif s == "10/01/21":
        sheet["R2"] = date.get()
        sheet['R3'] = v1
        sheet['R4'] = v2
        sheet['R5'] = v3
        sheet['R6'] = v4
        sheet['R7'] = v5
        sheet['R8'] = v6
        sheet['R9'] = v7
        sheet['R10'] = v8
        sheet['R11'] = v9
        sheet['R12'] = v10
        sheet['R13'] = v11
        sheet['R14'] = v12
        sheet['R15'] = v13
    elif s == "17/01/21":
        sheet["S2"] = date.get()
        sheet['S3'] = v1
        sheet['S4'] = v2
        sheet['S5'] = v3
        sheet['S6'] = v4
        sheet['S7'] = v5
        sheet['S8'] = v6
        sheet['S9'] = v7
        sheet['S10'] = v8
        sheet['S11'] = v9
        sheet['S12'] = v10
        sheet['S13'] = v11
        sheet['S14'] = v12
        sheet['S15'] = v13
    elif s == "24/01/21":
        sheet["T2"] = date.get()
        sheet['T3'] = v1
        sheet['T4'] = v2
        sheet['T5'] = v3
        sheet['T6'] = v4
        sheet['T7'] = v5
        sheet['T8'] = v6
        sheet['T9'] = v7
        sheet['T10'] = v8
        sheet['T11'] = v9
        sheet['I12'] = v10
        sheet['I13'] = v11
        sheet['I14'] = v12
        sheet['I15'] = v13
    elif s == "31/01/21":
        sheet["U2"] = date.get()
        sheet['U3'] = v1
        sheet['U4'] = v2
        sheet['U5'] = v3
        sheet['U6'] = v4
        sheet['U7'] = v5
        sheet['U8'] = v6
        sheet['U9'] = v7
        sheet['U10'] = v8
        sheet['U11'] = v9
        sheet['U12'] = v10
        sheet['U13'] = v11
        sheet['U14'] = v12
        sheet['U15'] = v13
    elif s == "7/02/21":
        sheet["V2"] = date.get()
        sheet['V3'] = v1
        sheet['V4'] = v2
        sheet['V5'] = v3
        sheet['V6'] = v4
        sheet['V7'] = v5
        sheet['V8'] = v6
        sheet['V9'] = v7
        sheet['V10'] = v8
        sheet['V11'] = v9
        sheet['V12'] = v10
        sheet['V13'] = v11
        sheet['V14'] = v12
        sheet['V15'] = v13
    elif s == "14/02/21":
        sheet["W2"] = date.get()
        sheet['W3'] = v1
        sheet['W4'] = v2
        sheet['W5'] = v3
        sheet['W6'] = v4
        sheet['W7'] = v5
        sheet['W8'] = v6
        sheet['W9'] = v7
        sheet['W10'] = v8
        sheet['W11'] = v9
        sheet['W12'] = v10
        sheet['W13'] = v11
        sheet['W14'] = v12
        sheet['W15'] = v13
    elif s == "21/02/21":
        sheet["X2"] = date.get()
        sheet['X3'] = v1
        sheet['X4'] = v2
        sheet['X5'] = v3
        sheet['X6'] = v4
        sheet['X7'] = v5
        sheet['X8'] = v6
        sheet['X9'] = v7
        sheet['X10'] = v8
        sheet['X11'] = v9
        sheet['X12'] = v10
        sheet['X13'] = v11
        sheet['X14'] = v12
        sheet['X15'] = v13
    elif s == "28/02/21":
        sheet["Y2"] = date.get()
        sheet['Y3'] = v1
        sheet['Y4'] = v2
        sheet['Y5'] = v3
        sheet['Y6'] = v4
        sheet['Y7'] = v5
        sheet['Y8'] = v6
        sheet['Y9'] = v7
        sheet['Y10'] = v8
        sheet['Y11'] = v9
        sheet['Y12'] = v10
        sheet['Y13'] = v11
        sheet['Y14'] = v12
        sheet['Y15'] = v13
    wb.save("student management system.xlsx")
top1 = Frame(root1, width=1700, height=200, bg="black", relief="raise", bd=10)
top1.pack(side=TOP, fill=X)
image = Frame(root1, width=100, height=500, bg="black", relief="raise", bd=9)
image.pack(side=RIGHT, fill=Y)
top2 = Frame(root1, width=1600, height=200, bg="black", relief="raise", bd=8)
top2.pack(side=TOP, fill=X)
bottom1 = Frame(root1, relief="raise", width=900, height=500, bg="black", bd=8)
bottom1.pack(side=TOP, fill=X)
date = StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
value11 = StringVar()
value12 = StringVar()
value13 = StringVar()
def Rest():
    value1.set("Select")
    value2.set("Select")
    value3.set("Select")
    value4.set("Select")
    value5.set("Select")
    value6.set("Select")
    value7.set("Select")
    value8.set("Select")
    value9.set("Select")
    value10.set("Select")
    value11.set("Select")
    value12.set("Select")
    value13.set("Select")
c = Canvas(image, width=200, height=230, bg="black", bd=5)
c.grid(row=2, column=0, columnspan=2, padx=40)
imagem = PhotoImage(file="man.png")
c.create_image(105, 133, image=imagem)
Add = Button(image, width=5, height=1, text="Enter", font=("Times New Roman", 25), background='black', foreground='red',bd=10, command=save)
Add.grid(row=3, column=0, columnspan=2, padx=40)
image1 = PhotoImage(file="ravi.png")
def pc1(e):
    c.create_image(105, 133, image=image1)
    name["text"] = "MALLARAPU RAVIKIRAN GOUD"
image2 = PhotoImage(file="man.png")
def pc2(e):
    c.create_image(105, 133, image=image2)
    name["text"] = "ANKENAPALLY PRANAY"
image3 = PhotoImage(file="man.png")
def pc3(e):
    c.create_image(105, 133, image=image3)
    name["text"] = "YADLAPALLI AASHLESH"
image4 = PhotoImage(file="man.png")
def pc4(e):
    c.create_image(105, 133, image=image4)
    name["text"] = "MADINENI RAVITEJA"
image5 = PhotoImage(file="man.png")
def pc5(e):
    c.create_image(105, 133, image=image5)
    name["text"] = "TUPPELLI VIKIRANTH"
image6 = PhotoImage(file="man.png")
def pc6(e):
    c.create_image(105, 133, image=image6)
    name["text"] = "ANUGU SHIVANADH REDDY"
image7 = PhotoImage(file="man.png")
def pc7(e):
    c.create_image(105, 133, image=image7)
    name["text"] = "AGGIDI VIDYA SAGAR"
image8 = PhotoImage(file="man.png")
def pc8(e):
    c.create_image(105, 133, image=image8)
    name["text"] = "KASOJI SRAVANTH KUMAR"
image9 = PhotoImage(file="man.png")
def pc9(e):
    c.create_image(105, 133, image=image9)
    name["text"] = "THATTALA SAIKUMAR"
image10 = PhotoImage(file="man.png")
def pc10(e):
    c.create_image(105, 133, image=image10)
    name["text"] = "MOHAMMAD SOHAIL"
image11 = PhotoImage(file="man.png")
def pc11(e):
    c.create_image(105, 133, image=image11)
    name["text"] = "KASHETTI AJAY"
image12 = PhotoImage(file="man.png")
def pc12(e):
    c.create_image(105, 133, image=image12)
    name["text"] = "S P ANIKETH JAIN"
image13 = PhotoImage(file="man.png")
def pc13(e):
    c.create_image(105, 133, image=image13)
    name["text"] = "BADAVATH SANTHOSH"
L = Label(top1, text="Student Attendance Register",font=("Times New Roman", 30) , background='black', foreground='white')
L.pack(side=LEFT)
date.set(time.strftime("%d/%m/%y"))
Date = Label(top1, font=('Times New Roman', 20, 'bold'), background='black', foreground='white', textvariable=date)
Date.pack(side=RIGHT)

L1 = Label(top2, text="SL.No", font=("Times New Roman", 25), background='black', foreground='red', bd=10).grid(row=0,column=0,padx=60,sticky=W)
L2 = Label(top2, text="Roll.No", font=("Times New Roman", 25), background='black', foreground='red', bd=10).grid(row=0,column=1,padx=30,sticky=W)
L3 = Label(top2, text="Student Name", font=("Times New Roman", 25), background='black', foreground='red', bd=10).grid(row=0, column=2, padx=80, sticky=W)
L4 = Label(top2, text="Attendance", font=("Times New Roman", 25), background='black', foreground='red', bd=10).grid(row=0, column=3, padx=60, sticky=W)

a1 = Label(bottom1, text="1", font=("Times New Roman", 15), background='black', foreground='white').grid(row=0,column=0,padx=10,pady=12)
a2 = Label(bottom1, text="17AG1A001", font=("Times New Roman", 15), background='BLACK', foreground='WHITE', width=15).grid(row=0, column=1, padx=60, pady=12)
a3 = Label(bottom1, text="MALLARAPU RAVIKIRAN GOUD", font=("Times New Roman", 15), background='BLACK',foreground='WHITE', width=27, anchor=W)
a3.bind("<Enter>", pc1)
a3.grid(row=0, column=2, padx=30, pady=12)
a4 = Combobox(bottom1, textvariable=value1, width=15, height=27, font=("Times New Roman", 19))
a4["values"] = ["P", "A"]
a4.set("Select")
a4.grid(row=0, column=3, padx=20)

b1 = Label(bottom1, text="2", font=("Times New Roman", 15), background='black', foreground='white').grid(row=1,column=0,padx=80,pady=12)
b2 = Label(bottom1, text="17AG1A002", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=1, column=1, padx=10, pady=12)
b3 = Label(bottom1, text="ANKENAPALLY PRANAY", font=("Times New Roman", 15), background='BLACK',foreground='WHITE', width=27, anchor=W)
b3.bind("<Enter>", pc2)
b3.grid(row=1, column=2, padx=10, pady=12)
b4 = Combobox(bottom1, textvariable=value2, width=15, height=27, font=("Times New Roman", 19))
b4["values"] = ["P", "A"]
b4.set("Select")
b4.grid(row=1, column=3, padx=20)

c1 = Label(bottom1, text="3", font=("Times New Roman", 15), background='black', foreground='white').grid(row=2,column=0,padx=10,pady=12)
c2 = Label(bottom1, text="17AG1A003", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=2, column=1, padx=10, pady=12)
c3 = Label(bottom1, text="YADLAPALLI AASHLESH", font=("Times New Roman", 15), background='BLACK',foreground='WHITE', width=27, anchor=W)
c3.bind("<Enter>", pc3)
c3.grid(row=2, column=2, padx=10, pady=12)
c4 = Combobox(bottom1, textvariable=value3, width=15, height=27, font=("Times New Roman", 19))
c4["values"] = ["P", "A"]
c4.set("Select")
c4.grid(row=2, column=3, padx=20)

d1 = Label(bottom1, text="4", font=("Times New Roman", 15), background='black', foreground='white').grid(row=3,column=0,padx=10,pady=12)
d2 = Label(bottom1, text="17AG1A004", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=3, column=1, padx=10, pady=12)
d3 = Label(bottom1, text="MADINENI RAVITEJA", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=27, anchor=W)
d3.bind("<Enter>", pc4)
d3.grid(row=3, column=2, padx=10, pady=12)
d4 = Combobox(bottom1, textvariable=value4, width=15, height=27, font=("Times New Roman", 19))
d4["values"] = ["P", "A"]
d4.set("Select")
d4.grid(row=3, column=3, padx=20)

e1 = Label(bottom1, text="5", font=("Times New Roman", 15), background='black', foreground='white').grid(row=4,column=0,padx=80,pady=12)
e2 = Label(bottom1, text="17AG1A005", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=4, column=1, padx=10, pady=12)
e3 = Label(bottom1, text="TUPPELLI VIKIRANTH", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=27, anchor=W)
e3.bind("<Enter>", pc5)
e3.grid(row=4, column=2, padx=10, pady=12)
e4 = Combobox(bottom1, textvariable=value5, width=15, height=27, font=("Times New Roman", 19))
e4["values"] = ["P", "A"]
e4.set("Select")
e4.grid(row=4, column=3, padx=20)

f1 = Label(bottom1, text="6", font=("Times New Roman", 15), background='black', foreground='white').grid(row=5,column=0,padx=10,pady=12)
f2 = Label(bottom1, text="17AG1A006", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=5, column=1, padx=10, pady=12)
f3 = Label(bottom1, text="ANUGU SHIVANADH REDDY", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=27, anchor=W)
f3.bind("<Enter>", pc6)
f3.grid(row=5, column=2, padx=10, pady=12)
f4 = Combobox(bottom1, textvariable=value6, width=15, height=27, font=("Times New Roman", 19))
f4["values"] = ["P", "A"]
f4.set("Select")
f4.grid(row=5, column=3, padx=20)

g1 = Label(bottom1, text="7", font=("Times New Roman", 15), background='black', foreground='white').grid(row=6,column=0,padx=10,pady=12)
g2 = Label(bottom1, text="17AG1A007", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=6, column=1, padx=10, pady=12)
g3 = Label(bottom1, text="AGGIDI VIDYA SAGAR", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=27, anchor=W)
g3.bind("<Enter>", pc7)
g3.grid(row=6, column=2, padx=10, pady=12)
g4 = Combobox(bottom1, textvariable=value7, width=15, height=27, font=("Times New Roman", 19))
g4["values"] = ["P", "A"]
g4.set("Select")
g4.grid(row=6, column=3, padx=20)

h1 = Label(bottom1, text="8", font=("Times New Roman", 15), background='black', foreground='white').grid(row=7,column=0,padx=10,pady=12)
h2 = Label(bottom1, text="17AG1A008", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=7, column=1, padx=10, pady=12)
h3 = Label(bottom1, text="KASOJI SRAVANTH KUMAR", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=27, anchor=W)
h3.bind("<Enter>", pc8)
h3.grid(row=7, column=2, padx=10, pady=12)
h4 = Combobox(bottom1, textvariable=value8, width=15, height=27, font=("Times New Roman", 19))
h4["values"] = ["P", "A"]
h4.set("Select")
h4.grid(row=7, column=3, padx=20)

i1 = Label(bottom1, text="9", font=("Times New Roman", 15), background='black', foreground='white').grid(row=8,column=0,padx=10,pady=12)
i2 = Label(bottom1, text="17AG1A009", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=8, column=1, padx=10, pady=12)
i3 = Label(bottom1, text="THATTALA SAIKUMAR ", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=27, anchor=W)
i3.bind("<Enter>", pc9)
i3.grid(row=8, column=2, padx=10, pady=12)
i4 = Combobox(bottom1, textvariable=value9, width=15, height=27, font=("Times New Roman", 19))
i4["values"] = ["P", "A"]
i4.set("Select")
i4.grid(row=8, column=3, padx=20)

j1 = Label(bottom1, text="10", font=("Times New Roman", 15), background='black', foreground='white').grid(row=9,column=0,padx=10,pady=12)
j2 = Label(bottom1, text="17AG1A010", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=9, column=1, padx=10, pady=12)
j3 = Label(bottom1, text="MOHAMMAD SOHAIL ", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=27, anchor=W)
j3.bind("<Enter>", pc10)
j3.grid(row=9, column=2, padx=10, pady=12)
j4 = Combobox(bottom1, textvariable=value10, width=15, height=27, font=("Times New Roman", 19))
j4["values"] = ["P", "A"]
j4.set("Select")
j4.grid(row=9, column=3, padx=20)

k1 = Label(bottom1, text="11", font=("Times New Roman", 15), background='black', foreground='white').grid(row=10,column=0,padx=10,pady=12)
k2 = Label(bottom1, text="17AG1A011", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=10, column=1, padx=10, pady=12)
k3 = Label(bottom1, text="KASHETTI AJAY ", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=27, anchor=W)
k3.bind("<Enter>", pc11)
k3.grid(row=10, column=2, padx=10, pady=12)
k4 = Combobox(bottom1, textvariable=value11, width=15, height=27, font=("Times New Roman", 19))
k4["values"] = ["P", "A"]
k4.set("Select")
k4.grid(row=10, column=3, padx=20)

l1 = Label(bottom1, text="12", font=("Times New Roman", 15), background='black', foreground='white').grid(row=11,column=0,padx=10,pady=12)
l2 = Label(bottom1, text="17AG1A012", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=11, column=1, padx=10, pady=12)
l3 = Label(bottom1, text="S P ANIKETH JAIN", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=27, anchor=W)
l3.bind("<Enter>", pc12)
l3.grid(row=11, column=2, padx=10, pady=12)
l4 = Combobox(bottom1, textvariable=value12, width=15, height=27, font=("Times New Roman", 19))
l4["values"] = ["P", "A"]
l4.set("Select")
l4.grid(row=11, column=3, padx=20)

m1 = Label(bottom1, text="13", font=("Times New Roman", 15), background='black', foreground='white').grid(row=12,column=0,padx=10,pady=12)
m2 = Label(bottom1, text="17AG1A013", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=15).grid(row=12, column=1, padx=10, pady=12)
m3 = Label(bottom1, text="BADAVATH SANTHOSH", font=("Times New Roman", 15), background='BLACK', foreground='WHITE',width=27, anchor=W)
m3.bind("<Enter>", pc13)
m3.grid(row=12, column=2, padx=10, pady=12)
m4 = Combobox(bottom1, textvariable=value13, width=15, height=27, font=("Times New Roman", 19))
m4["values"] = ["P", "A"]
m4.set("Select")
m4.grid(row=12, column=3, padx=20)
rest = Button(image, width=5, height=1, text="Reset", font=("Times New Roman", 25), background='black',foreground='red', bd=10, command=Rest)
rest.grid(row=0, column=0, sticky=W, padx=15)
def Exit():
    answer = tkinter.messagebox.askyesnocancel("Exit System", "Do you want to quit")
    if answer == True:
        root1.destroy()
exit = Button(image, width=5, height=1, text="Exit", font=("Times New Roman", 25), background='black', foreground='red',bd=10, command=Exit)
exit.grid(row=0, column=1, sticky=E, padx=10)
name =Label(image, text=" NAME OF THE CANDIDATE", font=("Times New Roman", 13), background='black',foreground='white')
name.grid(row=1, column=0, columnspan=2, pady=40)
root1.mainloop()