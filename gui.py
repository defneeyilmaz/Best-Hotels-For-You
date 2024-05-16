import csv
import tkinter.ttk
from tkinter import *
import customtkinter
from tkcalendar import DateEntry
import datetime
from CTkTable import *
from scraping import *
import csv


def format_date(date):
    values = date.split("/")
    formatted_date = "20" + values[2] + "-"
    if len(values[0]) == 1:
        formatted_date += "0" + values[0] + "-"
    else:
        formatted_date += values[0]
    if len(values[1]) == 1:
        formatted_date += "0" + values[1]
    else:
        formatted_date += values[1]
    return formatted_date


class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = customtkinter.CTkFrame(master=self, fg_color="#00246B")
        self.my_frame.grid(row=0, column=0, padx=210, pady=200, sticky="nsew")
        self.title("Best Hotels For You")
        self.set_title("Best Hotels For You!", 0.5, 0.07, 40)
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
        self.label("Currency:", 0.616, 0.15, 20)
        self.button("Search", 0.8, 0.15, 20)
        self.table = self.table(240, 220, 20)

        customtkinter.set_appearance_mode("light")

    def search(self):
        self.table = self.table(220, 200, 20)
        selected_city = str(self.dropdown_var.get())
        selected_checkin_date = format_date(str(self.checkin_date.get()))
        selected_checkout_date = format_date(str(self.checkout_date.get()))
        selected_currency = self.radio_event()
        scrape(selected_city, selected_checkin_date, selected_checkout_date)
        self.update_table(self.file_reading(), self.table)

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
        calendar = DateEntry(master=self, width=10, year=today.year, month=today.month, day=today.day, relief=FLAT,
                             background="#CADCFC", foreground="#00246B", borderwidth=8, textvariable=variable,
                             font=("Helvetica", fontsize), mindate=today, date_format="%Y-%m-%d")
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

    def table(self, relx, rely, fontsize):
        value = [["Name", "Address", "Distance to City Center", "Review Score", "Price"], ["", "", "", "", ""],
                 ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]
        table = CTkTable(master=self, font=("Helvetica", fontsize, "bold"), text_color="#00246B", values=value,
                         border_width=0, header_color="#CADCFC", anchor="c", height=90, width=280,
                         justify="center", bg_color="#00246B", row=6, column=5, state="readonly")
        table.grid(row=0, column=0, padx=relx, pady=rely)
        return table

    def file_reading(self):
        hotelsfile = open("test_hotels.csv")
        type(hotelsfile)
        filereader = csv.reader(hotelsfile)
        infos = []
        for row in filereader:
            infos.append(row)
        hotelsfile.close()
        return infos

    def update_table(self, hotels, table):
        value = [["Name", "Address", "Distance to City Center", "Review Score", "Price"], hotels[1], hotels[2],
                 hotels[3], hotels[4], hotels[5]]
        table.update_values(values=value)
        for x in range(1, 6):
            table.edit_row(row=x, font=("Helvetica", 18))

    def loop(self):
        self.mainloop()
