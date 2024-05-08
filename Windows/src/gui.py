import os 
import tkinter as tk
from tkinter import messagebox, simpledialog

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bienvenido a Solve Dynamics")

        """self.background_image = tk.PhotoImage(file="~/Downloads/math.png")

        # Create a label to display the background image
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        """

        self.buttons = [
            "MUR(movimiento rectilineo uniforme)", 
            "MURA(movimiento rectilineo uniforme acelerado)", 
            "MURAXA(movimiento rectilineo uniforme acelerado en el eje x)", 
            "MURAXAYA(movimiento rectilineo uniforme acelerado en ejes x, y)", 
            "MURAXAZA(movimiento rectilineo uniforme acelerado en ejes x,z)", 
            "MURAYAZA(movimiento rectilineo uniforme en ejes y,z)", 
            "MURA3(movimiento rectilineo uniforme acelerado en los 3 ejes)",
            "Plano inclinado", "Plano inclinado polea", "Péndulo", "Péndulo resorte",
            "Resorte", "Colisión lineal elástica", "Colisión lineal inelástica"
        ]
        for idx, button_text in enumerate(self.buttons):
            button = tk.Button(master, text=button_text, command=lambda text=button_text: self.open_dialog(text))
            row = idx // 3  # Calculate row number
            column = idx % 3  # Calculate column number
            button.grid(row=row, column=column, padx=5, pady=5)

    def save_to_file(self, button_text, variables, variable_names):
        folder_path = "dynamic_scenarios"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)  # Create the directory if it doesn't exist
        file_path = f"{folder_path}/data_{button_text}.txt"
        with open(file_path, "w") as file:
            file.write(f"Variables para {button_text}:\n")
            for name, value in zip(variable_names, variables):
                file.write(f"{name}: {value}\n")
            file.write("\n")
    def open_dialog(self, button_text):
        if button_text == "MUR(movimiento rectilineo uniforme)":
            variables = self.get_variables(["Velocidad inicial", "Distancia"])
            variable_names = ["Velocidad inicial", "Distancia"]
        elif button_text == "MURA(movimiento rectilineo uniforme acelerado)":
            variables = self.get_variables(["Velocidad inicial", "X inicial", "Aceleración"])
            variable_names=["Velocidad inicial", "X inicial", "Aceleración"]
        elif button_text == "MURAXA(movimiento rectilineo uniforme acelerado en el eje x)":
            variables = self.get_variables(["Velocidad inicial en X", "X inicial", "Aceleración en X",
                                             "Velocidad en Y", "Distancia en Y", "Velocidad en Z", "Distancia en Z"])
            variable_names=["Velocidad inicial en X", "X inicial", "Aceleración en X",
                                             "Velocidad en Y", "Distancia en Y", "Velocidad en Z", "Distancia en Z"]
        elif button_text == "MURAXAYA(movimiento rectilineo uniforme acelerado en ejes x, y)":
            variables = self.get_variables(["Velocidad inicial en X", "X inicial", "Aceleración en X",
                                             "Velocidad inicial en Y", "Y inicial","Aceleracion en Y", "Velocidad en Z", "Distancia en Z"])
            variable_names=["Velocidad inicial en X", "X inicial", "Aceleración en X",
                                             "Velocidad inicial en Y", "Y inicial","Aceleracion en Y", "Velocidad en Z", "Distancia en Z"]
        elif button_text == "MURAXAZA(movimiento rectilineo uniforme acelerado en ejes x,z)":
            variables = self.get_variables(["Velocidad inicial en X", "X inicial", "Aceleración en X",
                                             "Velocidad en Y", "distancia en Y ","Velocidad en Z", "Z inicial", "Aceleracion en Z"])
            variable_names=["Velocidad inicial en X", "X inicial", "Aceleración en X",
                                             "Velocidad en Y", "distancia en Y ","Velocidad en Z", "Z inicial", "Aceleracion en Z"]
        elif button_text == "MURAYAZA(movimiento rectilineo uniforme en ejes y,z)":
            variables = self.get_variables(["Velocidad en X", "distancia en X", "Aceleración en Y",
                                             "Velocidad inicial en Y", "Y inicial","Aceleracion en Z", "Velocdiad inicial", "Aceleracion en Z"])
            variable_names=["Velocidad en X", "distancia en X", "Aceleración en Y",
                                             "Velocidad inicial en Y", "Y inicial","Aceleracion en Z", "Velocdiad inicial", "Aceleracion en Z"]
        elif button_text == "MURA3(movimiento rectilineo uniforme acelerado en los 3 ejes)":
            variables = self.get_variables(["Velocidad inicial en X", "X inicial","Aceleracion en X", "Aceleración en Y",
                                             "Velocidad inicial en Y", "Y inicial","Aceleracion en Z", "Velocdiad inicial", "Aceleracion en Z"])
            variable_names=["Velocidad inicial en X", "X inicial","Aceleracion en X", "Aceleración en Y",
                                             "Velocidad inicial en Y", "Y inicial","Aceleracion en Z", "Velocdiad inicial", "Aceleracion en Z"]
        elif button_text == "Plano inclinado":
            variables = self.get_variables(["Masa objeto", "angulo de inclinacion"])
            variable_names=["Masa objeto", "angulo de inclinacion"]
        elif button_text == "Plano inclinado polea":
            variables = self.get_variables(["Masa ladrillo 1","masa ladrillo 2","angulo de inclinacion"])
            variable_names=["Masa ladrillo 1","masa ladrillo 2","angulo de inclinacion"]
        elif button_text == "Péndulo":
            variables = self.get_variables(["Masa objeto","angulo inicial"])
            variable_names=["Masa objeto","angulo inicial"]
        elif button_text == "Péndulo resorte":
            variables = self.get_variables(["Masa objeto","angulo inicial","constante del resorte"])
            variable_names=["Masa objeto","angulo inicial","constante del resorte"]
        elif button_text == "Resorte":
            variables = self.get_variables(["Masa objeto","constante del resorte","distancia de compresion"])
            variable_names=["Masa objeto","constante del resorte","distancia de compresion"]
        elif button_text == "Colisión lineal elástica":
            variables = self.get_variables(["Masa ladrillo 1","masa ladrillo 2","distancia entre los ladrillos","velocidad inicial ladrillo 1","velocidad inicial ladrillo 2"])
            variable_names=["Masa ladrillo 1","masa ladrillo 2","distancia entre los ladrillos","velocidad inicial ladrillo 1","velocidad inicial ladrillo 2"]
        elif button_text == "Colisión lineal inelástica":
            variables = self.get_variables(["Masa ladrillo 1","masa ladrillo 2","distancia entre los ladrillos","velocidad inicial ladrillo 1","velocidad inicial ladrillo 2"])   
            variable_names=["Masa ladrillo 1","masa ladrillo 2","distancia entre los ladrillos","velocidad inicial ladrillo 1","velocidad inicial ladrillo 2"]

        if variables:
            self.save_to_file(button_text.replace(" ", ""),variables,variable_names)
            messagebox.showinfo("Variables", f"Variables para {button_text}: {variables}")
            if button_text == "MUR(movimiento rectilineo uniforme)":
                os.system('python dynamic_scenarios/m_r_u.py')               
            elif button_text == "MURA(movimiento rectilineo uniforme acelerado)":
                os.system('python dynamic_scenarios/m_r_u_a.py')
            elif button_text == "MURAXA(movimiento rectilineo uniforme acelerado en el eje x)":
                os.system('python dynamic_scenarios/m_r_u_xA.py')
            elif button_text == "MURAXAYA(movimiento rectilineo uniforme acelerado en ejes x, y)":
                os.system('python dynamic_scenarios/m_r_u_xA_yA.py')
            elif button_text == "MURAXAZA(movimiento rectilineo uniforme acelerado en ejes x,z)":
                os.system('python dynamic_scenarios/m_r_u_xA_zA.py')
            elif button_text == "MURAYAZA(movimiento rectilineo uniforme en ejes y,z)":
                os.system('python dynamic_scenarios/m_r_u_yA_zA.py')
            elif button_text == "MURA3(movimiento rectilineo uniforme acelerado en los 3 ejes)":
                os.system('python dynamic_scenarios/m_r_u_A_3.py')
            elif button_text == "Plano inclinado":
                os.system('python dynamic_scenarios/plane.py')
            elif button_text == "Plano inclinado polea":
                os.system('python dynamic_scenarios/plane_pole.py')
            elif button_text == "Péndulo":
                os.system('python dynamic_scenarios/pendulum.py')   
            elif button_text == "Péndulo resorte":
                os.system('python dynamic_scenarios/pedulum-spring.py')       
            elif button_text == "Resorte":
                os.system('python dynamic_scenarios/spring.py') 
            elif button_text == "Colisión lineal elástica":
                os.system('python dynamic_scenarios/elastic-collision.py')       
            elif button_text == "Colisión lineal inelástica":
                os.system('python dynamic_scenarios/inelastic-collision.py')       
                                  
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
