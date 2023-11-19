from tkinter import *
def update_inC_Q():
    global show_in_consul, show_in_queue

    # UPDATES IN CONSULTATION
    show_in_consul = list_doc.get(0)
    in_consul.delete(0, END)
    in_consul.insert(0, show_in_consul)

    # UPDATES QUEUE
    list_queue.delete(0, END)
    for i in range(list_doc.size()):
        show_in_queue = list_doc.get(i + 1)
        if show_in_queue:
            list_queue.insert(END, show_in_queue)
def ps_set_appointment():
    global get_name

    # NAME to DOC LIST
    get_name = name.get()
    if get_name:
        list_doc.insert(END, get_name)

    # UPDATE
    update_inC_Q()

    # DELETING NAME, SURNAME, AGE Entry Box
    ps_clear()
def ps_clear():
    # DELETING NAME, SURNAME, AGE Entry Box
    name.set("")
    surname.set("")
    age.set("")
def ds_done():
    if list_doc.size() > 0:
        list_doc.delete(0)

    # UPDATE
    update_inC_Q()
def ps_ds_qs():
    mainscreen.withdraw()

    ##################################################
    # PATIENT SCREEN #

    global pscreen, name, surname, age, entry_name, entry_surname, entry_age

    pscreen = Toplevel(mainscreen)
    pscreen.geometry(f"500x400+{int(xBor + 100)}+{int(yBor + 350)}")
    pscreen.title("PATIENT'S APPOINTMENT SCREEN")
    pscreen.configure(bg="#1B262C")
    pscreen.resizable(False, False)

    name = StringVar()
    surname = StringVar()
    age = StringVar()

    Label(pscreen, text="", bg="#1B262C").pack()  # BLANK

    Label(pscreen, text="PATIENT APPOINTMENT FORM", fg="#3282B8", bg="#1B262C", height=3, width=50,
          font=("Helvetica", 20, "bold")).pack()
    Label(pscreen, text="Enter the details below:", fg="white", bg="#1B262C", font=("Helvetica", 13, "bold")).pack()
    Label(pscreen, text="", bg="#1B262C").pack()

    Label(pscreen, text="Name:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    entry_name = Entry(pscreen, justify="center", textvariable=name)
    entry_name.pack()

    Label(pscreen, text="Surname:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    entry_surname = Entry(pscreen, justify="center", textvariable=surname)
    entry_surname.pack()

    Label(pscreen, text="Age:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    entry_age = Entry(pscreen, justify="center", textvariable=age)
    entry_age.pack()

    Label(pscreen, text="", bg="#1B262C").pack()  # BLANK

    Button(pscreen, text="Set Appointment", fg="white", bg="#0F4C75", height=1, width=20, bd=5,
           font=("Helvetica", 12, "bold"), command=ps_set_appointment).pack()

    Button(pscreen, text="CLEAR", fg="white", bg="#0F4C75", font=("Helvetica", 10, "bold"), command=ps_clear).place(x=375, y=270)

    ##################################################

    ##################################################
    # DOCTOR SCREEN #

    global dscreen, list_doc
    dscreen = Toplevel(mainscreen)
    dscreen.geometry(f"500x400+{int(xBor + 800)}+{int(yBor + 350)}")
    dscreen.title("DOCTOR'S CONSULTATION SCREEN")
    dscreen.configure(bg="#1B262C")
    dscreen.resizable(False, False)

    Label(dscreen, text="", bg="#1B262C").pack()  # BLANK
    Label(dscreen, text="CONSULTATION LIST", fg="#3282B8", bg="#1B262C", height=3, width=50,
          font=("Helvetica", 20, "bold")).pack()
    Label(dscreen, text="LIST:", fg="white", bg="#1B262C", font=("Helvetica", 13, "bold")).pack()
    Label(dscreen, text="", bg="#1B262C").pack()  # BLANK

    list_doc = Listbox(dscreen, justify="center", height=10, width=15)
    list_doc.pack()

    Button(dscreen, text="DONE", fg="white", bg="#0F4C75", font=("Helvetica", 10, "bold"), command=ds_done).place(x=325,
                                                                                                                  y=170)
    ##################################################

    ##################################################
    # WAITING SCREEN #

    global wscreen, in_consul, in_consul_var, list_queue

    wscreen = Toplevel(mainscreen)
    wscreen.geometry(f"700x300+{int(xBor + 350)}+{int(yBor)}")
    wscreen.title("Waiting Screen")
    wscreen.configure(bg="#1B262C")
    wscreen.resizable(False, False)

    in_consul_var = StringVar()

    Label(wscreen, text="In Consultation", fg="#3282B8", bg="#1B262C", height=2, width=50,
          font=("Helvetica", 15, "bold")).pack()
    in_consul = Entry(wscreen, justify="center", textvariable=in_consul_var)
    in_consul.pack()

    Label(wscreen, text="Next in Queue", fg="#3282B8", bg="#1B262C", height=2, width=50,
          font=("Helvetica", 15, "bold")).pack()
    list_queue = Listbox(wscreen, justify="center", height=9, width=15)
    list_queue.pack()

    ##################################################


def main_proj():
    global mainscreen, screen_width, screen_height, xBor, yBor

    mainscreen = Tk()

    screen_width = mainscreen.winfo_screenwidth()
    screen_height = mainscreen.winfo_screenheight()
    xBor = (screen_width - 1400) / 2
    yBor = (screen_height - 850) / 2

    # mainscreen.geometry("400x400+570+190") - Original Size
    mainscreen.geometry(f"400x400+{int(xBor + 500)}+{int(yBor + 200)}")
    mainscreen.title("DOCTOR APPOINTMENT SIMULATOR")
    mainscreen.configure(bg="#1B262C")

    Label(mainscreen, text="", bg="#1B262C").pack()  # BLANK
    Label(text="PRESS START", fg="#3282B8", bg="#1B262C", height=3, width=50, font=("Helvetica", 20, "bold")).pack()

    Label(mainscreen, text="", bg="#1B262C").pack()  # BLANK
    Label(mainscreen, text="", bg="#1B262C").pack()  # BLANK
    Label(mainscreen, text="", bg="#1B262C").pack()  # BLANK

    Button(text="START", fg="white", bg="#0F4C75", height=2, width=20, font=("Helvetica", 15, "bold"),
           command=ps_ds_qs).pack()

    Label(mainscreen, text="", bg="#1B262C").pack()  # BLANK

    Label(text=f"Screen width: {screen_width} x: {xBor}").pack()
    Label(text=f"Screen height: {screen_height} y: {yBor}").pack()

    mainscreen.resizable(False, False)
    mainscreen.mainloop()

main_proj()
