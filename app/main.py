'''
    Application - A code explainer for SQL
'''
from __future__ import annotations
from tkinter import END, messagebox
from turtle import width
from typing import Tuple
# from widgets.new_widgets import CTkQuestion, CTkResultLabel
import customtkinter

from widgets.new_widgets import CTkQuestion, CTkQuestionnaire

# Creating home configs
customtkinter.set_appearance_mode("Dark")


def alert_error(error_message):
    '''
        Show alert for error
    '''
    messagebox.showerror(title="Error founded", message=error_message)


def alert_information(information_message):
    '''
        Show alert for information
    '''
    messagebox.showinfo(message=information_message)


class Retiql(customtkinter.CTk):
    '''
        Creating the app for SQL code explainer
    '''

    def __init__(self, fg_color: str | Tuple[str, str] | None = None,
                 **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title('Modely')
        self.geometry("1466X868")

        # Screen components
        # Title
        self.app_name = customtkinter.CTkLabel(
            self, text="Modely", font=customtkinter.CTkFont(
                family='Modern No. 20', size=32,
                weight='bold'))

        self.app_name.pack(pady=12)

        # Description
        self._description_app = customtkinter.CTkLabel(
            self, text=('A DB modeling question generator'),
            font=customtkinter.CTkFont(
                family='Trebuchet MS', slant='italic'),
        )
        self._description_app.pack()

        # Input context field
        self.input_output_frame = customtkinter.CTkFrame(
            self, fg_color=("gray100", "gray15"))
        self.input_output_frame.pack(pady=10)

        self.input_frame = customtkinter.CTkFrame(self.input_output_frame)
        self.input_frame.pack(padx=10, side="left")

        self.input_label = customtkinter.CTkLabel(
            self.input_frame, text="Context", font=customtkinter.CTkFont(
                family="Yu Gothic UI Semibold"))
        self.input_label.pack()

        self.input_textarea = customtkinter.CTkTextbox(
            self.input_frame, width=550, height=400,
            font=customtkinter.CTkFont(family="Yu Gothic UI Semibold"),
            corner_radius=0, wrap="none")
        self.input_textarea.insert(1.0, "Insert your modeling context here.")
        self.input_textarea.pack()

        # Generate questionary from context button
        self.generate_questionary_button = customtkinter.CTkButton(
            self.input_frame, text='Generate',
            fg_color=("green"), hover_color=('#19692c'),
            command=self.generate_questionnarie,
            font=customtkinter.CTkFont(family="@Yu Gothic UI", weight="bold"))
        self.generate_questionary_button.pack(side='right', pady=10, padx=10)

        # Clear context button
        self.clear_button = customtkinter.CTkButton(
            self.input_frame, text='Clear',
            fg_color='red',
            hover_color=("#DB3E39", "#821D1A"),
            command=self.clear_input,
            font=customtkinter.CTkFont(family="@Yu Gothic UI", weight="bold")
        )
        self.clear_button.pack(side="right", pady=10, padx=10)

        self.question_label = None

    def generate_questionnarie(self):
        self.input_frame.forget()

    def clear_input(self):
        '''
            Clear context from input textarea
        '''
        self.input_textarea.delete("0.0", END)


if __name__ == '__main__':
    retiql = Retiql()
    retiql.mainloop()
