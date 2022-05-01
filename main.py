from gui import *
from tkinter import *


def main():
    window = Tk()
    window.title('Python Translator')
    window.geometry('450x700')

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
