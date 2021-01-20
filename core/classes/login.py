import tkinter
from core.classes.main_window import MainWindow


class LoginWindow(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Login")
        self.master.resizable(False, False)
        self.lb_name = tkinter.Label(self.master, text="Usuario:")
        self.lb_name.pack()

        self.in_name = tkinter.Entry(self.master, width=26)
        self.in_name.pack()

        self.lb_pass = tkinter.Label(self.master, text="Contraseña:")
        self.lb_pass.pack()

        self.in_pass = tkinter.Entry(self.master, width=26, show="*")
        self.in_pass.pack()

        self.bt_send = tkinter.Button(self.master, text="Validar", command=self.check_info)
        self.bt_send.pack(pady=10)

    def check_info(self):
        """
        accion que genera el boton de Validar
        Valida que el usuario y contraseña sean correctos e inicializa
        el programa principal en caso de que los datos sean validos.
        :return:
        """
        if self.in_name.get() == "admin" and self.in_pass.get() == "admin":
            self.master.destroy()
            root = tkinter.Tk()
            App = MainWindow(root)
            App.mainloop()
