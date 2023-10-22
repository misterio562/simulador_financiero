import tkinter as tk

class FrameMain(tk.Frame):
    def __init__(self, root, bg_color="yellow"):
        print("Hola")
        super().__init__(root, bg=bg_color)
        self.pack(side="right", fill="both", expand=True)
        self.current_content = None

    def add_content(self, content):
        if self.current_content:
            self.current_content.destroy()
        content.pack(in_=self, fill="both", expand=True)
        self.current_content = content

    