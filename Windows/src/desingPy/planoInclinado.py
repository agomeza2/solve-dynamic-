# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\peral\OneDrive\Escritorio\solve-dynamic-\Windows\desingUi\planoInclinado.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogPlanoInclinado(object):
    def setupUi(self, DialogPlanoInclinado):
        DialogPlanoInclinado.setObjectName("DialogPlanoInclinado")
        DialogPlanoInclinado.resize(227, 294)
        DialogPlanoInclinado.setStyleSheet("background-color: #DFEAFF;")
        self.inptMasaObjeto = QtWidgets.QLineEdit(DialogPlanoInclinado)
        self.inptMasaObjeto.setGeometry(QtCore.QRect(30, 100, 161, 20))
        self.inptMasaObjeto.setStyleSheet("background-color: white;")
        self.inptMasaObjeto.setObjectName("inptMasaObjeto")
        self.label_3 = QtWidgets.QLabel(DialogPlanoInclinado)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(DialogPlanoInclinado)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(DialogPlanoInclinado)
        self.label.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.label.setObjectName("label")
        self.lblErrorAnguloInclinacion = QtWidgets.QLabel(DialogPlanoInclinado)
        self.lblErrorAnguloInclinacion.setGeometry(QtCore.QRect(30, 200, 131, 16))
        self.lblErrorAnguloInclinacion.setText("")
        self.lblErrorAnguloInclinacion.setObjectName("lblErrorAnguloInclinacion")
        self.inptAnguloInclinacion = QtWidgets.QLineEdit(DialogPlanoInclinado)
        self.inptAnguloInclinacion.setGeometry(QtCore.QRect(30, 180, 161, 20))
        self.inptAnguloInclinacion.setStyleSheet("background-color: white;")
        self.inptAnguloInclinacion.setObjectName("inptAnguloInclinacion")
        self.lblErrorMasaObjeto = QtWidgets.QLabel(DialogPlanoInclinado)
        self.lblErrorMasaObjeto.setGeometry(QtCore.QRect(30, 120, 131, 16))
        self.lblErrorMasaObjeto.setText("")
        self.lblErrorMasaObjeto.setObjectName("lblErrorMasaObjeto")
        self.btnSimular = QtWidgets.QPushButton(DialogPlanoInclinado)
        self.btnSimular.setGeometry(QtCore.QRect(30, 240, 75, 23))
        self.btnSimular.setStyleSheet("background-color: #3D63DD;\n"
"color: white;")
        self.btnSimular.setObjectName("btnSimular")
        self.btnCancelar = QtWidgets.QPushButton(DialogPlanoInclinado)
        self.btnCancelar.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.btnCancelar.setStyleSheet("background-color: #3D63DD;\n"
"color: white;")
        self.btnCancelar.setObjectName("btnCancelar")

        self.retranslateUi(DialogPlanoInclinado)
        QtCore.QMetaObject.connectSlotsByName(DialogPlanoInclinado)

    def retranslateUi(self, DialogPlanoInclinado):
        _translate = QtCore.QCoreApplication.translate
        DialogPlanoInclinado.setWindowTitle(_translate("DialogPlanoInclinado", "Plano inclinado"))
        self.label_3.setText(_translate("DialogPlanoInclinado", "Plano inclinado"))
        self.label_2.setText(_translate("DialogPlanoInclinado", "Angulo de inclinacion"))
        self.label.setText(_translate("DialogPlanoInclinado", "Masa del  objeto"))
        self.btnSimular.setText(_translate("DialogPlanoInclinado", "Simular"))
        self.btnCancelar.setText(_translate("DialogPlanoInclinado", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogPlanoInclinado = QtWidgets.QDialog()
    ui = Ui_DialogPlanoInclinado()
    ui.setupUi(DialogPlanoInclinado)
    DialogPlanoInclinado.show()
    sys.exit(app.exec_())
