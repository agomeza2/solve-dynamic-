# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\peral\OneDrive\Escritorio\solve-dynamic-\Windows\desingUi\colisionLinealElastica.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogColisionLinealElastica(object):
    def setupUi(self, DialogColisionLinealElastica):
        DialogColisionLinealElastica.setObjectName("DialogColisionLinealElastica")
        DialogColisionLinealElastica.resize(644, 282)
        DialogColisionLinealElastica.setStyleSheet("background-color: #DFEAFF;")
        self.inptVelocidadLadrillo1 = QtWidgets.QLineEdit(DialogColisionLinealElastica)
        self.inptVelocidadLadrillo1.setGeometry(QtCore.QRect(30, 170, 161, 20))
        self.inptVelocidadLadrillo1.setStyleSheet("background-color: white;")
        self.inptVelocidadLadrillo1.setObjectName("inptVelocidadLadrillo1")
        self.lblErrorVelocidadLadrillo1 = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.lblErrorVelocidadLadrillo1.setGeometry(QtCore.QRect(30, 120, 131, 16))
        self.lblErrorVelocidadLadrillo1.setText("")
        self.lblErrorVelocidadLadrillo1.setObjectName("lblErrorVelocidadLadrillo1")
        self.label_2 = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.label_2.setGeometry(QtCore.QRect(240, 80, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.label_6.setGeometry(QtCore.QRect(450, 80, 111, 16))
        self.label_6.setObjectName("label_6")
        self.lblVelocidadLadrillo2 = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.lblVelocidadLadrillo2.setGeometry(QtCore.QRect(240, 190, 131, 16))
        self.lblVelocidadLadrillo2.setText("")
        self.lblVelocidadLadrillo2.setObjectName("lblVelocidadLadrillo2")
        self.lblErrorMasaLadrillo2 = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.lblErrorMasaLadrillo2.setGeometry(QtCore.QRect(240, 120, 131, 16))
        self.lblErrorMasaLadrillo2.setText("")
        self.lblErrorMasaLadrillo2.setObjectName("lblErrorMasaLadrillo2")
        self.lblVelocidadLadrillo1 = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.lblVelocidadLadrillo1.setGeometry(QtCore.QRect(30, 190, 131, 16))
        self.lblVelocidadLadrillo1.setText("")
        self.lblVelocidadLadrillo1.setObjectName("lblVelocidadLadrillo1")
        self.label_3 = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 641, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.inptDistanciaLadrillos = QtWidgets.QLineEdit(DialogColisionLinealElastica)
        self.inptDistanciaLadrillos.setGeometry(QtCore.QRect(450, 100, 161, 20))
        self.inptDistanciaLadrillos.setStyleSheet("background-color: white;")
        self.inptDistanciaLadrillos.setObjectName("inptDistanciaLadrillos")
        self.inptMasaLadrillo1 = QtWidgets.QLineEdit(DialogColisionLinealElastica)
        self.inptMasaLadrillo1.setGeometry(QtCore.QRect(30, 100, 161, 20))
        self.inptMasaLadrillo1.setStyleSheet("background-color: white;")
        self.inptMasaLadrillo1.setObjectName("inptMasaLadrillo1")
        self.label = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.label.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.label.setObjectName("label")
        self.inptVelocidadLadrillo2 = QtWidgets.QLineEdit(DialogColisionLinealElastica)
        self.inptVelocidadLadrillo2.setGeometry(QtCore.QRect(240, 170, 161, 20))
        self.inptVelocidadLadrillo2.setStyleSheet("background-color: white;")
        self.inptVelocidadLadrillo2.setObjectName("inptVelocidadLadrillo2")
        self.label_7 = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.label_7.setGeometry(QtCore.QRect(240, 150, 161, 16))
        self.label_7.setObjectName("label_7")
        self.lblErrorMasaLadrillo1 = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.lblErrorMasaLadrillo1.setGeometry(QtCore.QRect(30, 120, 131, 16))
        self.lblErrorMasaLadrillo1.setText("")
        self.lblErrorMasaLadrillo1.setObjectName("lblErrorMasaLadrillo1")
        self.inptMasaLadrillo2 = QtWidgets.QLineEdit(DialogColisionLinealElastica)
        self.inptMasaLadrillo2.setGeometry(QtCore.QRect(240, 100, 161, 20))
        self.inptMasaLadrillo2.setStyleSheet("background-color: white;")
        self.inptMasaLadrillo2.setObjectName("inptMasaLadrillo2")
        self.lblErrorDistanciaLadrillos = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.lblErrorDistanciaLadrillos.setGeometry(QtCore.QRect(450, 120, 131, 16))
        self.lblErrorDistanciaLadrillos.setText("")
        self.lblErrorDistanciaLadrillos.setObjectName("lblErrorDistanciaLadrillos")
        self.label_4 = QtWidgets.QLabel(DialogColisionLinealElastica)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 161, 16))
        self.label_4.setObjectName("label_4")
        self.btnSimular = QtWidgets.QPushButton(DialogColisionLinealElastica)
        self.btnSimular.setGeometry(QtCore.QRect(240, 230, 75, 23))
        self.btnSimular.setStyleSheet("background-color: #3D63DD;\n"
"color: white;")
        self.btnSimular.setObjectName("btnSimular")
        self.btnCancelar = QtWidgets.QPushButton(DialogColisionLinealElastica)
        self.btnCancelar.setGeometry(QtCore.QRect(330, 230, 75, 23))
        self.btnCancelar.setStyleSheet("background-color: #3D63DD;\n"
"color: white;")
        self.btnCancelar.setObjectName("btnCancelar")

        self.retranslateUi(DialogColisionLinealElastica)
        QtCore.QMetaObject.connectSlotsByName(DialogColisionLinealElastica)

    def retranslateUi(self, DialogColisionLinealElastica):
        _translate = QtCore.QCoreApplication.translate
        DialogColisionLinealElastica.setWindowTitle(_translate("DialogColisionLinealElastica", "Colisión lineal elástica "))
        self.label_2.setText(_translate("DialogColisionLinealElastica", "Masa ladrillo 2"))
        self.label_6.setText(_translate("DialogColisionLinealElastica", "Distancia entre ladrillos"))
        self.label_3.setText(_translate("DialogColisionLinealElastica", "Colisión lineal elástica "))
        self.label.setText(_translate("DialogColisionLinealElastica", "Masa ladrillo 1"))
        self.label_7.setText(_translate("DialogColisionLinealElastica", "Velocidad incial ladrillo 2"))
        self.label_4.setText(_translate("DialogColisionLinealElastica", "Velocidad incial ladrillo 1"))
        self.btnSimular.setText(_translate("DialogColisionLinealElastica", "Simular"))
        self.btnCancelar.setText(_translate("DialogColisionLinealElastica", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogColisionLinealElastica = QtWidgets.QDialog()
    ui = Ui_DialogColisionLinealElastica()
    ui.setupUi(DialogColisionLinealElastica)
    DialogColisionLinealElastica.show()
    sys.exit(app.exec_())
