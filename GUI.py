from tkinter import *
import customtkinter


class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Best Hotels For You")
        customtkinter.set_appearance_mode("light")

    def button(self, name, relx, rely):
        button = customtkinter.CTkButton(master=self, text=name)

        button.place(relx=relx, rely=rely, anchor=CENTER)

    def loop(self):
        self.mainloop()
