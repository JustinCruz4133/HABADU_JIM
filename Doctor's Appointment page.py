from tkinter import *
from tkinter import ttk

def mainwindow():
    global mainpage
    mainpage = Tk()
    mainpage.geometry("650x325+450+50")
    mainpage.title("Clinic shits")
    mainpage.resizable(FALSE, FALSE)
    
    def temp_ftext(e):
        fnametext.delete(0,"end")
        fnametext.configure(fg="black")

    def restore_fplaceholder(e):
        if not fnametext.get():
            fnametext.insert(0, "First Name")
            fnametext.config(fg="gray")
    
    def temp_ltext(e):
        lnametext.delete(0,"end")
        lnametext.configure(fg="black")

    def restore_lplaceholder(e):
        if not lnametext.get():
            lnametext.insert(0, "Last Name")
            lnametext.config(fg="gray")

    Label(mainpage, text="+++++++++++++++++++++++++++ Habadu Jim +++++++++++++++++++++++++++", font=("Sans Serif", 13, "bold"), bd=0, fg="#526D82").place(x=5,y=9)
    Label(mainpage, text="Patient Appointment Form", font=("Sans Serif", 19, "bold"), fg="white", bd=21, bg="#526D82", padx=120).pack(pady=40)
    Label(mainpage, text="Patient's Name", font=("Sans Serif", 13, "bold"), bd=0).place(x=40,y=130)
    Label(mainpage, text="First Name", font=("Sans Serif", 9, "bold"), bd=0).place(x=43,y=190)

    fnametext = Entry(mainpage, width=20, bd=3, font=("Sans Serif", 17))
    fnametext.insert(0, "First Name")
    fnametext.place(x=40,y=153)
    fnametext.config(fg="gray")
    fnametext.bind("<FocusIn>", temp_ftext)
    fnametext.bind("<FocusOut>", restore_fplaceholder)

    Label(mainpage, text="Last Name", font=("Sans Serif", 9, "bold"), bd=0).place(x=345,y=190)

    lnametext= Entry(mainpage, width=20, bd=3, font=("Sans Serif", 17))
    lnametext = Entry(mainpage, width=20, bd=3, font=("Sans Serif", 17))
    lnametext.insert(0, "Last Name")
    lnametext.place(x=340,y=153)
    lnametext.config(fg="gray")
    lnametext.bind("<FocusIn>", temp_ltext)
    lnametext.bind("<FocusOut>", restore_lplaceholder)

    Label(mainpage, text="Patient's Date of Birth", font=("Sans Serif", 13, "bold"), bd=0).place(x=40,y=230)

    getMonth = StringVar()
    getYear = StringVar()
    getDay = StringVar()
    
    month = ttk.Combobox(mainpage, textvariable=getMonth, font=("Sans Serif", 17), width=9, values=list(["January", "February", "March", "April", "May", "June", 
                                                                                                        "July", "August", "September", "October", "November", "December"]))
    month.set("November")
    month.place(x=40,y=260)

    day = ttk.Combobox(mainpage, textvariable=getDay, values=list(range(1, 32)), font=("Sans Serif", 17), width=2)
    day.place(x=190,y=260)
    day.set("18")

    year = ttk.Combobox(mainpage, textvariable=getYear, values=list(range(1950, 2025)), font=("Sans Serif", 17), width=5)
    year.set("2023")
    year.place(x=249,y=260)

    Button(mainpage, text="Set Appointment", fg="White", bg="#526D82", font=("Sans Serif", 17), width=15).place(x=380,y=252)


    pagelist = Toplevel(mainpage)
    pagelist.geometry("500x300+225+445")
    pagelist.title("List")
    pagelist.resizable(FALSE, FALSE)

    Label(pagelist, text="Last Name", font=("Sans Serif", 9, "bold"), bd=0).pack()

    nextl = Toplevel(mainpage)
    nextl.geometry("500x300+850+445")
    nextl.title("List")
    nextl.resizable(FALSE, FALSE)

    mainpage.mainloop()
mainwindow()
