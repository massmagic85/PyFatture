# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdocumento.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import sqlite3

global doc_id
doc_id = ''

global path
path = ''

def get_DocId(database, id):
    global doc_id
    doc_id = id

    global path
    path = database





class Ui_MainWindow2(object):

    def loadFattura(self, database, id):
            global path
            #database = "C:\\Users\\Massimiliano\\Documents\\Python\\Fatture.db"
            database = path
        # if len(database) != 0:
            conn = sqlite3.connect(database)
            query = "SELECT IdDocumento, EstrattoConto, NumOperazione, DataDocumento, DataBanca, DataValuta, TipoDocumento, Fornitore, NumeroDocumento, NumeroAssegno, SpeseIncasso, PagatoRiscosso, Valore " \
                    "FROM Documenti WHERE IdDocumento=" + id

            Fattura = conn.execute(query)

            for row_number, row_data in enumerate(Fattura):
                valori = []
                for column_number, data in enumerate(row_data):
                    valori.append(data)

            self.lineEdit_IdFattura.setText(str(valori[0]))
            self.checkBox_EC.setChecked(bool(valori[1]))
            self.lineEdit_NumOperazione.setText(str(valori[2]))

            if valori[3]:
                self.dateEdit_Data.setDate(datetime.datetime.strptime(valori[3], '%Y-%m-%d'))

            if valori[4]:
                self.dateEdit_DataBanca.setDate(datetime.datetime.strptime(valori[4], '%Y-%m-%d'))

            if valori[5]:
                self.dateEdit_DataValuta.setDate(datetime.datetime.strptime(valori[5], '%Y-%m-%d'))

            self.comboBox_Tipologia.setItemText(0, str(valori[6]))
            self.comboBox_Fornitore.setItemText(0, str(valori[7]))
            self.textEdit_NumeroDocumento.setText(str(valori[8]))
            self.lineEdit_Assegno.setText(str(valori[9]))
            self.lineEdit_Spese.setText(str(valori[10]))
            self.checkBox_Pagato.setChecked(bool(valori[11]))
            self.lineEdit_Valore.setText(str(valori[12]))


    def setupUi(self, MainWindow2):

        global doc_id
        global path

        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(340, 445)
        MainWindow2.setMinimumSize(QtCore.QSize(340, 445))
        MainWindow2.setMaximumSize(QtCore.QSize(340, 445))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)

        MainWindow2.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit_IdFattura = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_IdFattura.setGeometry(QtCore.QRect(140, 10, 180, 20))
        self.lineEdit_IdFattura.setReadOnly(True)
        self.lineEdit_IdFattura.setObjectName("lineEdit_IdFattura")

        self.checkBox_EC = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_EC.setGeometry(QtCore.QRect(140, 40, 20, 20))
        self.checkBox_EC.setText("")
        self.checkBox_EC.setObjectName("checkBox_EC")

        self.lineEdit_NumOperazione = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_NumOperazione.setGeometry(QtCore.QRect(140, 70, 180, 20))
        self.lineEdit_NumOperazione.setObjectName("lineEdit_NumOperazione")

        self.dateEdit_Data = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_Data.setGeometry(QtCore.QRect(140, 100, 180, 20))
        self.dateEdit_Data.setObjectName("dateEdit_Data")

        self.dateEdit_DataBanca = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_DataBanca.setGeometry(QtCore.QRect(140, 130, 180, 20))
        self.dateEdit_DataBanca.setObjectName("dateEdit_DataBanca")

        self.dateEdit_DataValuta = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_DataValuta.setGeometry(QtCore.QRect(140, 160, 180, 20))
        self.dateEdit_DataValuta.setObjectName("dateEdit_DataValuta")

        self.comboBox_Tipologia = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Tipologia.setGeometry(QtCore.QRect(140, 190, 180, 20))
        self.comboBox_Tipologia.addItem("")
        self.comboBox_Tipologia.setObjectName("comboBox_Tipologia")

        self.comboBox_Fornitore = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Fornitore.setGeometry(QtCore.QRect(140, 220, 180, 20))
        self.comboBox_Fornitore.addItem("")
        self.comboBox_Fornitore.setObjectName("comboBox_Fornitore")

        self.textEdit_NumeroDocumento = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_NumeroDocumento.setGeometry(QtCore.QRect(140, 250, 180, 60))
        self.textEdit_NumeroDocumento.setObjectName("textEdit_NumeroDocumento")

        self.lineEdit_Assegno = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Assegno.setGeometry(QtCore.QRect(140, 320, 180, 20))
        self.lineEdit_Assegno.setObjectName("lineEdit_Assegno")

        self.lineEdit_Spese = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Spese.setGeometry(QtCore.QRect(140, 350, 180, 20))
        self.lineEdit_Spese.setObjectName("lineEdit_Spese")

        self.checkBox_Pagato = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Pagato.setGeometry(QtCore.QRect(140, 380, 20, 20))
        self.checkBox_Pagato.setText("")
        self.checkBox_Pagato.setObjectName("checkBox_Pagato")

        self.lineEdit_Valore = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Valore.setGeometry(QtCore.QRect(140, 410, 180, 20))
        self.lineEdit_Valore.setObjectName("lineEdit_Valore")

        self.label_ID = QtWidgets.QLabel(self.centralwidget)
        self.label_ID.setGeometry(QtCore.QRect(20, 10, 100, 20))
        self.label_ID.setObjectName("label_ID")

        self.label_EC = QtWidgets.QLabel(self.centralwidget)
        self.label_EC.setGeometry(QtCore.QRect(20, 40, 100, 20))
        self.label_EC.setObjectName("label_EC")

        self.label_NumOperazione = QtWidgets.QLabel(self.centralwidget)
        self.label_NumOperazione.setGeometry(QtCore.QRect(20, 70, 115, 20))
        self.label_NumOperazione.setObjectName("label_NumOperazione")

        self.label_Data = QtWidgets.QLabel(self.centralwidget)
        self.label_Data.setGeometry(QtCore.QRect(20, 100, 100, 20))
        self.label_Data.setObjectName("label_Data")

        self.label_DataBanca = QtWidgets.QLabel(self.centralwidget)
        self.label_DataBanca.setGeometry(QtCore.QRect(20, 130, 100, 20))
        self.label_DataBanca.setObjectName("label_DataBanca")

        self.label_DataValuta = QtWidgets.QLabel(self.centralwidget)
        self.label_DataValuta.setGeometry(QtCore.QRect(20, 160, 100, 20))
        self.label_DataValuta.setObjectName("label_DataValuta")

        self.label_Tipologia = QtWidgets.QLabel(self.centralwidget)
        self.label_Tipologia.setGeometry(QtCore.QRect(20, 190, 100, 20))
        self.label_Tipologia.setObjectName("label_Tipologia")

        self.label_Fornitore = QtWidgets.QLabel(self.centralwidget)
        self.label_Fornitore.setGeometry(QtCore.QRect(20, 220, 100, 20))
        self.label_Fornitore.setObjectName("label_Fornitore")

        self.label_NumDocumento = QtWidgets.QLabel(self.centralwidget)
        self.label_NumDocumento.setGeometry(QtCore.QRect(20, 250, 115, 20))
        self.label_NumDocumento.setObjectName("label_NumDocumento")

        self.label_Assegno = QtWidgets.QLabel(self.centralwidget)
        self.label_Assegno.setGeometry(QtCore.QRect(20, 320, 100, 20))
        self.label_Assegno.setObjectName("label_Assegno")

        self.label_Spese = QtWidgets.QLabel(self.centralwidget)
        self.label_Spese.setGeometry(QtCore.QRect(20, 350, 115, 20))
        self.label_Spese.setObjectName("label_Spese")

        self.label_Pagato = QtWidgets.QLabel(self.centralwidget)
        self.label_Pagato.setGeometry(QtCore.QRect(20, 380, 115, 20))
        self.label_Pagato.setObjectName("label_Pagato")

        self.label_Valuta = QtWidgets.QLabel(self.centralwidget)
        self.label_Valuta.setGeometry(QtCore.QRect(20, 410, 100, 20))
        self.label_Valuta.setObjectName("label_Valuta")

        MainWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)
        self.loadFattura(path, doc_id)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Modifica"))
        self.label_ID.setText(_translate("MainWindow2", "ID Documento"))
        self.label_EC.setText(_translate("MainWindow2", "Estratto Conto"))
        self.label_NumOperazione.setText(_translate("MainWindow2", "Numero Operazione"))
        self.label_Data.setText(_translate("MainWindow2", "Data Documento"))
        self.label_DataBanca.setText(_translate("MainWindow2", "Data Banca"))
        self.label_DataValuta.setText(_translate("MainWindow2", "Data Valuta"))
        self.label_Tipologia.setText(_translate("MainWindow2", "Tipologia"))
        self.label_Fornitore.setText(_translate("MainWindow2", "Fornitore"))
        self.label_NumDocumento.setText(_translate("MainWindow2", "Numero Documento"))
        self.label_Assegno.setText(_translate("MainWindow2", "Assegno"))
        self.label_Spese.setText(_translate("MainWindow2", "Spese Incasso EUR"))
        self.label_Pagato.setText(_translate("MainWindow2", "Pagato / Riscosso"))
        self.label_Valuta.setText(_translate("MainWindow2", "Valore EUR"))



