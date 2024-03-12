import tkinter as tk
from tkinter import messagebox, simpledialog

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz Gráfica")

        self.buttons = [
            "MUR", "MURA", "MURAXA", "MURAXAYA", "MURAXAZA", "MURAYAZA", "MURA3",
            "Plano inclinado", "Plano inclinado polea", "Péndulo", "Péndulo resorte",
            "Resorte", "Colisión lineal elástica", "Colisión lineal inelástica"
        ]

        for button_text in self.buttons:
            button = tk.Button(master, text=button_text, command=lambda text=button_text: self.open_dialog(text))
            button.pack()

    def open_dialog(self, button_text):
        if button_text == "MUR":
            variables = self.get_variables(["Velocidad inicial", "Distancia"])
        elif button_text == "MURA":
            variables = self.get_variables(["Velocidad inicial", "X inicial", "Aceleración"])
        elif button_text == "MURAXA":
            variables = self.get_variables(["Velocidad inicial en X", "X inicial", "Aceleración en X",
                                             "Velocidad en Y", "Distancia en Y", "Velocidad en Z", "Distancia en Z"])
        elif button_text == "MURAXAYA":
            variables = self.get_variables(["Velocidad inicial en X", "X inicial", "Aceleración en X",
                                             "Velocidad inicial en Y", "Y inicial","Aceleracion en Y", "Velocidad en Z", "Distancia en Z"])
        elif button_text == "MURAXAZA":
            variables = self.get_variables(["Velocidad inicial en X", "X inicial", "Aceleración en X",
                                             "Velocidad en Y", "distancia en Y ","Velocidad en Z", "Z inicial", "Aceleracion en Z"])
        elif button_text == "MURAYAZA":
            variables = self.get_variables(["Velocidad en X", "distancia en X", "Aceleración en Y",
                                             "Velocidad inicial en Y", "Y inicial","Aceleracion en Z", "Velocdiad inicial", "Aceleracion en Z"])
        elif button_text == "MURA3":
            variables = self.get_variables(["Velocidad inicial en X", "X inicial","Aceleracion en X", "Aceleración en Y",
                                             "Velocidad inicial en Y", "Y inicial","Aceleracion en Z", "Velocdiad inicial", "Aceleracion en Z"])
        elif button_text == "Plano inclinado":
            variables = self.get_variables(["Masa objeto", "angulo de inclinacion"])
        elif button_text == "Plano inclinado polea":
            variables = self.get_variables(["Masa ladrillo 1","masa ladrillo 2","angulo de inclinacion"])
        elif button_text == "Péndulo":
            variables = self.get_variables(["Masa objeto","angulo inicial"])
        elif button_text == "Péndulo resorte":
            variables = self.get_variables(["Masa objeto","angulo inicial","constante del resorte"])
        elif button_text == "Resorte":
            variables = self.get_variables(["Masa objeto","constante del resorte","distancia de compresion"])
        elif button_text == "Colisión lineal elástica":
            variables = self.get_variables(["Masa ladrillo 1","masa ladrillo 2","distancia entre los ladrillos","velocidad inicial ladrillo 1","velocidad inicial ladrillo 2"])
        elif button_text == "Colisión lineal inelástica":
            variables = self.get_variables(["Masa ladrillo 1","masa ladrillo 2","distancia entre los ladrillos","velocidad inicial ladrillo 1","velocidad inicial ladrillo 2"])   
            

            
        if variables:
            messagebox.showinfo("Variables", f"Variables para {button_text}: {variables}")

    def get_variables(self, variable_names):
        variables = []
        for name in variable_names:
            variables.append(simpledialog.askfloat("Variables", f"Ingrese {name}:"))
        return variables

def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
