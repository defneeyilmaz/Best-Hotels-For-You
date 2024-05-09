from tkinter import *
import customtkinter
from tkcalendar import DateEntry
import datetime


class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Best Hotels For You")
        self.set_title("Best Hotels For You!", 0.5, 0.05, 40)
        self.dropdown(0.15, 0.18, 20, ["Barcelona", "Rome", "Budapest", "Paris", "Berlin",
                                       "London", "Stockholm", "Prague", "Salzburg", "Munich",
                                       "Porto", "Florence", "Bruges", "Vienna", "Amsterdam"])
        self.label("Cities", 0.127, 0.15, 20)
        self.calendar(0.28, 0.18, 12)
        self.label("Check-in Date", 0.278, 0.15, 20)
        self.calendar(0.4, 0.18, 12)
        self.label("Check-out Date", 0.398, 0.15, 20)
        customtkinter.set_appearance_mode("light")

    def button(self, name, relx, rely):
        button = customtkinter.CTkButton(master=self, text=name)
        button.place(relx=relx, rely=rely, anchor=CENTER)

    def set_title(self, name, relx, rely, fontsize):
        label = customtkinter.CTkLabel(master=self, text=name, font=('Helvetica', fontsize), text_color="#00246B",
                                       fg_color="#CADCFC", corner_radius=8)
        label.place(relx=relx, rely=rely, anchor=CENTER)

    def label(self, name, relx, rely, fontsize):
        label = customtkinter.CTkLabel(master=self, text=name, font=('Helvetica', fontsize), text_color="#00246B",
                                       corner_radius=8)
        label.place(relx=relx, rely=rely, anchor=CENTER)

    def dropdown(self, relx, rely, fontsize, values):
        dropdown = customtkinter.CTkComboBox(master=self, values=values,font=("Helvetica", fontsize), fg_color="#CADCFC"
                                             , border_color="#CADCFC", text_color="#00246B", button_color="#A8A8A8",
                                             dropdown_fg_color="#CADCFC", dropdown_text_color="#00246B", button_hover_color="#000000")
        dropdown.place(relx=relx, rely=rely, anchor=CENTER)

    def calendar(self, relx, rely, fontsize):
        today = datetime.date.today()
        calendar = DateEntry(master=self, width=12, year=today.year, month=today.month, day=today.day, background='#CADCFC', foreground='#00246B', borderwidth=8, relief=FLAT, font=("Helvetica", fontsize))
        calendar.place(relx=relx, rely=rely, anchor=CENTER)

    def loop(self):
        self.mainloop()
