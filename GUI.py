from tkinter import *
import customtkinter


class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Best Hotels For You")
        self.label("Best Hotels For You!", 0.5, 0.05, 40)
        customtkinter.set_appearance_mode("dark")

    def button(self, name, relx, rely):
        button = customtkinter.CTkButton(master=self, text=name)
        button.place(relx=relx, rely=rely, anchor=CENTER)

    def label(self, name, relx, rely, fontsize):
        label = customtkinter.CTkLabel(master=self, text=name, font=('Helvetica', fontsize), text_color="#DF3C5F", fg_color="#224193",corner_radius=8)
        label.place(relx=relx, rely=rely, anchor=CENTER)

    def loop(self):
        self.mainloop()
