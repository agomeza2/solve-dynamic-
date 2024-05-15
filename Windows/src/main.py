import sys
import os
import subprocess

from PyQt5 import QtWidgets
from desingPy.main import Ui_MainWindow

# Importar los dialogos de cada simulacion
from desingPy.mur import Ui_DialogMur
from desingPy.mura import Ui_DialogMura
from desingPy.muraxa import Ui_DialogMuraxa
from desingPy.muraxaya import Ui_DialogMuraxaya
from desingPy.muraxaza import Ui_DialogMuraxaza
from desingPy.murayaza import Ui_DialogMurayaza
from desingPy.mura3 import Ui_DialogMura3
from desingPy.planoInclinado import Ui_DialogPlanoInclinado
from desingPy.planoInclinadoPolea import Ui_DialogPlanoInclinadoPolea
from desingPy.pendulo import Ui_DialogPendulo
from desingPy.penduloResorte import Ui_DialogPenduloResorte
from desingPy.resorte import Ui_DialogResorte
from desingPy.colisionLinealElastica import Ui_DialogColisionLinealElastica
from desingPy.colisionLinealInelastica import Ui_DialogColisionLinealInelastica

class MurDialog(QtWidgets.QDialog, Ui_DialogMur):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):
        # Obtener el texto de inptVelocidadInicial y inptDistanciaLadrillos
        velocidad_text = self.inptVelocidadInicial.text()
        distancia_text = self.inptDistanciaLadrillos.text()

        # Verificar si los textos son números enteros
        try:
            velocidad = int(velocidad_text)
            distancia = int(distancia_text)
        except ValueError:
            if not velocidad_text.isdigit():
                self.lblErrorVelocidadInicial.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicial.clear()

            if not distancia_text.isdigit():
                self.lblErrorDistanciaLadrillos.setText("Dato incorrecto")
            else:
                self.lblErrorDistanciaLadrillos.clear()
            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_MUR(movimientorectilineouniforme).txt')
        with open(archivo, 'w') as f:
            f.write("Variables para MUR(movimientorectilineouniforme):\n")
            f.write(f"Velocidad inicial: {velocidad}\n")
            f.write(f"Distancia: {distancia}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorVelocidadInicial.clear()
        self.lblErrorDistanciaLadrillos.clear()

        self.inptVelocidadInicial.clear()
        self.inptDistanciaLadrillos.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script m_r_u.py desde la carpeta actual
        subprocess.run(['python', 'm_r_u.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.inptVelocidadInicial.clear()
        self.lblErrorVelocidadInicial.clear()

        self.inptDistanciaLadrillos.clear()
        self.lblErrorDistanciaLadrillos.clear()

        self.close()

class MuraDialog(QtWidgets.QDialog, Ui_DialogMura):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):
        # Obtener el texto de inptVelocidadInicial y inptDistanciaLadrillos
        velocidad_text = self.inptVelocidadInicial.text()
        posicion_text = self.inptPosicionX.text()
        aceleracion_text = self.inptAceleracion.text()

        # Verificar si los textos son números enteros
        try:
            velocidad = int(velocidad_text)
            posicion = int(posicion_text)
            aceleracion = int(aceleracion_text)
        except ValueError:
            if not velocidad_text.isdigit():
                self.lblErrorVelocidadInicial.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicial.clear()

            if not posicion_text.isdigit():
                self.lblErrorPosicionX.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionX.clear()

            if not aceleracion_text.isdigit():
                self.lblErrorAceleracion.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracion.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_MURA(movimientorectilineouniformeacelerado).txt')
        with open(archivo, 'w') as f:

            f.write("Variables para MURA(movimientorectilineouniformeacelerado):\n")
            f.write(f"Velocidad inicial: {velocidad}\n")
            f.write(f"X inicial: {posicion}\n")
            f.write(f"Aceleración: {aceleracion}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorVelocidadInicial.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracion.clear()

        self.inptVelocidadInicial.clear()
        self.inptPosicionX.clear()
        self.inptAceleracion.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script m_r_u_a.py desde la carpeta actual
        subprocess.run(['python', 'm_r_u_a.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.inptVelocidadInicial.clear()
        self.lblErrorVelocidadInicial.clear()

        self.inptPosicionX.clear()
        self.lblErrorPosicionX.clear()

        self.inptAceleracion.clear()
        self.lblErrorAceleracion.clear()

        self.close()

class MuraxaDialog(QtWidgets.QDialog, Ui_DialogMuraxa):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):
        # Obtener el texto de inptVelocidadInicial y inptDistanciaLadrillos
        velocidadX_text = self.inptVelocidadInicialX.text()
        posicionX_text = self.inptPosicionX.text()
        aceleracionX_text = self.inptAceleracionX.text()

        velocidadY_text = self.inptVelocidadInicialY.text()
        posicionY_text = self.inptPosicionY.text()

        velocidadZ_text = self.inptVelocidadInicialZ.text()
        posicionZ_text = self.inptPosicionZ.text()

        # Verificar si los textos son números enteros
        try:
            velocidadX = int(velocidadX_text)
            posicionX = int(posicionX_text)
            aceleracionX = int(aceleracionX_text)

            velocidadY = int(velocidadY_text)
            posicionY = int(posicionY_text)

            velocidadZ = int(velocidadZ_text)
            posicionZ = int(posicionZ_text)

        except ValueError:
            if not velocidadX_text.isdigit():
                self.lblErrorVelocidadInicialX.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialX.clear()

            if not posicionX_text.isdigit():
                self.lblErrorPosicionX.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionX.clear()

            if not aceleracionX_text.isdigit():
                self.lblErrorAceleracionX.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracionX.clear()

            if not velocidadY_text.isdigit():
                self.lblErrorVelocidadInicialY.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialY.clear()

            if not posicionY_text.isdigit():
                self.lblErrorPosicionY.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionY.clear()

            if not velocidadZ_text.isdigit():
                self.lblErrorVelocidadInicialZ.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialZ.clear()

            if not posicionZ_text.isdigit():
                self.lblErrorPosicionZ.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionZ.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_MURAXA(movimientorectilineouniformeaceleradoenelejex).txt')
        with open(archivo, 'w') as f:
            f.write("Variables para MURAXA(movimientorectilineouniformeaceleradoenelejex):\n")
            f.write(f"Velocidad inicial en X: {velocidadX}\n")
            f.write(f"X inicial: {posicionX}\n")
            f.write(f"Aceleración en X: {aceleracionX}\n")
            f.write(f"Velocidad en Y: {velocidadY}\n")
            f.write(f"Distancia en Y: {posicionY}\n")
            f.write(f"Velocidad en Z: {velocidadZ}\n")
            f.write(f"Distancia en Z: {posicionZ}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorVelocidadInicialX.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracionX.clear()

        self.lblErrorVelocidadInicialY.clear()
        self.lblErrorPosicionY.clear()

        self.lblErrorVelocidadInicialZ.clear()
        self.lblErrorPosicionZ.clear()

        self.inptVelocidadInicialX.clear()
        self.inptPosicionX.clear()
        self.inptAceleracionX.clear()

        self.inptPosicionY.clear()
        self.inptVelocidadInicialY.clear()

        self.inptPosicionZ.clear()
        self.inptVelocidadInicialZ.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script m_r_u_xA.py desde la carpeta actual
        subprocess.run(['python', 'm_r_u_xA.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorVelocidadInicialX.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracionX.clear()

        self.lblErrorVelocidadInicialY.clear()
        self.lblErrorPosicionY.clear()

        self.lblErrorVelocidadInicialZ.clear()
        self.lblErrorPosicionZ.clear()

        self.inptVelocidadInicialX.clear()
        self.inptPosicionX.clear()
        self.inptAceleracionX.clear()

        self.inptPosicionY.clear()
        self.inptVelocidadInicialY.clear()

        self.inptPosicionZ.clear()
        self.inptVelocidadInicialZ.clear()

        self.close()

class MuraxayaDialog(QtWidgets.QDialog, Ui_DialogMuraxaya):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):
        # Obtener el texto de inptVelocidadInicial y inptDistanciaLadrillos
        velocidadX_text = self.inptVelocidadInicialX.text()
        posicionX_text = self.inptPosicionX.text()
        aceleracionX_text = self.inptAceleracionX.text()

        velocidadY_text = self.inptVelocidadInicialY.text()
        posicionY_text = self.inptPosicionY.text()
        aceleracionY_text = self.inptAceleracionY.text()

        velocidadZ_text = self.inptVelocidadInicialZ.text()
        posicionZ_text = self.inptPosicionZ.text()

        # Verificar si los textos son números enteros
        try:
            velocidadX = int(velocidadX_text)
            posicionX = int(posicionX_text)
            aceleracionX = int(aceleracionX_text)

            velocidadY = int(velocidadY_text)
            posicionY = int(posicionY_text)
            aceleracionY = int(aceleracionY_text)

            velocidadZ = int(velocidadZ_text)
            posicionZ = int(posicionZ_text)

        except ValueError:
            if not velocidadX_text.isdigit():
                self.lblErrorVelocidadInicialX.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialX.clear()

            if not posicionX_text.isdigit():
                self.lblErrorPosicionX.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionX.clear()

            if not aceleracionX_text.isdigit():
                self.lblErrorAceleracionX.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracionX.clear()

            if not velocidadY_text.isdigit():
                self.lblErrorVelocidadInicialY.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialY.clear()

            if not posicionY_text.isdigit():
                self.lblErrorPosicionY.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionY.clear()
            if not aceleracionY_text.isdigit():
                self.lblErrorAceleracionY.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracionY.clear()

            if not velocidadZ_text.isdigit():
                self.lblErrorVelocidadInicialZ.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialZ.clear()

            if not posicionZ_text.isdigit():
                self.lblErrorPosicionZ.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionZ.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_MURAXAYA(movimientorectilineouniformeaceleradoenejesx,y).txt')
        with open(archivo, 'w') as f:
            f.write("Variables para MURAXAYA(movimientorectilineouniformeaceleradoenejesx,y):\n")
            f.write(f"Velocidad inicial en X: {velocidadX}\n")
            f.write(f"X inicial: {posicionX}\n")
            f.write(f"Aceleración en X: {aceleracionX}\n")
            f.write(f"Velocidad en Y: {velocidadY}\n")
            f.write(f"Distancia en Y: {posicionY}\n")
            f.write(f"Aceleración en Y: {aceleracionY}\n")
            f.write(f"Velocidad en Z: {velocidadZ}\n")
            f.write(f"Distancia en Z: {posicionZ}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorVelocidadInicialX.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracionX.clear()

        self.lblErrorVelocidadInicialY.clear()
        self.lblErrorPosicionY.clear()
        self.lblErrorAceleracionY.clear()

        self.lblErrorVelocidadInicialZ.clear()
        self.lblErrorPosicionZ.clear()

        self.inptVelocidadInicialX.clear()
        self.inptPosicionX.clear()
        self.inptAceleracionX.clear()

        self.inptPosicionY.clear()
        self.inptVelocidadInicialY.clear()
        self.inptAceleracionY.clear()

        self.inptPosicionZ.clear()
        self.inptVelocidadInicialZ.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script m_r_u_xA_yA.py desde la carpeta actual
        subprocess.run(['python', 'm_r_u_xA_yA.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorVelocidadInicialX.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracionX.clear()

        self.lblErrorVelocidadInicialY.clear()
        self.lblErrorPosicionY.clear()
        self.lblErrorAceleracionY.clear()

        self.lblErrorVelocidadInicialZ.clear()
        self.lblErrorPosicionZ.clear()

        self.inptVelocidadInicialX.clear()
        self.inptPosicionX.clear()
        self.inptAceleracionX.clear()

        self.inptPosicionY.clear()
        self.inptVelocidadInicialY.clear()
        self.inptAceleracionY.clear()

        self.inptPosicionZ.clear()
        self.inptVelocidadInicialZ.clear()

        self.close()

class MuraxazaDialog(QtWidgets.QDialog, Ui_DialogMuraxaza):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):
        # Obtener el texto de inptVelocidadInicial y inptDistanciaLadrillos
        velocidadX_text = self.inptVelocidadInicialX.text()
        posicionX_text = self.inptPosicionX.text()
        aceleracionX_text = self.inptAceleracionX.text()

        velocidadY_text = self.inptVelocidadInicialY.text()
        posicionY_text = self.inptPosicionY.text()

        velocidadZ_text = self.inptVelocidadInicialZ.text()
        posicionZ_text = self.inptPosicionZ.text()
        aceleracionZ_text = self.inptAceleracionZ.text()

        # Verificar si los textos son números enteros
        try:
            velocidadX = int(velocidadX_text)
            posicionX = int(posicionX_text)
            aceleracionX = int(aceleracionX_text)

            velocidadY = int(velocidadY_text)
            posicionY = int(posicionY_text)

            velocidadZ = int(velocidadZ_text)
            posicionZ = int(posicionZ_text)
            aceleracionZ = int(aceleracionZ_text)

        except ValueError:
            if not velocidadX_text.isdigit():
                self.lblErrorVelocidadInicialX.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialX.clear()

            if not posicionX_text.isdigit():
                self.lblErrorPosicionX.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionX.clear()

            if not aceleracionX_text.isdigit():
                self.lblErrorAceleracionX.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracionX.clear()

            if not velocidadY_text.isdigit():
                self.lblErrorVelocidadInicialY.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialY.clear()

            if not posicionY_text.isdigit():
                self.lblErrorPosicionY.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionY.clear()

            if not velocidadZ_text.isdigit():
                self.lblErrorVelocidadInicialZ.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialZ.clear()

            if not posicionZ_text.isdigit():
                self.lblErrorPosicionZ.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionZ.clear()
            if not aceleracionZ_text.isdigit():
                self.lblErrorAceleracionZ.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracionZ.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_MURAXAZA(movimientorectilineouniformeenejesx,z).txt')
        with open(archivo, 'w') as f:
            f.write("Variables para MURAXAZA(movimientorectilineouniformeenejesx,z):\n")
            f.write(f"Velocidad inicial en X: {velocidadX}\n")
            f.write(f"X inicial: {posicionX}\n")
            f.write(f"Aceleración en X: {aceleracionX}\n")
            f.write(f"Velocidad en Y: {velocidadY}\n")
            f.write(f"Distancia en Y: {posicionY}\n")
            f.write(f"Velocidad en Z: {velocidadZ}\n")
            f.write(f"Distancia en Z: {posicionZ}\n")
            f.write(f"Aceleración en Z: {aceleracionZ}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorVelocidadInicialX.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracionX.clear()

        self.lblErrorVelocidadInicialY.clear()
        self.lblErrorPosicionY.clear()

        self.lblErrorVelocidadInicialZ.clear()
        self.lblErrorPosicionZ.clear()
        self.lblErrorAceleracionZ.clear()

        self.inptVelocidadInicialX.clear()
        self.inptPosicionX.clear()
        self.inptAceleracionX.clear()

        self.inptPosicionY.clear()
        self.inptVelocidadInicialY.clear()

        self.inptPosicionZ.clear()
        self.inptVelocidadInicialZ.clear()
        self.inptAceleracionZ.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script m_r_u_xA_zA.py desde la carpeta actual
        subprocess.run(['python', 'm_r_u_xA_zA.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorVelocidadInicialX.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracionX.clear()

        self.lblErrorVelocidadInicialY.clear()
        self.lblErrorPosicionY.clear()

        self.lblErrorVelocidadInicialZ.clear()
        self.lblErrorPosicionZ.clear()
        self.lblErrorAceleracionZ.clear()

        self.inptVelocidadInicialX.clear()
        self.inptPosicionX.clear()
        self.inptAceleracionX.clear()

        self.inptPosicionY.clear()
        self.inptVelocidadInicialY.clear()

        self.inptPosicionZ.clear()
        self.inptVelocidadInicialZ.clear()
        self.inptAceleracionZ.clear()

        self.close()

class MurayazaDialog(QtWidgets.QDialog, Ui_DialogMurayaza):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):
        # Obtener el texto de inptVelocidadInicial y inptDistanciaLadrillos
        velocidadX_text = self.inptVelocidadInicialX.text()
        posicionX_text = self.inptPosicionX.text()
        aceleracionX_text = self.inptAceleracionX.text()

        velocidadY_text = self.inptVelocidadInicialY.text()
        posicionY_text = self.inptPosicionY.text()

        velocidadZ_text = self.inptVelocidadInicialZ.text()
        posicionZ_text = self.inptPosicionZ.text()
        aceleracionZ_text = self.inptAceleracionZ.text()

        # Verificar si los textos son números enteros
        try:
            velocidadX = int(velocidadX_text)
            posicionX = int(posicionX_text)
            aceleracionX = int(aceleracionX_text)

            velocidadY = int(velocidadY_text)
            posicionY = int(posicionY_text)

            velocidadZ = int(velocidadZ_text)
            posicionZ = int(posicionZ_text)
            aceleracionZ = int(aceleracionZ_text)

        except ValueError:
            if not velocidadX_text.isdigit():
                self.lblErrorVelocidadInicialX.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialX.clear()

            if not posicionX_text.isdigit():
                self.lblErrorPosicionX.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionX.clear()

            if not aceleracionX_text.isdigit():
                self.lblErrorAceleracionX.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracionX.clear()

            if not velocidadY_text.isdigit():
                self.lblErrorVelocidadInicialY.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialY.clear()

            if not posicionY_text.isdigit():
                self.lblErrorPosicionY.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionY.clear()

            if not velocidadZ_text.isdigit():
                self.lblErrorVelocidadInicialZ.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialZ.clear()

            if not posicionZ_text.isdigit():
                self.lblErrorPosicionZ.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionZ.clear()
            if not aceleracionZ_text.isdigit():
                self.lblErrorAceleracionZ.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracionZ.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_MURAYAZA(movimientorectilineouniformeenejesy,z).txt')
        with open(archivo, 'w') as f:
            f.write("Variables para MURAYAZA(movimientorectilineouniformeenejesy,z):\n")
            f.write(f"Velocidad inicial en X: {velocidadX}\n")
            f.write(f"X inicial: {posicionX}\n")
            f.write(f"Aceleración en X: {aceleracionX}\n")
            f.write(f"Velocidad en Y: {velocidadY}\n")
            f.write(f"Distancia en Y: {posicionY}\n")
            f.write(f"Velocidad en Z: {velocidadZ}\n")
            f.write(f"Distancia en Z: {posicionZ}\n")
            f.write(f"Aceleración en Z: {aceleracionZ}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorVelocidadInicialX.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracionX.clear()

        self.lblErrorVelocidadInicialY.clear()
        self.lblErrorPosicionY.clear()

        self.lblErrorVelocidadInicialZ.clear()
        self.lblErrorPosicionZ.clear()
        self.lblErrorAceleracionZ.clear()

        self.inptVelocidadInicialX.clear()
        self.inptPosicionX.clear()
        self.inptAceleracionX.clear()

        self.inptPosicionY.clear()
        self.inptVelocidadInicialY.clear()

        self.inptPosicionZ.clear()
        self.inptVelocidadInicialZ.clear()
        self.inptAceleracionZ.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script m_r_u_xA_zA.py desde la carpeta actual
        subprocess.run(['python', 'm_r_u_xA_zA.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorVelocidadInicialX.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracionX.clear()

        self.lblErrorVelocidadInicialY.clear()
        self.lblErrorPosicionY.clear()

        self.lblErrorVelocidadInicialZ.clear()
        self.lblErrorPosicionZ.clear()
        self.lblErrorAceleracionZ.clear()

        self.inptVelocidadInicialX.clear()
        self.inptPosicionX.clear()
        self.inptAceleracionX.clear()

        self.inptPosicionY.clear()
        self.inptVelocidadInicialY.clear()

        self.inptPosicionZ.clear()
        self.inptVelocidadInicialZ.clear()
        self.inptAceleracionZ.clear()

        self.close()

class Mura3Dialog(QtWidgets.QDialog, Ui_DialogMura3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):
        # Obtener el texto de inptVelocidadInicial y inptDistanciaLadrillos
        velocidadX_text = self.inptVelocidadInicialX.text()
        posicionX_text = self.inptPosicionX.text()
        aceleracionX_text = self.inptAceleracionX.text()

        velocidadY_text = self.inptVelocidadInicialY.text()
        posicionY_text = self.inptPosicionY.text()
        aceleracionY_text = self.inptAceleracionY.text()

        velocidadZ_text = self.inptVelocidadInicialZ.text()
        posicionZ_text = self.inptPosicionZ.text()
        aceleracionZ_text = self.inptAceleracionZ.text()

        # Verificar si los textos son números enteros
        try:
            velocidadX = int(velocidadX_text)
            posicionX = int(posicionX_text)
            aceleracionX = int(aceleracionX_text)

            velocidadY = int(velocidadY_text)
            posicionY = int(posicionY_text)
            aceleracionY = int(aceleracionY_text)

            velocidadZ = int(velocidadZ_text)
            posicionZ = int(posicionZ_text)
            aceleracionZ = int(aceleracionZ_text)

        except ValueError:
            if not velocidadX_text.isdigit():
                self.lblErrorVelocidadInicialX.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialX.clear()

            if not posicionX_text.isdigit():
                self.lblErrorPosicionX.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionX.clear()

            if not aceleracionX_text.isdigit():
                self.lblErrorAceleracionX.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracionX.clear()

            if not velocidadY_text.isdigit():
                self.lblErrorVelocidadInicialY.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialY.clear()

            if not posicionY_text.isdigit():
                self.lblErrorPosicionY.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionY.clear()

            if not aceleracionY_text.isdigit():
                self.lblErrorAceleracionY.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracionY.clear()

            if not velocidadZ_text.isdigit():
                self.lblErrorVelocidadInicialZ.setText("Dato incorrecto")
            else:
                self.lblErrorVelocidadInicialZ.clear()

            if not posicionZ_text.isdigit():
                self.lblErrorPosicionZ.setText("Dato incorrecto")
            else:
                self.lblErrorPosicionZ.clear()
            if not aceleracionZ_text.isdigit():
                self.lblErrorAceleracionZ.setText("Dato incorrecto")
            else:
                self.lblErrorAceleracionZ.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_MURA3(movimientorectilineouniformeaceleradoenlos3ejes).txt')
        with open(archivo, 'w') as f:
            f.write("Variables para MURA3(movimientorectilineouniformeaceleradoenlos3ejes):\n")
            f.write(f"Velocidad inicial en X: {velocidadX}\n")
            f.write(f"X inicial: {posicionX}\n")
            f.write(f"Aceleración en X: {aceleracionX}\n")
            f.write(f"Velocidad en Y: {velocidadY}\n")
            f.write(f"Distancia en Y: {posicionY}\n")
            f.write(f"Aceleración en Y: {aceleracionY}\n")
            f.write(f"Velocidad en Z: {velocidadZ}\n")
            f.write(f"Distancia en Z: {posicionZ}\n")
            f.write(f"Aceleración en Z: {aceleracionZ}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorVelocidadInicialX.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracionX.clear()

        self.lblErrorVelocidadInicialY.clear()
        self.lblErrorPosicionY.clear()
        self.lblErrorAceleracionY.clear()

        self.lblErrorVelocidadInicialZ.clear()
        self.lblErrorPosicionZ.clear()
        self.lblErrorAceleracionZ.clear()

        self.inptVelocidadInicialX.clear()
        self.inptPosicionX.clear()
        self.inptAceleracionX.clear()

        self.inptPosicionY.clear()
        self.inptVelocidadInicialY.clear()
        self.inptAceleracionY.clear()

        self.inptPosicionZ.clear()
        self.inptVelocidadInicialZ.clear()
        self.inptAceleracionZ.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script m_r_u_A_3.py desde la carpeta actual
        subprocess.run(['python', 'm_r_u_A_3.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorVelocidadInicialX.clear()
        self.lblErrorPosicionX.clear()
        self.lblErrorAceleracionX.clear()

        self.lblErrorVelocidadInicialY.clear()
        self.lblErrorPosicionY.clear()
        self.lblErrorAceleracionY.clear()

        self.lblErrorVelocidadInicialZ.clear()
        self.lblErrorPosicionZ.clear()
        self.lblErrorAceleracionZ.clear()

        self.inptVelocidadInicialX.clear()
        self.inptPosicionX.clear()
        self.inptAceleracionX.clear()

        self.inptPosicionY.clear()
        self.inptVelocidadInicialY.clear()
        self.inptAceleracionY.clear()

        self.inptPosicionZ.clear()
        self.inptVelocidadInicialZ.clear()
        self.inptAceleracionZ.clear()

        self.close()

class planoInclinadoDialog(QtWidgets.QDialog, Ui_DialogPlanoInclinado):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):

        masaObjeto_text = self.inptMasaObjeto.text()
        anguloInclinacion_text = self.inptAnguloInclinacion.text()

        # Verificar si los textos son números enteros
        try:
            masaObjeto = int(masaObjeto_text)
            anguloInclinacion = int(anguloInclinacion_text)

        except ValueError:
            if not masaObjeto_text.isdigit():
                self.lblErrorMasaObjeto.setText("Dato incorrecto")
            else:
                self.lblErrorMasaObjeto.clear()

            if not anguloInclinacion_text.isdigit():
                self.lblErrorAnguloInclinacion.setText("Dato incorrecto")
            else:
                self.lblErrorAnguloInclinacion.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_Planoinclinado.txt')
        with open(archivo, 'w') as f:
            f.write("Variables para Planoinclinado:\n")
            f.write(f"Masa objeto: {masaObjeto}\n")
            f.write(f"Angulo de inclinacion: {anguloInclinacion}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorMasaObjeto.clear()
        self.lblErrorAnguloInclinacion.clear()

        self.inptMasaObjeto.clear()
        self.inptAnguloInclinacion.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script m_r_u_A_3.py desde la carpeta actual
        subprocess.run(['python', 'plane.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorMasaObjeto.clear()
        self.lblErrorAnguloInclinacion.clear()

        self.inptMasaObjeto.clear()
        self.inptAnguloInclinacion.clear()

        self.close()

class planoInclinadoPoleaDialog(QtWidgets.QDialog, Ui_DialogPlanoInclinadoPolea):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):

        masaObjeto_text = self.inptMasaObjeto.text()
        masaObjeto2_text = self.inptMasaObjeto2.text()
        anguloInclinacion_text = self.inptAnguloInclinacion.text()

        # Verificar si los textos son números enteros
        try:
            masaObjeto = int(masaObjeto_text)
            masaObjeto2 = int(masaObjeto2_text)
            anguloInclinacion = int(anguloInclinacion_text)

        except ValueError:
            if not masaObjeto_text.isdigit():
                self.lblErrorMasaObjeto.setText("Dato incorrecto")
            else:
                self.lblErrorMasaObjeto.clear()

            if not masaObjeto2_text.isdigit():
                self.lblErrorMasaObjeto2.setText("Dato incorrecto")
            else:
                self.lblErrorMasaObjeto2.clear()

            if not anguloInclinacion_text.isdigit():
                self.lblErrorAnguloInclinacion.setText("Dato incorrecto")
            else:
                self.lblErrorAnguloInclinacion.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_Planoinclinadopolea.txt')
        with open(archivo, 'w') as f:
            f.write("Variables para Planoinclinadopolea:\n")
            f.write(f"Masa ladrillo 1: {masaObjeto}\n")
            f.write(f"Masa ladrillo 2: {masaObjeto2}\n")
            f.write(f"Angulo de inclinacion: {anguloInclinacion}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorMasaObjeto.clear()
        self.lblErrorMasaObjeto2.clear()
        self.lblErrorAnguloInclinacion.clear()

        self.inptMasaObjeto.clear()
        self.inptMasaObjeto2.clear()
        self.inptAnguloInclinacion.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script m_r_u_A_3.py desde la carpeta actual
        subprocess.run(['python', 'plane_pole.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorMasaObjeto.clear()
        self.lblErrorMasaObjeto2.clear()
        self.lblErrorAnguloInclinacion.clear()

        self.inptMasaObjeto.clear()
        self.inptMasaObjeto2.clear()
        self.inptAnguloInclinacion.clear()

        self.close()

class penduloDialog(QtWidgets.QDialog, Ui_DialogPendulo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):

        masaObjeto_text = self.inptMasaObjeto.text()
        anguloInclinacion_text = self.inptAnguloInclinacion.text()

        # Verificar si los textos son números enteros
        try:
            masaObjeto = int(masaObjeto_text)
            anguloInclinacion = int(anguloInclinacion_text)

        except ValueError:
            if not masaObjeto_text.isdigit():
                self.lblErrorMasaObjeto.setText("Dato incorrecto")
            else:
                self.lblErrorMasaObjeto.clear()

            if not anguloInclinacion_text.isdigit():
                self.lblErrorAnguloInclinacion.setText("Dato incorrecto")
            else:
                self.lblErrorAnguloInclinacion.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_Péndulo.txt')
        with open(archivo, 'w') as f:
            f.write("Variables para Péndulo:\n")
            f.write(f"Masa objeto: {masaObjeto}\n")
            f.write(f"Angulo de inclinacion: {anguloInclinacion}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorMasaObjeto.clear()
        self.lblErrorAnguloInclinacion.clear()

        self.inptMasaObjeto.clear()
        self.inptAnguloInclinacion.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script pendulum.py desde la carpeta actual
        subprocess.run(['python', 'pendulum.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorMasaObjeto.clear()
        self.lblErrorAnguloInclinacion.clear()

        self.inptMasaObjeto.clear()
        self.inptAnguloInclinacion.clear()

        self.close()

class penduloResorteDialog(QtWidgets.QDialog, Ui_DialogPenduloResorte):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):

        masaObjeto_text = self.inptMasaObjeto.text()
        anguloInclinacion_text = self.inptAnguloInclinacion.text()
        constanteResorte_text = self.inptConstanteResorte.text()

        # Verificar si los textos son números enteros
        try:
            masaObjeto = int(masaObjeto_text)
            anguloInclinacion = int(anguloInclinacion_text)
            constanteResorte = int(constanteResorte_text)

        except ValueError:
            if not masaObjeto_text.isdigit():
                self.lblErrorMasaObjeto.setText("Dato incorrecto")
            else:
                self.lblErrorMasaObjeto.clear()

            if not anguloInclinacion_text.isdigit():
                self.lblErrorAnguloInclinacion.setText("Dato incorrecto")
            else:
                self.lblErrorAnguloInclinacion.clear()

            if not constanteResorte_text.isdigit():
                self.lblErrorConstanteResorte.setText("Dato incorrecto")
            else:
                self.lblErrorConstanteResorte.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_Pénduloresorte.txt')
        with open(archivo, 'w') as f:
            f.write("Variables para Péndulo:\n")
            f.write(f"Masa objeto: {masaObjeto}\n")
            f.write(f"Angulo de inclinacion: {anguloInclinacion}\n")
            f.write(f"Constante del resorte: {constanteResorte}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorMasaObjeto.clear()
        self.lblErrorAnguloInclinacion.clear()
        self.lblErrorConstanteResorte.clear()

        self.inptMasaObjeto.clear()
        self.inptAnguloInclinacion.clear()
        self.inptConstanteResorte.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script pendulum.py desde la carpeta actual
        subprocess.run(['python', 'pendulum-spring.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorMasaObjeto.clear()
        self.lblErrorAnguloInclinacion.clear()
        self.lblErrorConstanteResorte.clear()

        self.inptMasaObjeto.clear()
        self.inptAnguloInclinacion.clear()
        self.inptConstanteResorte.clear()

        self.close()

class resorteDialog(QtWidgets.QDialog, Ui_DialogResorte):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):

        masaObjeto_text = self.inptMasaObjeto.text()
        distanciaCompresion_text = self.inptDistanciaCompresion.text()
        constanteResorte_text = self.inptConstanteResorte.text()

        # Verificar si los textos son números enteros
        try:
            masaObjeto = int(masaObjeto_text)
            distanciaCompresion = int(distanciaCompresion_text)
            constanteResorte = int(constanteResorte_text)

        except ValueError:
            if not masaObjeto_text.isdigit():
                self.lblErrorMasaObjeto.setText("Dato incorrecto")
            else:
                self.lblErrorMasaObjeto.clear()

            if not distanciaCompresion_text.isdigit():
                self.lblErrorDistanciaCompresion.setText("Dato incorrecto")
            else:
                self.lblErrorDistanciaCompresion.clear()

            if not constanteResorte_text.isdigit():
                self.lblErrorConstanteResorte.setText("Dato incorrecto")
            else:
                self.lblErrorConstanteResorte.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_Resorte.txt')
        with open(archivo, 'w') as f:
            f.write("Variables para Resorte:\n")
            f.write(f"Masa objeto: {masaObjeto}\n")
            f.write(f"Distancia de compresion: {distanciaCompresion}\n")
            f.write(f"Constante del resorte: {constanteResorte}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorMasaObjeto.clear()
        self.lblErrorDistanciaCompresion.clear()
        self.lblErrorConstanteResorte.clear()

        self.inptMasaObjeto.clear()
        self.inptDistanciaCompresion.clear()
        self.inptConstanteResorte.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script pendulum.py desde la carpeta actual
        subprocess.run(['python', 'spring.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorMasaObjeto.clear()
        self.lblErrorDistanciaCompresion.clear()
        self.lblErrorConstanteResorte.clear()

        self.inptMasaObjeto.clear()
        self.inptDistanciaCompresion.clear()
        self.inptConstanteResorte.clear()

        self.close()

class colisionLinealElasticaDialog(QtWidgets.QDialog, Ui_DialogColisionLinealElastica):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSimular.clicked.connect(self.on_simular_clicked)
        self.btnCancelar.clicked.connect(self.on_cancelar_clicked)

    def on_simular_clicked(self):

        masaLadrillo1_text = self.inptMasaLadrillo1.text()
        velocidadInicialLadrillo1_text = self.inptVelocidadLadrillo1()

        masaLadrillo2_text = self.inptMasaLadrillo2.text()
        velocidadInicialLadrillo2_text = self.inptVelocidadLadrillo2()

        distanciaLadrillos_text = self.inptDistanciaLadrillos()

        # Verificar si los textos son números enteros
        try:
            masaLadrillo1 = int(masaLadrillo1_text)
            velocidadInicialLadrillo1 = int(velocidadInicialLadrillo1_text)

            masaLadrillo2 = int(masaLadrillo2_text)
            velocidadInicialLadrillo2 = int(velocidadInicialLadrillo2_text)

            distanciaLadrilos = int(distanciaLadrillos_text)

        except ValueError:
            if not masaLadrillo1.isdigit():
                self.lblErrorMasaLadrillo1.setText("Dato incorrecto")
            else:
                self.lblErrorMasaLadrillo1.clear()

            if not velocidadInicialLadrillo1.isdigit():
                self.lblErro.setText("Dato incorrecto")
            else:
                self.lblErrorDistanciaCompresion.clear()

            if not distanciaLadrilos.isdigit():
                self.lblErrorConstanteResorte.setText("Dato incorrecto")
            else:
                self.lblErrorConstanteResorte.clear()

            return

        # Obtener la ruta completa a la carpeta dynamic_scenarios
        carpeta = os.path.join(os.path.dirname(__file__), 'dynamic_scenarios')

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Guardar en un archivo .txt dentro de la carpeta dynamic_scenarios
        archivo = os.path.join(carpeta, 'data_Resorte.txt')
        with open(archivo, 'w') as f:
            f.write("Variables para Resorte:\n")
            f.write(f"Masa objeto: {masaObjeto}\n")
            f.write(f"Distancia de compresion: {distanciaCompresion}\n")
            f.write(f"Constante del resorte: {constanteResorte}\n")

        # Limpiar los mensajes de error si los valores son números enteros
        self.lblErrorMasaObjeto.clear()
        self.lblErrorDistanciaCompresion.clear()
        self.lblErrorConstanteResorte.clear()

        self.inptMasaObjeto.clear()
        self.inptDistanciaCompresion.clear()
        self.inptConstanteResorte.clear()

        # Establecer la carpeta actual como dynamic_scenarios
        os.chdir(carpeta)

        # Ejecutar el script pendulum.py desde la carpeta actual
        subprocess.run(['python', 'spring.py'])

        self.close()

    def on_cancelar_clicked(self):
        self.lblErrorMasaObjeto.clear()
        self.lblErrorDistanciaCompresion.clear()
        self.lblErrorConstanteResorte.clear()

        self.inptMasaObjeto.clear()
        self.inptDistanciaCompresion.clear()
        self.inptConstanteResorte.clear()

        self.close()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnMur.clicked.connect(self.show_mur_dialog)
        self.ui.btnMura.clicked.connect(self.show_mura_dialog)
        self.ui.btnMuraxa.clicked.connect(self.show_muraxa_dialog)
        self.ui.btnMuraxaya.clicked.connect(self.show_muraxaya_dialog)
        self.ui.btnMuraxaza.clicked.connect(self.show_muraxaza_dialog)
        self.ui.btnMurayaza.clicked.connect(self.show_murayaza_dialog)
        self.ui.btnMura3.clicked.connect(self.show_mura3_dialog)
        self.ui.btnPlanoInclinado.clicked.connect(self.show_planoInclinado_dialog)
        self.ui.btnPlanoInclinadoPolea.clicked.connect(self.show_planoInclinadoPolea_dialog)
        self.ui.btnPendulo.clicked.connect(self.show_pendulo_dialog)
        self.ui.btnPenduloResorte.clicked.connect(self.show_penduloResorte_dialog)
        self.ui.btnResorte.clicked.connect(self.show_resorte_dialog)
        self.ui.btnColisionLinealElastica.clicked.connect(self.show_colisionLinealElastica_dialog)

        # Crear instancias de cadad dialogo
        self.mur_dialog = MurDialog()
        self.mura_dialog = MuraDialog()
        self.muraxa_dialog = MuraxaDialog()
        self.muraxaya_dialog = MuraxayaDialog()
        self.muraxaza_dialog = MuraxazaDialog()
        self.murayaza_dialog = MurayazaDialog()
        self.mura3_dialog = Mura3Dialog()
        self.planoInclinado_dialog = planoInclinadoDialog()
        self.planoInclinadoPolea_dialog = planoInclinadoPoleaDialog()
        self.pendulo_dialog = penduloDialog()
        self.penduloResorte_dialog = penduloResorteDialog()
        self.resorte_dialog = resorteDialog()
        self.colisionLinealElastica_dialog = colisionLinealElasticaDialog()

    def show_mur_dialog(self):
        # Mostrar el diálogo
        self.mur_dialog.exec_()

    def show_mura_dialog(self):
        # Mostrar el diálogo
        self.mura_dialog.exec_()

    def show_muraxa_dialog(self):
        # Mostrar el diálogo
        self.muraxa_dialog.exec_()

    def show_muraxaya_dialog(self):
        # Mostrar el diálogo
        self.muraxaya_dialog.exec_()

    def show_muraxaza_dialog(self):
        # Mostrar el diálogo
        self.muraxaza_dialog.exec_()

    def show_murayaza_dialog(self):
        # Mostrar el diálogo
        self.murayaza_dialog.exec_()

    def show_mura3_dialog(self):
        # Mostrar el diálogo
        self.mura3_dialog.exec_()

    def show_planoInclinado_dialog(self):
        # Mostrar el diálogo
        self.planoInclinado_dialog.exec_()

    def show_planoInclinadoPolea_dialog(self):
        # Mostrar el diálogo
        self.planoInclinadoPolea_dialog.exec_()

    def show_pendulo_dialog(self):
        # Mostrar el diálogo
        self.pendulo_dialog.exec_()

    def show_penduloResorte_dialog(self):
        # Mostrar el diálogo
        self.penduloResorte_dialog.exec_()

    def show_resorte_dialog(self):
        # Mostrar el diálogo
        self.resorte_dialog.exec_()

    def show_colisionLinealElastica_dialog(self):
        # Mostrar el diálogo
        self.colisionLinealElastica_dialog.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
