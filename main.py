import tkinter
from core.classes.login import LoginWindow


def main():

    root = tkinter.Tk()
    log = LoginWindow(root)
    log.mainloop()

    print("Program Execution Completed")


if __name__ == "__main__":
    main()