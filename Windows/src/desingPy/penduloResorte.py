# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\peral\OneDrive\Escritorio\solve-dynamic-\Windows\desingUi\penduloResorte.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogPenduloResorte(object):
    def setupUi(self, DialogPenduloResorte):
        DialogPenduloResorte.setObjectName("DialogPenduloResorte")
        DialogPenduloResorte.resize(226, 377)
        DialogPenduloResorte.setStyleSheet("background-color: #DFEAFF;")
        self.label_3 = QtWidgets.QLabel(DialogPenduloResorte)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.inptMasaObjeto = QtWidgets.QLineEdit(DialogPenduloResorte)
        self.inptMasaObjeto.setGeometry(QtCore.QRect(30, 100, 161, 20))
        self.inptMasaObjeto.setStyleSheet("background-color: white;")
        self.inptMasaObjeto.setObjectName("inptMasaObjeto")
        self.label = QtWidgets.QLabel(DialogPenduloResorte)
        self.label.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogPenduloResorte)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 131, 16))
        self.label_2.setObjectName("label_2")
        self.inptAnguloInclinacion = QtWidgets.QLineEdit(DialogPenduloResorte)
        self.inptAnguloInclinacion.setGeometry(QtCore.QRect(30, 180, 161, 20))
        self.inptAnguloInclinacion.setStyleSheet("background-color: white;")
        self.inptAnguloInclinacion.setObjectName("inptAnguloInclinacion")
        self.lblErrorAnguloInclinacion = QtWidgets.QLabel(DialogPenduloResorte)
        self.lblErrorAnguloInclinacion.setGeometry(QtCore.QRect(30, 200, 131, 16))
        self.lblErrorAnguloInclinacion.setText("")
        self.lblErrorAnguloInclinacion.setObjectName("lblErrorAnguloInclinacion")
        self.lblErrorMasaObjeto = QtWidgets.QLabel(DialogPenduloResorte)
        self.lblErrorMasaObjeto.setGeometry(QtCore.QRect(30, 120, 131, 16))
        self.lblErrorMasaObjeto.setText("")
        self.lblErrorMasaObjeto.setObjectName("lblErrorMasaObjeto")
        self.label_4 = QtWidgets.QLabel(DialogPenduloResorte)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 131, 16))
        self.label_4.setObjectName("label_4")
        self.inptConstanteResorte = QtWidgets.QLineEdit(DialogPenduloResorte)
        self.inptConstanteResorte.setGeometry(QtCore.QRect(30, 260, 161, 20))
        self.inptConstanteResorte.setStyleSheet("background-color: white;")
        self.inptConstanteResorte.setObjectName("inptConstanteResorte")
        self.lblErrorConstanteResorte = QtWidgets.QLabel(DialogPenduloResorte)
        self.lblErrorConstanteResorte.setGeometry(QtCore.QRect(30, 280, 131, 16))
        self.lblErrorConstanteResorte.setText("")
        self.lblErrorConstanteResorte.setObjectName("lblErrorConstanteResorte")
        self.btnSimular = QtWidgets.QPushButton(DialogPenduloResorte)
        self.btnSimular.setGeometry(QtCore.QRect(30, 320, 75, 23))
        self.btnSimular.setStyleSheet("background-color: #3D63DD;\n"
"color: white;")
        self.btnSimular.setObjectName("btnSimular")
        self.btnCancelar = QtWidgets.QPushButton(DialogPenduloResorte)
        self.btnCancelar.setGeometry(QtCore.QRect(120, 320, 75, 23))
        self.btnCancelar.setStyleSheet("background-color: #3D63DD;\n"
"color: white;")
        self.btnCancelar.setObjectName("btnCancelar")

        self.retranslateUi(DialogPenduloResorte)
        QtCore.QMetaObject.connectSlotsByName(DialogPenduloResorte)

    def retranslateUi(self, DialogPenduloResorte):
        _translate = QtCore.QCoreApplication.translate
        DialogPenduloResorte.setWindowTitle(_translate("DialogPenduloResorte", "Péndulo resorte"))
        self.label_3.setText(_translate("DialogPenduloResorte", "Péndulo resorte"))
        self.label.setText(_translate("DialogPenduloResorte", "Masa del  objeto"))
        self.label_2.setText(_translate("DialogPenduloResorte", "Angulo de inclinacion"))
        self.label_4.setText(_translate("DialogPenduloResorte", "Constante del resorte"))
        self.btnSimular.setText(_translate("DialogPenduloResorte", "Simular"))
        self.btnCancelar.setText(_translate("DialogPenduloResorte", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogPenduloResorte = QtWidgets.QDialog()
    ui = Ui_DialogPenduloResorte()
    ui.setupUi(DialogPenduloResorte)
    DialogPenduloResorte.show()
    sys.exit(app.exec_())
