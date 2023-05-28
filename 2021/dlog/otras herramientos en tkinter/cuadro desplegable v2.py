from tkinter import ttk
import tkinter as tk
class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Combobox")
        
        self.combo = ttk.Combobox(self)
        self.combo.place(x=50, y=50)
        self.combo["values"] = ["Python", "C", "C++", "Java"]
        self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
        
        main_window.configure(width=300, height=200)
        self.place(width=300, height=200)
    
    def selection_changed(self, event):
        print("Nuevo elemento seleccionado:", self.combo.get())
