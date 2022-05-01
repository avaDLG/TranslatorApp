from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
import textblob.exceptions


class GUI:

    def __init__(self, window):
        self.google_lang_dict = googletrans.LANGUAGES  # DICTIONARY OF ALL LANGUAGES
        self.language_list = list(self.google_lang_dict.values())

        self.frame_top = Frame(window)
        self.user_text = Text(self.frame_top, height=10, width=50)
        self.user_language_combo = ttk.Combobox(self.frame_top, values=self.language_list, width=35)
        self.user_language_combo.current(21)  # ENGLISH
        self.user_text.pack(side='top', pady=20)
        self.user_language_combo.pack()
        self.frame_top.pack()

        self.frame_middle = Frame(window)
        self.translate_button = Button(self.frame_middle, text='TRANSLATE', height=5, width=20,
                                       command=self.translate_clicked)
        self.translate_button.pack(side='top', pady=35)
        self.frame_middle.pack()

        self.frame_bottom = Frame(window)
        self.translated_text = Text(self.frame_bottom, height=10, width=50)
        self.translated_language_combo = ttk.Combobox(self.frame_bottom, values=self.language_list, width=35)
        self.translated_language_combo.current(88)  # SPANISH
        self.translated_text.pack(side='top', pady=15)
        self.translated_language_combo.pack()
        self.frame_bottom.pack()

        self.frame_very_bottom = Frame(window)
        self.clear_button = Button(self.frame_very_bottom, text='CLEAR', height=2, width=15, command=self.clear_clicked)
        self.clear_button.pack(side='top', pady=55)
        self.frame_very_bottom.pack()

    def translate_clicked(self):
        global user_language_key, to_translate_language_key
        self.translated_text.delete(1.0, END)

        try:
            for key, value in self.google_lang_dict.items():
                if value == self.user_language_combo.get():
                    user_language_key = key

            for key, value in self.google_lang_dict.items():
                if value == self.translated_language_combo.get():
                    to_translate_language_key = key

            text = textblob.TextBlob(self.user_text.get(1.0, END))
            text = text.translate(from_lang=user_language_key, to=to_translate_language_key)

            self.translated_text.insert(1.0, text)

        except textblob.exceptions.NotTranslated as i:
            self.translated_text.insert(1.0, 'Error Translating.\nIt is the same word/number in both languages.')
            self.user_text.delete(1.0, END)
        except textblob.exceptions.TranslatorError as e:
            self.translated_text.insert(1.0, 'Error Translating. Word must be at least three characters.')
            self.user_text.delete(1.0, END)
        except:
            self.translated_text.insert(1.0, 'ERROR TRY AGAIN')
            self.user_text.delete(1.0, END)

    def clear_clicked(self):
        self.user_text.delete(1.0, END)
        self.translated_text.delete(1.0, END)






