import tkinter as tk

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Control")

        # Sección de información
        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(pady=20)
        
        self.info_label = tk.Label(self.info_frame, text="Información:")
        self.info_label.pack()
        
        self.info_text = tk.Text(self.info_frame, height=5, width=40)
        self.info_text.pack()

        # Sección de botones
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.button1 = tk.Button(self.button_frame, text="Botón 1", command=self.on_button1_click)
        self.button1.pack(side="left", padx=10)

        self.button2 = tk.Button(self.button_frame, text="Botón 2", command=self.on_button2_click)
        self.button2.pack(side="left", padx=10)

    def on_button1_click(self):
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, "Hiciste clic en el Botón 1")

    def on_button2_click(self):
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, "Hiciste clic en el Botón 2")

if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
