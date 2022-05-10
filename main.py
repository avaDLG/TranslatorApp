# videos that helped me!
# https://www.youtube.com/watch?v=64f5fKBM3-o&t=200s


from gui import *
from tkinter import *


def main():
    # creating the gui window
    window = Tk()
    # titling the window
    window.title('Python Translator')
    # setting the dimensions of the window
    window.geometry('450x800')
    # making sure the window is not re-sizable
    window.minsize(450, 800)
    window.maxsize(450, 800)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
