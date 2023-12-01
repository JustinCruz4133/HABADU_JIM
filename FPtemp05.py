from tkinter import *

def update_inC_Q():
    global show_in_consul, show_in_queue, show_doc_name, show_doc_age, show_doc_symptoms, show_num_p

    # UPDATES IN CONSULTATION
    show_in_consul = list_doc.get(0)
    in_consul.config(state="normal")
    in_consul.delete(0, END)
    in_consul.insert(0, show_in_consul)
    in_consul.config(state="readonly")

    # UPDATES DOC NAME
    show_doc_name = list_doc_name01.get(0)
    list_doc_name.config(state="normal")
    list_doc_name.delete(0, END)
    list_doc_name.insert(0, show_doc_name)
    list_doc_name.config(state=DISABLED)

    # UPDATES DOC AGE
    show_doc_age = list_doc_age01.get(0)
    list_doc_age.config(state="normal")
    list_doc_age.delete(0, END)
    list_doc_age.insert(0, show_doc_age)
    list_doc_age.config(state=DISABLED)

    # UPDATES DOC SYMPTOMS
    show_doc_symptoms = list_doc_symptoms01.get(0)
    list_doc_symptoms.config(state="normal")
    list_doc_symptoms.delete(0, END)
    list_doc_symptoms.insert(0, show_doc_symptoms)
    list_doc_symptoms.config(state=DISABLED)

    # UPDATES QUEUE
    list_queue.config(state="normal")
    list_queue.delete(0, END)
    for i in range(list_doc.size()):
        show_in_queue = list_doc.get(i + 1)
        if show_in_queue:
            list_queue.insert(END, show_in_queue)
    list_queue.config(state=DISABLED)

    #UPDATES QUEUE NUM
    list_queue_num.config(state="normal")
    list_queue_num.delete(0, END)
    for i in range(list_doc_num_p.size()):
        show_in_queue_num = list_doc_num_p.get(i + 1)
        if show_in_queue_num:
            list_queue_num.insert(END, show_in_queue_num)
    list_queue_num.config(state=DISABLED)

    # UPDATES IN PATIENT NO
    show_num_p = list_doc_num_p.get(0)
    entry_npatient.config(state="normal")
    entry_npatient.delete(0, END)
    entry_npatient.insert(0, show_num_p)
    entry_npatient.config(state="readonly")

num_p = 0

def ps_set_appointment():
    global get_name, get_surname, get_age, get_symptoms, patient_name, wpscreen, num_p

    # NAME to DOC LIST
    get_name = name.get()
    get_surname = surname.get()
    get_age = age.get()
    get_symptoms = symptoms.get()

    if get_name and get_surname and get_age and get_symptoms:
        if (get_age.isdigit() == True) and ((get_name.isalpha() and get_surname.isalpha() and get_symptoms.isalpha()) == True):
            patient_name = f"{get_surname}, {get_name}"

            if patient_name:
                list_doc.insert(END, patient_name)
                list_doc_name01.insert(END, patient_name)
                list_doc_age01.insert(END, get_age)
                list_doc_symptoms01.insert(END, get_symptoms)

            num_p += 1
            list_doc_num_p.insert(END, num_p)

            # UPDATE
            update_inC_Q()

            # DELETING NAME, SURNAME, AGE Entry Box
            ps_clear()
        else:
            pass
            """wpscreen = Toplevel(mainscreen)
            wpscreen.geometry(f"100x50+{int(xBor + 650)}+{int(yBor + 400)}")
            wpscreen.title("ERROR!")
            wpscreen.resizable(False, False)

            Label(wpscreen, text="Patient Appointment Form", fg="white", bg="#526D82", bd=15,
                  font=("Sans Serif", 15, "bold"),
                  padx=90).pack(pady=20)"""
    else:
        pass
        """wpscreen = Toplevel(mainscreen)
        wpscreen.geometry(f"100x50+{int(xBor + 650)}+{int(yBor + 400)}")
        wpscreen.title("ERROR!")
        wpscreen.resizable(False, False)

        Label(wpscreen, text="Patient Appointment Form", fg="white", bg="#526D82", bd=15,
              font=("Sans Serif", 15, "bold"),
              padx=90).pack(pady=20)"""


    #patient_name = f"{get_surname}, {get_name}"

    #if patient_name:
    #    list_doc.insert(END, patient_name)
    #    list_doc_name01.insert(END, patient_name)
    #    list_doc_age01.insert(END, get_age)
    #    list_doc_symptoms01.insert(END, get_symptoms)

    # UPDATE
    #update_inC_Q()

    # DELETING NAME, SURNAME, AGE Entry Box
    #ps_clear()

def ps_clear():
    # DELETING NAME, SURNAME, AGE Entry Box
    name.set("")
    surname.set("")
    age.set("")
    symptoms.set("")
def ds_done():
    if list_doc.size() > 0:
        list_doc.delete(0)
        list_doc_name01.delete(0)
        list_doc_age01.delete(0)
        list_doc_symptoms01.delete(0)
        list_doc_num_p.delete(0)

    # UPDATE
    update_inC_Q()
