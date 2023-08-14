import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import database as db


class App(customtkinter.CTk):

    def __init__(self):
        super(App, self).__init__()

        self.title("PokePy")

        self.btn_create = customtkinter.CTkButton(master=self, text="Create", command=self.btn_create)
        self.btn_create.grid(pady=20, row=1, columnspan=2, sticky="nsew")

        self.btn_read = customtkinter.CTkButton(master=self, text="Read", command=self.btn_read)
        self.btn_read.grid(pady=20, row=2, columnspan=2, sticky="nsew")

        self.btn_update = customtkinter.CTkButton(master=self, text="Update", command=self.btn_update)
        self.btn_update.grid(pady=20, row=3, columnspan=2, sticky="nsew")

        self.btn_delete = customtkinter.CTkButton(master=self, text="Delete", command=self.btn_delete)
        self.btn_delete.grid(pady=20, row=4, columnspan=2, sticky="nsew")

        self.btn_play = customtkinter.CTkButton(master=self, text="Play", command=self.btn_play)
        self.btn_play.grid(pady=20, row=5, columnspan=2, sticky="nsew")

    def btn_create(self):
        pass

    def btn_read(self):
        pass

    def btn_update(self):
        pass

    def btn_delete(self):
        pass

    def btn_play(self):
        multiplayer = question(title="Is multiplayer?", message="Do you want to play alone?")


if __name__ == '__main__':
    app = App()
    app.mainloop()
