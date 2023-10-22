import tkinter as tk
from Indicadores.Macro.macro import Macro
from frame_main import FrameMain  # Asegúrate de importar FrameMain desde el módulo frame_main

class Sidebar:

    def __init__(self, frame_main):
        self.frame_main = frame_main  # Guarda una referencia al FrameMain
        self.widget()

    def widget(self):
        sidebar = tk.Frame(self.frame_main, width=100, bg="lightblue")
        sidebar.pack(side="left", fill="y")

        sections = ["Inicio", "Macro", "Micro"]

        for section in sections:
            button = tk.Button(sidebar, text=section, command=lambda s=section: self.on_button_click(s), relief="flat")
            button.pack(fill="x", padx=3, pady=2)

    def on_button_click(self, section):
        if section == "Macro":
            # Crea una instancia de la clase Macro y obtén su contenido
            macro_content = Macro(self.frame_main)
            content = macro_content.get_content()
            self.frame_main.add_content(content)
