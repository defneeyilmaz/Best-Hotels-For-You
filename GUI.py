from tkinter import *
import customtkinter


class GUI:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("500x500")
        self.root.title("Best Hotels For You")
        customtkinter.set_appearance_mode("light")

    def button(self, name, relx, rely):
        button_ = customtkinter.CTkButton(master=self.root, text=name)
        button_.place(relx=relx, rely=rely, anchor=CENTER)

    def loop(self):
        self.root.mainloop()
