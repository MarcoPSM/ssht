"""
Created on Feb 19, 1010
@author: marco
"""

from tkinter import *
from ssht.Tunnel import Tunnel


class ConfigPage(Frame):
    # private var
    __ename = None
    __erhost = None
    __eruser = None
    __erport = None
    __erkey = None
    __erpass = None
    __elhost = None
    __elport = None
    __edescr = None

    tunnel = None
    action = None

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is config page", font=controller.title_font)
        label.pack(side=TOP, fill=X, pady=10)

    def set_tunnel(self, t):
        self.tunnel = t

    def set_action(self, a):
        self.action = a

    def load_form(self):
        fname = Frame(self)
        fname.pack(fill=X)
        lname = Label(fname, text="Nome", width=10, justify=LEFT, fg='blue', anchor=W)
        lname.pack(side=LEFT, padx=5, pady=2)
        self.__ename = Entry(fname)
        self.__ename.insert(END, self.tunnel._get_name())
        self.__ename.pack(fill=X, padx=5, expand=True)

        frhost = Frame(self)
        frhost.pack(fill=X)
        lrhost = Label(frhost, text="Remote host", width=10, justify=LEFT, fg='blue', anchor=W)
        lrhost.pack(side=LEFT, padx=5, pady=2)
        self.__erhost = Entry(frhost)
        self.__erhost.insert(END, self.tunnel._get_remote_host())
        self.__erhost.pack(fill=X, padx=5, expand=True)

        fruser = Frame(self)
        fruser.pack(fill=X)
        lruser = Label(fruser, text="Remote user", width=10, justify=LEFT, fg='blue', anchor=W)
        lruser.pack(side=LEFT, padx=5, pady=2)
        self.__eruser = Entry(fruser)
        self.__eruser.insert(END, self.tunnel._get_remote_user())
        self.__eruser.pack(fill=X, padx=5, expand=True)

        frport = Frame(self)
        frport.pack(fill=X)
        lrport = Label(frport, text="Remote port", width=10, justify=LEFT, fg='blue', anchor=W)
        lrport.pack(side=LEFT, padx=5, pady=2)
        self.__erport = Entry(frport)
        self.__erport.insert(END, self.tunnel._get_remote_port())
        self.__erport.pack(fill=X, padx=5, expand=True)

        frkey = Frame(self)
        frkey.pack(fill=X)
        lrkey = Label(frkey, text="key", width=10, justify=LEFT, fg='blue', anchor=W)
        lrkey.pack(side=LEFT, padx=5, pady=2)
        self.__erkey = Entry(frkey)
        self.__erkey.insert(END, str(self.tunnel._get_remote_key()))
        self.__erkey.pack(fill=X, padx=5, expand=True)

        flport = Frame(self)
        flport.pack(fill=X)
        llport = Label(flport, text="Local port", width=10, justify=LEFT, fg='blue', anchor=W)
        llport.pack(side=LEFT, padx=5, pady=2)
        self.__elport = Entry(flport)
        self.__elport.insert(END, self.tunnel._get_local_port())
        self.__elport.pack(fill=X, padx=5, expand=True)

        fdescr = Frame(self)
        fdescr.pack(fill=BOTH)
        ldescr = Label(fdescr, text="Description", width=10, justify=LEFT, fg='blue', anchor=W)
        ldescr.pack(side=LEFT, anchor=N, padx=5, pady=2)
        self.__edescr = Text(fdescr, width=30, height=5)
        self.__edescr.insert(END, self.tunnel._get_descr())
        self.__edescr.pack(fill=BOTH, padx=5, pady=2, expand=True)

        toolbar = Frame(self, bd=1, relief=RAISED)
        toolbar.pack(side=BOTTOM, fill=X)
        btn_cancel = Button(toolbar, text='Cancel', command=self.back)
        btn_cancel.pack(side=LEFT, pady=2, padx=5, fill=X, expand=True)
        btn_save = Button(toolbar, text='Save', command=self.save)
        btn_save.pack(side=RIGHT, pady=2, padx=5, fill=X, expand=True)

    def back(self):
        self.controller.show_frame("MainPage")

    def save(self):
        print("save")
        tunnel = {}
        tunnel['name'] = self.__ename.get()
        tunnel['remote_host'] = self.__erhost.get()
        tunnel['remote_user'] = self.__eruser.get()
        tunnel['remote_port'] = int(self.__erport.get())
        tunnel['remote_key'] = self.__erkey.get()
        tunnel['local_port'] = int(self.__elport.get())
        tunnel['descr'] = self.__edescr.get("1.0", END).strip()

        self.tunnel._set_tunnel(tunnel)
        if self.action == 'ADD':
            self.controller.tunnels.append(self.tunnel)

        self.controller.save_tunnels()
        self.back()



