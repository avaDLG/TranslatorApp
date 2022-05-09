from tkinter import *
from tkinter import ttk
import googletrans
import textblob
import textblob.exceptions
import textwrap


class GUI:
    """
    a class to create the gui and translate the text for the language translator
    """

    def __init__(self, window):
        """
        a constructor to create the gui from the window created in the main class
        :param window: the window from the main class
        """
        self.window = window

        # taking the values from the googletrans language dictionary and putting it into a list
        self.google_lang_dict = googletrans.LANGUAGES  # DICTIONARY OF ALL LANGUAGES
        self.language_list = list(self.google_lang_dict.values())

        # creating and packing the top frame which has the text box and the first combo box
        self.frame_top = Frame(window)
        self.user_text = Text(self.frame_top, height=10, width=35, font=('Arial', 18))
        self.user_language_combo = ttk.Combobox(self.frame_top, values=self.language_list, width=35)
        self.user_language_combo.current(21)  # ENGLISH
        self.user_text.pack(side='top', pady=20)
        self.user_language_combo.pack()
        self.frame_top.pack()

        # creating and packing the middle frame which has the translation button
        self.frame_middle = Frame(window)
        self.translate_button = Button(self.frame_middle, text='TRANSLATE', height=5, width=20, font=('Arial', 15),
                                       command=self.translate_clicked)
        self.translate_button.pack(side='top', pady=35)
        self.frame_middle.pack()

        # creating and backing the bottom frame which has the translated text label and the second combo box
        self.frame_bottom = Frame(window)
        self.translated_label = Label(self.frame_bottom, height=10, width=35, font=('Arial', 18))
        self.translated_language_combo = ttk.Combobox(self.frame_bottom, values=self.language_list, width=35)
        self.translated_language_combo.current(88)  # SPANISH
        self.translated_label.pack(side='top')
        self.translated_language_combo.pack()
        self.frame_bottom.pack()

        # creating and packing the very bottom label which has the clear button
        self.frame_very_bottom = Frame(window)
        self.clear_button = Button(self.frame_very_bottom, text='CLEAR', height=2, width=15, command=self.clear_clicked)
        self.clear_button.pack(side='top', pady=15)
        self.frame_very_bottom.pack()

    def translate_clicked(self) -> None:
        """
        method for when the translate button is clicked
        :return: nothing / changes the value of the text box and the translated label
        """

        global user_language_key, to_translate_language_key
        self.translated_label['text'] = ''

        # making sure the entered text will approx fit in the translated label
        if len(self.user_text.get(1.0, END)) > 250:
            self.translated_label['text'] = 'Typed too many characters at one time.\nTry again.'
            self.user_text.delete(1.0, END)
        else:
            try:
                # finding what language the user is typing in
                for key, value in self.google_lang_dict.items():
                    if value == self.user_language_combo.get():
                        user_language_key = key

                # finding what language the user wants the text translated to
                for key, value in self.google_lang_dict.items():
                    if value == self.translated_language_combo.get():
                        to_translate_language_key = key

                # using textblob to translate what the user types into a variable called text
                text = textblob.TextBlob(self.user_text.get(1.0, END))
                text = text.translate(from_lang=user_language_key, to=to_translate_language_key)
                text = str(text)

                # text wrapping it so all the translated text can be seen
                wrapper = textwrap.TextWrapper(width=30)
                text = wrapper.fill(text=text)
                self.translated_label['text'] = text

            # the textblob translation exceptions will show an error and clear the entry box
            except textblob.exceptions.NotTranslated:
                self.translated_label['text'] = 'Error Translating.\nIt is the same word/number in both languages.'
                self.user_text.delete(1.0, END)
            except textblob.exceptions.TranslatorError:
                self.translated_label['text'] = 'Error Translating.\nPlease type more words.'
                self.user_text.delete(1.0, END)

    def clear_clicked(self) -> None:
        """
        method for when the clear button is clicked
        :return: nothing / deletes the text from the entry box and the translated text label
        """
        self.user_text.delete(1.0, END)
        self.translated_label['text'] = ''






