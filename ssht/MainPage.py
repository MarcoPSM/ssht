"""
Created on Feb 19, 2020
@author: marco
"""

import tkinter as tk
from tkinter import font  as tkfont
from ssht.Tunneling import Tunneling


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        controller.tunneling = Tunneling()
        controller.tunnels = controller.tunneling._get_list()

        self.load_buttons()

    def load_buttons(self):
        # label = tk.Label(self, text="Main Page", font=self.controller.title_font)
        # label.pack(side="top", fill="x", pady=10)

        for t in self.controller.tunnels:
            button_frame = tk.Frame(self)
            button_frame.pack(side="top")
            t_btn = tk.Button(button_frame)
            t_btn["text"] = t._get_name()
            t_btn["height"] = 2
            t_btn["width"] = 25
            if t._is_on():

                t_btn["bg"] = 'green'
            else:
                t_btn["bg"] = 'blue'

            e_btn = tk.Button(button_frame, text="Edit")
            e_btn["height"] = 2
            e_btn["width"] = 2
            e_btn["state"] = tk.NORMAL

            t_btn["command"] = lambda x=(t, t_btn, e_btn): self.change_status(x)
            t_btn.pack(side="left", pady=2, padx=5)

            e_btn["command"] = lambda x=t: self.controller.show_frame("ConfigPage", x)
            e_btn.pack(side="right", pady=2, padx=5)

        self.quit = tk.Button(self, text="ADD TUNNEL", fg="blue",
                              command=lambda: self.controller.show_frame("ConfigPage"))
        self.quit.pack(side="bottom", fill='x')

    def change_status(self, x):
        t = x[0]
        print(t._get_name())
        t_btn = x[1]
        e_btn = x[2]
        if t._is_on():
            t._close()
            t_btn["bg"] = 'blue'
            e_btn["state"] = tk.NORMAL
        else:
            t._open()
            t_btn["bg"] = 'green'
            e_btn["state"] = tk.DISABLED



