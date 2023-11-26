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
    global get_name, get_surname, get_age, get_symptoms, patient_name

    # NAME to DOC LIST
    get_name = name.get()
    get_surname = surname.get()
    get_age = age.get()
    get_symptoms = symptoms.get()
    patient_name = f"{get_surname}, {get_name}, {get_age} yr/yrs old - ({get_symptoms})"

    if patient_name:
        list_doc.insert(END, patient_name)
        #list_doc_copy.insert(END, f"{get_surname}, {get_name}")

    # UPDATE
    update_inC_Q()

    # DELETING NAME, SURNAME, AGE Entry Box
    ps_clear()
def ps_clear():
    # DELETING NAME, SURNAME, AGE Entry Box
    name.set("")
    surname.set("")
    age.set("")
    symptoms.set("")
def ds_done():
    if list_doc.size() > 0:
        list_doc.delete(0)

    #if list_doc_copy.size() > 0:
    #    list_doc_copy.delete(0)

    # UPDATE
    update_inC_Q()
def ps_ds_qs():
    mainscreen.withdraw()

    ##################################################
    # PATIENT SCREEN #

    global pscreen, name, surname, age, symptoms, entry_name, entry_surname, entry_age, entry_symptoms

    pscreen = Toplevel(mainscreen)
    pscreen.geometry(f"500x400+{int(xBor + 100)}+{int(yBor + 350)}")
    pscreen.title("PATIENT'S APPOINTMENT SCREEN")
    #pscreen.configure(bg="#1B262C")
    pscreen.resizable(False, False)

    name = StringVar()
    surname = StringVar()
    age = StringVar()
    symptoms = StringVar()

    #Label(pscreen, text="").pack()  # BLANK

    Label(pscreen, text="Patient Appointment Form", fg="white", bg="#526D82", bd=15, font=("Sans Serif", 15, "bold"),
          padx=90).pack(pady=20)
    Label(pscreen, text="Patient's Name", bd=0, font=("Sans Serif", 12, "bold")).place(x=40, y=100)
    #Label(pscreen, text="", bg="#1B262C").pack() # BLANK

    #Label(pscreen, text="Name:", fg="white", bg="#1B262C", font=("Helvetica", 10, "bold")).pack()
    entry_name = Entry(pscreen, width=17, bd=3, font=("Sans Serif", 15), textvariable=name)
    entry_name.place(x=40, y=125)
    entry_surname = Entry(pscreen, width=17, bd=3, font=("Sans Serif", 15), textvariable=surname)
    entry_surname.place(x=265, y=125)

    Label(pscreen, text="First Name", bd=0, font=("Sans Serif", 8, "bold")).place(x=45, y=160)
    Label(pscreen, text="Last Name", bd=0, font=("Sans Serif", 8, "bold")).place(x=270, y=160)

    Label(pscreen, text="Age", bd=0, font=("Sans Serif", 12, "bold")).place(x=40, y=180)
    entry_age = Entry(pscreen, width=5, bd=3, font=("Sans Serif", 15), textvariable=age)
    entry_age.place(x=40, y=205)

    # SYMPTOMS
    Label(pscreen, text="Symptoms", bd=0, font=("Sans Serif", 12, "bold")).place(x=40, y=250)
    entry_symptoms = Entry(pscreen, width=37, bd=3, font=("Sans Serif", 15), textvariable=symptoms)
    entry_symptoms.place(x=40, y=275)


    #Label(pscreen, text="", bg="#1B262C").pack()  # BLANK

    Button(pscreen, text="Set Appointment", fg="white", bg="#526D82", height=1, width=20, bd=5,
           font=("Sans Serif", 16), command=ps_set_appointment).place(x=60, y=330)

    Button(pscreen, text="Clear", fg="white", bg="#526D82", height=1, width=5, bd=5,
           font=("HSans Serif", 16), command=ps_clear).place(x=360, y=330)

    ##################################################

    ##################################################
    # DOCTOR SCREEN #

    global dscreen, list_doc
    dscreen = Toplevel(mainscreen)
    dscreen.geometry(f"500x400+{int(xBor + 800)}+{int(yBor + 350)}")
    dscreen.title("DOCTOR'S CONSULTATION SCREEN")
    #dscreen.configure(bg="#1B262C")
    dscreen.resizable(False, False)


    Label(dscreen, text="Consultation List", fg="white", bg="#526D82", bd=15, font=("Sans Serif", 15, "bold"),
          padx=90).pack(pady=20)

    Label(dscreen, text="List", bd=0, font=("Sans Serif", 12, "bold")).place(x=40, y=100)

    list_doc = Listbox(dscreen, height=10, width=69)
    list_doc.place(x=40, y=125)

    Button(dscreen, text="Done", fg="white", bg="#526D82", height=1, width=5, bd=5,
           font=("Sans Serif", 13), command=ds_done).place(x=230, y=330)

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
