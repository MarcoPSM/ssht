"""
Created on Feb 19, 2020
@author: marcopaulomartins@hotmail.com
@summary: Tool to SSH Tunneling
@requires: python 3 / tkinter
"""

import tkinter as tk
from tkinter import font  as tkfont
from ssht.MainPage import MainPage
from ssht.ConfigPage import ConfigPage


class SSHT(tk.Tk):
    tunnels = None
    tunneling = None

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        tk.Tk.title(self, "SSH  TUNNELS  MANAGER")
        tk.Tk.minsize(self, 300, 280)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, ConfigPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name, tunnel=None):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        if page_name == "MainPage":
            for widget in frame.winfo_children():
                widget.destroy()
            frame.load_buttons()
        if page_name == "ConfigPage":
            if tunnel is None:
                tunnel = self.tunneling.get_new_tunnel()
                action = 'ADD'
            else:
                action = 'EDIT'

            frame.set_action(action)
            frame.set_tunnel(tunnel)
            for widget in frame.winfo_children():
                widget.destroy()
            frame.load_form()

        frame.tkraise()

    def save_tunnels(self):
        self.tunneling._save_tunnels(self.tunnels)


if __name__ == "__main__":
    app = SSHT()
    app.mainloop()
