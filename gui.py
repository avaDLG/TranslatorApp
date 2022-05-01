from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob


class GUI:
    def __init__(self, window):
        self.frame_top = Frame(window)
        self.user_text = Text(self.frame_top, height=10, width=50)
        self.user_langauge_combo = ttk.Combobox(self.frame_top, width=35) #, value=language_list
        #self.user_langauge_combo.current(21)  # ENGLISH
        self.user_text.pack(side='top', pady=20)
        self.user_langauge_combo.pack()
        self.frame_top.pack()

        self.frame_middle = Frame(window)
        self.translate_button = Button(self.frame_middle, text='TRANSLATE', height=5, width=20, command=self.translate_clicked)
        self.translate_button.pack(side='top', pady=35)
        self.frame_middle.pack()

        self.frame_bottom = Frame(window)
        self.translated_text = Text(self.frame_bottom, height=10, width=50)
        self.translated_langauge_combo = ttk.Combobox(self.frame_bottom, width=35)  #value=language_list
        #  self.translated_language_combo.current(26)  #FRENCH TO CHANGE LATER
        self.translated_text.pack(side='top', pady=15)
        self.translated_langauge_combo.pack()
        self.frame_bottom.pack()

        self.frame_very_bottom = Frame(window)
        self.clear_button = Button(self.frame_very_bottom, text='CLEAR', height=2, width=15, command=self.clear_clicked)
        self.clear_button.pack(side='top', pady=55)
        self.frame_very_bottom.pack()

    def translate_clicked(self):
        pass

    def clear_clicked(self):
        pass

