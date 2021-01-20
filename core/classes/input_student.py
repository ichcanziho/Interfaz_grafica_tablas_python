import tkinter
import pandas as pd
from tkinter import ttk
from tkcalendar import DateEntry
import time
from tkinter import messagebox
import os.path as path


class InputStudentWindow(tkinter.Frame):

    def __init__(self, master=None, path="data/estudiantes.json"):
        super().__init__(master)
        self.pack()
        self.master.title("Entrada de alumnos")
        self.master.resizable(False, False)
        self.default_path = path
        # self.master.protocol("WM_DELETE_WINDOW", self.faa)
        self.lb_name = tkinter.Label(self.master, text="Nombre:")
        self.lb_name.pack()

        self.in_name = tkinter.Entry(self.master, width=26)
        self.in_name.pack()

        self.lb_age = tkinter.Label(self.master, text="Edad:")
        self.lb_age.pack()

        self.in_age = tkinter.Entry(self.master, width=26)
        self.in_age.pack()

        self.lb_school = tkinter.Label(self.master, text="Estudios:")
        self.lb_school.pack()

        self.cb_school = ttk.Combobox(self.master, state="readonly")
        self.cb_school["values"] = ["Primaria", "Secundaria", "Preparatoria", "Licenciatura", "Posgrado"]
        self.cb_school.current(0)
        self.cb_school.pack()

        self.lb_date = tkinter.Label(self.master, text="Fecha:")
        self.lb_date.pack()
        self.cal = DateEntry(self.master, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.cal.pack()

        self.lb_time = tkinter.Label(self.master, text="Hora:")
        self.lb_time.pack()

        self.in_time = tkinter.Entry(self.master, width=26)
        self.hour = time.strftime("%H:%M:%S")
        self.in_time.insert(0, self.hour)
        self.in_time.pack()

        self.bt_save = tkinter.Button(self.master, text="Guardar", command=self.save_student)
        self.bt_save.pack(pady=10)

    def save_student(self):
        """
        Valida que la información puesta sea coherente
        guarda el nuevo estudiante en el último documento abierto
        """
        if self.in_name.get() is None or self.in_name.get() == "" or self.cb_school.get().isdigit():
            messagebox.showerror("Error", "Por favor ingrese el nombre del estudiante. Verifique el formato.")
        elif self.in_age.get() is None or self.in_age.get() == "" or not self.in_age.get().isdigit():
            messagebox.showerror("Error", "Por favor ingrese la edad del estudiante. Verifique el formato.")
        elif self.cb_school.get() is None or self.cb_school.get() == "" or self.cb_school.get().isdigit():
            messagebox.showerror("Error", "Por favor ingrese la escolaridad del estudiante. Verifique la selección.")
        elif self.cal.get() is None or self.cal.get() == "":
            messagebox.showerror("Error", "Por favor ingrese la fecha de captura.")
        elif self.in_time.get() is None or self.in_time.get() == "":
            messagebox.showerror("Error", "Por favor ingrese la hora de captura.")
        else:
            output = pd.DataFrame({"Nombre": [self.in_name.get()],
                                   "Edad": [self.in_age.get()],
                                   "Escolaridad": [self.cb_school.get()],
                                   "Fecha": [self.cal.get()],
                                   "Hora": [self.in_time.get()]})
            if not (path.exists(self.default_path)):
                output.to_json(self.default_path)
            else:
                input_json = pd.read_json(self.default_path)
                output = pd.concat([input_json, output], axis=0)
                output.reset_index(drop=True, inplace=True)
                output.to_json(self.default_path)


