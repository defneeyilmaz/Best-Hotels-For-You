from tkinter import *
import customtkinter
from tkcalendar import Calendar


class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Best Hotels For You")
        self.settitle("Best Hotels For You!", 0.5, 0.05, 40)
        self.dropdown(0.15, 0.18, 20, ["Barcelona", "Rome", "Budapest", "Paris", "Berlin",
                                       "London", "Stockholm", "Prague", "Salzburg", "Munich",
                                       "Porto", "Florence", "Bruges", "Vienna", "Amsterdam"])
        self.label("Cities", 0.127, 0.15, 20)
        customtkinter.set_appearance_mode("dark")

    def button(self, name, relx, rely):
        button = customtkinter.CTkButton(master=self, text=name)
        button.place(relx=relx, rely=rely, anchor=CENTER)

    def settitle(self, name, relx, rely, fontsize):
        label = customtkinter.CTkLabel(master=self, text=name, font=('Helvetica', fontsize), text_color="#DF3C5F",
                                       fg_color="#224193", corner_radius=8)
        label.place(relx=relx, rely=rely, anchor=CENTER)

    def label(self, name, relx, rely, fontsize):
        label = customtkinter.CTkLabel(master=self, text=name, font=('Helvetica', fontsize), text_color="#DF3C5F",
                                       corner_radius=8)
        label.place(relx=relx, rely=rely, anchor=CENTER)

    def dropdown(self, relx, rely, fontsize, values):
        dropdown = customtkinter.CTkComboBox(master=self, values=values,
                                             font=("Helvetica", fontsize), fg_color="#224193", border_color="#224193",
                                             text_color="#DF3C5F", button_color="#4E4E4E", dropdown_fg_color="#224193",
                                             dropdown_text_color="#DF3C5F", button_hover_color="#000000")
        dropdown.place(relx=relx, rely=rely, anchor=CENTER)

    def calendar(self, relx, rely, values):
        calendar = Calendar(master=self, font=("Helvetica", 20), selectmode='day',)

    def loop(self):
        self.mainloop()
