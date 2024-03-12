import tkinter as tk
from tkinter import messagebox, simpledialog

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz Gráfica")

        self.buttons = [
            "MUR", "MURA", "MURAXA", "MURAXAYA", "MURAXAZA", "MURAYAZA",
            "MURA3", "Plano inclinado", "Plano inclinado polea", "Péndulo",
            "Péndulo resorte", "Resorte", "Colisión lineal elástica",
            "Colisión lineal inelástica"
        ]

        for button_text in self.buttons:
            button = tk.Button(master, text=button_text, command=lambda text=button_text: self.open_dialog(text))
            button.pack()

    def open_dialog(self, button_text):
        variables = self.get_variables()
        if variables:
            messagebox.showinfo("Variables", f"Variables para {button_text}: {variables}")

    def get_variables(self):
        variables = []
        variables.append(simpledialog.askfloat("Variables", "Ingrese x inicial:"))
        variables.append(simpledialog.askfloat("Variables", "Ingrese y inicial:"))
        variables.append(simpledialog.askfloat("Variables", "Ingrese z inicial:"))
        variables.append(simpledialog.askfloat("Variables", "Ingrese ángulo inicial:"))
        variables.append(simpledialog.askfloat("Variables", "Ingrese velocidad en x inicial:"))
        variables.append(simpledialog.askfloat("Variables", "Ingrese velocidad en y inicial:"))
        variables.append(simpledialog.askfloat("Variables", "Ingrese velocidad en z inicial:"))
        variables.append(simpledialog.askfloat("Variables", "Ingrese masa del objeto 1:"))
        variables.append(simpledialog.askfloat("Variables", "Ingrese masa del objeto 2:"))
        return variables

def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
