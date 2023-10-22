import tkinter as tk
from sidebar import Sidebar
from frame_main import FrameMain

class Window():

    def __init__(self):
        self.widget()
        

    def widget(self):
        self.root = tk.Tk()
        self.root.title("Simulador financiero")
        self.root.geometry("900x600")


        self.clases()

        self.root.mainloop()

    def clases(self):
        frame_main = FrameMain(self.root)
        sidebar = Sidebar(frame_main)
        
