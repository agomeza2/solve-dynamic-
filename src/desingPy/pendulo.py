# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\peral\OneDrive\Escritorio\solve-dynamic-\Windows\desingUi\pendulo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogPendulo(object):
    def setupUi(self, DialogPendulo):
        DialogPendulo.setObjectName("DialogPendulo")
        DialogPendulo.resize(225, 293)
        DialogPendulo.setStyleSheet("background-color: #DFEAFF;\n"
"")
        self.label_3 = QtWidgets.QLabel(DialogPendulo)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.lblErrorAnguloInclinacion = QtWidgets.QLabel(DialogPendulo)
        self.lblErrorAnguloInclinacion.setGeometry(QtCore.QRect(30, 200, 131, 16))
        self.lblErrorAnguloInclinacion.setText("")
        self.lblErrorAnguloInclinacion.setObjectName("lblErrorAnguloInclinacion")
        self.label_2 = QtWidgets.QLabel(DialogPendulo)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 131, 16))
        self.label_2.setObjectName("label_2")
        self.inptMasaObjeto = QtWidgets.QLineEdit(DialogPendulo)
        self.inptMasaObjeto.setGeometry(QtCore.QRect(30, 100, 161, 20))
        self.inptMasaObjeto.setStyleSheet("background-color: white;")
        self.inptMasaObjeto.setObjectName("inptMasaObjeto")
        self.lblErrorMasaObjeto = QtWidgets.QLabel(DialogPendulo)
        self.lblErrorMasaObjeto.setGeometry(QtCore.QRect(30, 120, 131, 16))
        self.lblErrorMasaObjeto.setText("")
        self.lblErrorMasaObjeto.setObjectName("lblErrorMasaObjeto")
        self.inptAnguloInclinacion = QtWidgets.QLineEdit(DialogPendulo)
        self.inptAnguloInclinacion.setGeometry(QtCore.QRect(30, 180, 161, 20))
        self.inptAnguloInclinacion.setStyleSheet("background-color: white;")
        self.inptAnguloInclinacion.setObjectName("inptAnguloInclinacion")
        self.label = QtWidgets.QLabel(DialogPendulo)
        self.label.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.label.setObjectName("label")
        self.btnSimular = QtWidgets.QPushButton(DialogPendulo)
        self.btnSimular.setGeometry(QtCore.QRect(40, 240, 75, 23))
        self.btnSimular.setStyleSheet("background-color: #3D63DD;\n"
"color: white;")
        self.btnSimular.setObjectName("btnSimular")
        self.btnCancelar = QtWidgets.QPushButton(DialogPendulo)
        self.btnCancelar.setGeometry(QtCore.QRect(120, 240, 75, 23))
        self.btnCancelar.setStyleSheet("background-color: #3D63DD;\n"
"color: white;")
        self.btnCancelar.setObjectName("btnCancelar")

        self.retranslateUi(DialogPendulo)
        QtCore.QMetaObject.connectSlotsByName(DialogPendulo)

    def retranslateUi(self, DialogPendulo):
        _translate = QtCore.QCoreApplication.translate
        DialogPendulo.setWindowTitle(_translate("DialogPendulo", "Péndulo"))
        self.label_3.setText(_translate("DialogPendulo", "Péndulo"))
        self.label_2.setText(_translate("DialogPendulo", "Angulo de inclinacion"))
        self.label.setText(_translate("DialogPendulo", "Masa del  objeto"))
        self.btnSimular.setText(_translate("DialogPendulo", "Simular"))
        self.btnCancelar.setText(_translate("DialogPendulo", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogPendulo = QtWidgets.QDialog()
    ui = Ui_DialogPendulo()
    ui.setupUi(DialogPendulo)
    DialogPendulo.show()
    sys.exit(app.exec_())
