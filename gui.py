import tkinter.ttk
from tkinter import *
import customtkinter
from tkcalendar import DateEntry
import datetime


class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = customtkinter.CTkFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=200, pady=180, sticky="nsew")
        self.title("Best Hotels For You")
        self.set_title("Best Hotels For You!", 0.5, 0.05, 40)
        self.dropdown(0.25, 0.15, 12, ["Barcelona", "Rome", "Budapest", "Paris", "Berlin",
                                       "London", "Stockholm", "Prague", "Salzburg", "Munich",
                                       "Porto", "Florence", "Bruges", "Vienna", "Amsterdam"])
        self.label("City:", 0.2, 0.15, 20)
        self.calendar(0.4, 0.15, 12)
        self.label("Check-in Date:", 0.33, 0.15, 20)
        self.calendar(0.56, 0.15, 12)
        self.label("Check-out Date:", 0.49, 0.15, 20)
        self.radio_var = IntVar()
        self.radio_button(0.7, 0.15, "Euro", 20, 0, self.radio_var)
        self.radio_button(0.76, 0.15, "Turkish Lira", 20, 1, self.radio_var)
        self.label("Currency:", 0.64, 0.15, 20)
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
        n = tkinter.StringVar()
        dropdown = tkinter.ttk.Combobox(self, textvariable=n, values=values, font=("Helvetica", fontsize), width=12,
                                        background="#CADCFC")
        dropdown.place(relx=relx, rely=rely, anchor=CENTER)
        dropdown.config(state="readonly")

    def calendar(self, relx, rely, fontsize):
        today = datetime.date.today()
        calendar = DateEntry(master=self, width=8, year=today.year, month=today.month, day=today.day,
                             background='#CADCFC', foreground='#00246B', borderwidth=8, relief=FLAT,
                             font=("Helvetica", fontsize))
        calendar.place(relx=relx, rely=rely, anchor=CENTER)
        calendar.config(state="readonly")

    def radio_event(self):
        choosen_price = f"{self.radio_var.get()}"

    def radio_button(self, relx, rely, name, fontsize, value, variable):
        radio_var = customtkinter.IntVar(value=value)
        radio_button = customtkinter.CTkRadioButton(master=self, variable=variable, value=value,
                                                    font=("Helvetica", fontsize), command=self.radio_event,
                                                    text_color="#00246B", text=name)
        radio_button.place(relx=relx, rely=rely, anchor=CENTER)

    def loop(self):
        self.mainloop()