def ps_ds_qs():
    mainscreen.withdraw()

    ##################################################
    # PATIENT SCREEN #

    global pscreen, name, surname, age, symptoms

    pscreen = Toplevel(mainscreen)
    pscreen.geometry(f"500x400+{int(xBor + 100)}+{int(yBor + 350)}")
    pscreen.title("PATIENT'S APPOINTMENT SCREEN")
    pscreen.resizable(False, False)

    name = StringVar()
    surname = StringVar()
    age = StringVar()
    symptoms = StringVar()

    Label(pscreen, text="Patient Appointment Form", fg="white", bg="#526D82", bd=15, font=("Sans Serif", 15, "bold"),
          padx=90).pack(pady=20)
    Label(pscreen, text="Patient's Name", bd=0, font=("Sans Serif", 12, "bold")).place(x=40, y=100)

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

    Button(pscreen, text="Set Appointment", fg="white", bg="#526D82", height=1, width=20, bd=5,
           font=("Sans Serif", 16), command=ps_set_appointment).place(x=60, y=330)

    Button(pscreen, text="Clear", fg="white", bg="#526D82", height=1, width=5, bd=5,
           font=("HSans Serif", 16), command=ps_clear).place(x=360, y=330)

    ##################################################

    ##################################################
    # DOCTOR SCREEN #

    global dscreen, list_doc, list_doc_name, list_doc_age, list_doc_symptoms, list_doc_name01, list_doc_age01, \
        list_doc_symptoms01, npatient, entry_npatient, list_doc_num_p

    dscreen = Toplevel(mainscreen)
    dscreen.geometry(f"500x400+{int(xBor + 800)}+{int(yBor + 350)}")
    dscreen.title("DOCTOR'S CONSULTATION SCREEN")
    dscreen.resizable(False, False)

    npatient = StringVar()

    Label(dscreen, text="Consultation List", fg="white", bg="#526D82", bd=15, font=("Sans Serif", 15, "bold"),
          padx=130).pack(pady=20)

    Label(dscreen, text="Patient No.", bd=0, font=("Sans Serif", 12, "bold")).place(x=40, y=95)
    entry_npatient = Entry(dscreen, width=5, bd=0, state="readonly", bg="#f0f0f0", font=("Sans Serif", 12, "bold"), textvariable=npatient)
    entry_npatient.place(x=130, y=95)

    Label(dscreen, text="Name:", bd=0, font=("Sans Serif", 12, "bold")).place(x=40, y=140)
    list_doc_name = Listbox(dscreen, height=1, width=17, state=DISABLED, justify="center", font=("Sans Serif", 25, "bold"))
    list_doc_name.place(x=130, y=125)

    Label(dscreen, text="Age:", bd=0, font=("Sans Serif", 12, "bold")).place(x=40, y=215)
    list_doc_age = Listbox(dscreen, height=1, width=17, state=DISABLED, justify="center", font=("Sans Serif", 25, "bold"))
    list_doc_age.place(x=130, y=200)

    Label(dscreen, text="Symptoms:", bd=0, font=("Sans Serif", 12, "bold")).place(x=35, y=290)
    list_doc_symptoms = Listbox(dscreen, height=1, width=17, state=DISABLED, justify="center", font=("Sans Serif", 25, "bold"))
    list_doc_symptoms.place(x=130, y=275)

    list_doc = Listbox(dscreen)
    list_doc_name01 = Listbox(dscreen)
    list_doc_age01 = Listbox(dscreen)
    list_doc_symptoms01 = Listbox(dscreen)
    list_doc_num_p = Listbox(dscreen)



    Button(dscreen, text="Done", fg="white", bg="#526D82", height=1, width=5, bd=5,
           font=("Sans Serif", 13), command=ds_done).place(x=230, y=340)

    ##################################################

    ##################################################
    # WAITING SCREEN #

    global wscreen, in_consul, in_consul_var, list_queue, list_queue_num

    wscreen = Toplevel(mainscreen)
    wscreen.geometry(f"700x300+{int(xBor + 350)}+{int(yBor)}") #yBor + 0 // try + 50
    wscreen.title("Waiting Screen")
    wscreen.configure(bg="#1B262C")
    wscreen.resizable(False, False)

    in_consul_var = StringVar()

    #Label(wscreen, text="In Consultation", fg="white", bg="#526D82", bd=15, font=("Sans Serif", 13, "bold"),
    #      padx=40).place(x=25, y=15)

    Label(wscreen, text="In Consultation", fg="white", bg="#1B262C", bd=0, font=("Sans Serif", 18, "bold")).place(x=50, y=30)

    #Label(wscreen, text="In Consultation", fg="#3282B8", bg="#1B262C", height=2, width=50,
    #      font=("Helvetica", 15, "bold")).pack()
    in_consul = Entry(wscreen, state="readonly", width=30, font=("Sans Serif", 14, "bold"), textvariable=in_consul_var)
    in_consul.place(x=260, y=33)

    Label(wscreen, text="Queue", fg="white", bg="#1B262C",
          bd=0, font=("Sans Serif", 16, "bold")).place(x=100, y=90)
    Label(wscreen, text="Patient's Name", fg="white", bg="#1B262C",
          bd=0, font=("Sans Serif", 16, "bold")).place(x=260, y=90)

    #Label(wscreen, text="Next in Queue", fg="#3282B8", bg="#1B262C", height=2, width=50,
    #      font=("Helvetica", 15, "bold")).pack()

    list_queue = Listbox(wscreen, width=30, state=DISABLED, height=6, font=("Sans Serif", 14, "bold"))
    list_queue.place(x=260, y=125)

    list_queue_num = Listbox(wscreen, justify="center", width=8, state=DISABLED, height=6, font=("Sans Serif", 14, "bold"))
    list_queue_num.place(x=90, y=125)

    ##################################################


def main_proj():
    global mainscreen, screen_width, screen_height, xBor, yBor

    mainscreen = Tk()

    screen_width = mainscreen.winfo_screenwidth()
    screen_height = mainscreen.winfo_screenheight()
    xBor = (screen_width - 1400) / 2    #1400
    yBor = (screen_height - 850) / 2    #850

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
