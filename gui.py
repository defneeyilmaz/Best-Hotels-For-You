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
        self.dropdown_var = StringVar()
        self.dropdown(0.22, 0.15, 12, ["Barcelona", "Rome", "Budapest",
                                       "Paris", "Berlin", "London", "Stockholm", "Prague",
                                       "Salzburg", "Munich", "Porto", "Florence", "Bruges",
                                       "Vienna", "Amsterdam"], self.dropdown_var)
        self.label("City:", 0.17, 0.15, 20)
        self.checkin_date = StringVar()
        self.calendar(0.38, 0.15, 12, self.checkin_date)
        self.label("Check-in Date:", 0.31, 0.15, 20)
        self.checkout_date = StringVar()
        self.calendar(0.54, 0.15, 12, self.checkout_date)
        self.label("Check-out Date:", 0.466, 0.15, 20)
        self.radio_var = IntVar()
        self.radio_button(0.67, 0.15, "Euro", 20, 0, self.radio_var)
        self.radio_button(0.717, 0.15, "Turkish Lira", 20, 1, self.radio_var)
        self.label("Currency:", 0.617, 0.15, 20)
        self.button("Search", 0.8, 0.15, 20)
        customtkinter.set_appearance_mode("light")

    def search(self):
        selected_city = f'{self.dropdown_var.get()}'
        selected_checkin_date = f'{self.checkin_date.get()}'
        selected_checkout_date = f'{self.checkout_date.get()}'
        selected_currency = self.radio_event()
        print(str(self.dropdown_var.get()), str(self.checkin_date.get()), str(self.checkout_date.get()), self.radio_event())

    def button(self, name, relx, rely, fontsize):
        button = customtkinter.CTkButton(master=self, text=name, font=('Helvetica', fontsize), command=self.search,
                                         text_color="#CADCFC", fg_color="#00246B", corner_radius=8)
        button.place(relx=relx, rely=rely, anchor=CENTER)

    def set_title(self, name, relx, rely, fontsize):
        label = customtkinter.CTkLabel(master=self, text=name, font=('Helvetica', fontsize), text_color="#00246B",
                                       fg_color="#CADCFC", corner_radius=8)
        label.place(relx=relx, rely=rely, anchor=CENTER)

    def label(self, name, relx, rely, fontsize):
        label = customtkinter.CTkLabel(master=self, text=name, font=('Helvetica', fontsize), text_color="#00246B",
                                       corner_radius=8, fg_color="#CADCFC")
        label.place(relx=relx, rely=rely, anchor=CENTER)

    def dropdown_event(self):
        return self.dropdown_var.get()  # chosen city

    def dropdown(self, relx, rely, fontsize, values, variable):
        dropdown = tkinter.ttk.Combobox(self, textvariable=variable, values=values, font=("Helvetica", fontsize),
                                        width=12, background="#CADCFC")
        dropdown.place(relx=relx, rely=rely, anchor=CENTER)
        dropdown.current(0)
        dropdown.config(state="readonly")

    def calendar(self, relx, rely, fontsize, variable):
        today = datetime.date.today()
        calendar = DateEntry(master=self, width=10, year=today.year, month=today.month, day=today.day,
                             background='#CADCFC', foreground='#00246B', borderwidth=8, relief=FLAT,
                             font=("Helvetica", fontsize), textvariable=variable, mindate=today)
        calendar.place(relx=relx, rely=rely, anchor=CENTER)
        calendar.config(state="readonly")
        if calendar.bind("<Enter>"):
            if variable == self.checkin_date:
                self.checkin_date.set(calendar.entry_kw)
            else:
                self.checkout_date.set(calendar.entry_kw)

    def radio_event(self):
        return f"{self.radio_var.get()}"  # chosen currency

    def radio_button(self, relx, rely, name, fontsize, value, variable):
        radio_var = customtkinter.IntVar(value=value)
        radio_button = customtkinter.CTkRadioButton(master=self, variable=variable, value=value,
                                                    font=("Helvetica", fontsize), command=self.radio_event,
                                                    text_color="#00246B", text=name)
        radio_button.place(relx=relx, rely=rely, anchor=CENTER)

    def loop(self):
        self.mainloop()
