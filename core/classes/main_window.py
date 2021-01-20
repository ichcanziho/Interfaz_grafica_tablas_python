import tkinter
from core.classes.input_student import InputStudentWindow
from core.fuctions import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from tkinter.simpledialog import askstring
from tkinter import filedialog


class MainWindow(tkinter.Frame):
    """Esta clase genera la ventana principal del programa, en dónde se muestran las tablas y gráfica"""

    def __init__(self, master=None):
        super().__init__(master)
        self.default_path = "data/estudiantes.json"
        self.master.title("Hola")
        self.master.geometry("950x560")
        self.master.resizable(False, False)

        self.main_table = tkinter.LabelFrame(self.master, text="Alumnos")
        self.main_table.grid(row=0, column=0, padx=10)
        make_table(self.main_table, self.default_path, editable=False, width=250, height=150)

        self.students_df = pd.read_json(self.default_path)
        self.make_aux_table()

        self.graph_section_frame = tkinter.LabelFrame(self.master, text="Gráfica")
        self.graph_section_frame.grid(row=0, column=1, rowspan=2, padx=10)

        self.make_graph()

        self.buttons_frame = tkinter.LabelFrame(self.master, text="Opciones", width=500, height=100, pady=10)
        self.buttons_frame.grid(row=2, column=0, columnspan=2)

        self.bt_new = tkinter.Button(self.buttons_frame, text='Agregar',
                                     padx=70, pady=10, bg="spring green",
                                     command=self.student_entry)
        self.bt_new.pack(side=tkinter.LEFT, padx=10)

        self.bt_update = tkinter.Button(self.buttons_frame, text='Actualizar',
                                        padx=70, pady=10, bg="cyan",
                                        command=self.update_screen)
        self.bt_update.pack(side=tkinter.LEFT, padx=10)

        self.bt_load = tkinter.Button(self.buttons_frame, text='Cargar',
                                      padx=70, pady=10, bg="yellow",
                                      command=self.open_file)
        self.bt_load.pack(side=tkinter.LEFT, padx=10)

        self.bt_clear = tkinter.Button(self.buttons_frame, text='Limpiar',
                                       padx=70, pady=10, bg="OrangeRed3",
                                       command=self.clear_dataset)
        self.bt_clear.pack(side=tkinter.LEFT, padx=10)

    def open_file(self):
        """
        Accion que genera el boton de abrir
        abre una ventana para buscar un nuevo documento json para ponerlo en las tablas
        """

        open_file = filedialog.askopenfilename()
        self.default_path = open_file
        self.update_screen()

    def clear_dataset(self):
        """
        Accion que genera el boton de eliminar.
        Sobre escribe el último documento abierto con una versión vacía del mismo
        """

        password = askstring('Administrador', 'Escribe tu contraseña de administrador.',show='*')
        if password == "admin":
            output = pd.DataFrame({"Nombre": [],
                                   "Edad": [],
                                   "Escolaridad": [],
                                   "Fecha": [],
                                   "Hora": []})
            output.to_json(self.default_path)
            self.update_screen()

    def update_screen(self):
        """
        Accion que genera el boton de actualizar.
        actualiza la tabla de alumnos, la tabla de escolaridad y la gráfica de edades"
        """

        make_table(self.main_table, self.default_path, editable=False, width=250, height=150)
        self.students_df = pd.read_json(self.default_path)
        self.aux_table_frame.destroy()
        self.make_aux_table()
        self.canvas.get_tk_widget().destroy()
        self.toolbar.destroy()
        self.make_graph()

    def make_aux_table(self):
        """crea la tabla de escolaridad y su numero de alumnos"""
        scholarship = self.students_df.groupby("Escolaridad").Escolaridad.count()
        scholar_dict = {"Escolaridad": list(scholarship.index),
                        "Alumnos:": list(scholarship.values)}
        scholar_table = pd.DataFrame(scholar_dict)

        self.aux_table_frame = tkinter.LabelFrame(self.master, text="Escolaridad")
        self.aux_table_frame.grid(row=1, column=0)
        show_aux_table(self.aux_table_frame, scholar_table, editable=False, width=250, height=150)

    def display_graph(self, table):
        "muestra en el programa la gráfica de edades"
        fig = Figure(figsize=(6, 4), dpi=100)
        graph = fig.add_subplot(111)
        graph.bar(table["Edad"].astype(str), table["Alumnos"])
        graph.set_title("Distribucion de las edades de los alumnos")
        graph.set_xlabel("Edades")
        graph.set_ylabel("Frecuencia")
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_section_frame)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.graph_section_frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack()

    def make_graph(self):
        """crea la gráfica de edades y manda a llamar al método display_graph"""
        group_by_ages = self.students_df.groupby("Edad").Edad.count()
        table_by_ages = {"Edad": list(group_by_ages.index),
                         "Alumnos": list(group_by_ages.values)}
        table_by_ages = pd.DataFrame(table_by_ages)
        self.display_graph(table_by_ages)

    def student_entry(self):
        """Acción que ejecuta el boton "nuevo".
        abre una nueva ventana para ingresar un alumno."""
        InputStudentWindow(tkinter.Toplevel(self.master), path=self.default_path)



