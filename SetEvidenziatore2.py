# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colorpicker.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

global nEvidenz
nEvidenz = 0

global sfondo
sfondo = []

global testo
testo = []

class Ui_MainWindow3(object):

    def loadEvidenz(self):

        global checkbox_abilitato
        global line_cerca
        global label_in
        global combobox_in
        global label_con
        global btn_testo
        global btn_sfondo
        global lbn_esempio
        global lbn_id

        global testo
        global sfondo
        global nEvidenz

        #global path
        database = "C:\\Users\\Massimiliano\\Documents\\GitHub\\PyFatture\\Fatture_new.db"
        #database = path
        # if len(database) != 0:
        conn = sqlite3.connect(database)
        query = "SELECT * FROM Evidenziatori"

        evidenz = conn.execute(query)


        for row_number, row_data in enumerate(evidenz):

            lbn_id[row_number].setText(str(row_data[0]))
            checkbox_abilitato[row_number].blockSignals(1)
            checkbox_abilitato[row_number].setChecked(bool(row_data[5]))
            checkbox_abilitato[row_number].blockSignals(0)
            line_cerca[row_number].setText(str(row_data[1]))
            lbn_esempio[row_number].setText(str(row_data[1]))
            combobox_in[row_number].blockSignals(1)
            combobox_in[row_number].setCurrentIndex(int(row_data[2]))
            combobox_in[row_number].blockSignals(0)
            btn_testo[row_number].setStyleSheet('color:' + str(row_data[3]) + ';')
            testo.append(str(row_data[3]))
            btn_sfondo[row_number].setStyleSheet('background-color:' + str(row_data[4]) + ';')
            sfondo.append(str(row_data[4]))

            self.trovatesto(row_number)
        conn.close()




    def saveEvidenz(self,id):

        global checkbox_abilitato
        global line_cerca
        global label_in
        global combobox_in
        global label_con
        global btn_testo
        global btn_sfondo
        global lbn_esempio
        global lbn_id

        global testo
        global sfondo

        # global path
        database = "C:\\Users\\Massimiliano\\Documents\\GitHub\\PyFatture\\Fatture_new.db"
        # database = path
        # if len(database) != 0:
        conn = sqlite3.connect(database)
        #query =

        a= checkbox_abilitato[id].isChecked()
        b=line_cerca[id].text()
        c=combobox_in[id].currentIndex()
        d=testo[id]
        if (d == '') or (d == 'None'):
            d = None

        e=sfondo[id]

        if (e == '') or (e == 'None'):
            e = None
        f=lbn_id[id].text()


        evidenz = conn.execute("UPDATE Evidenziatori SET isEnable=?, Ricerca=?, inContenuto=?, ColoreTesto=?, ColoreSfondo=? WHERE IdEvidenz=?",(a, b, c, d, e, f))


        conn.commit()
        conn.close()




    def colorpicker(self, type, item, n):
        global sfondo
        global testo

        if (type == 'sfondo'):
                color = QtWidgets.QColorDialog.getColor(QtGui.QColor(sfondo[n]))
        elif (type == 'testo'):
                color = QtWidgets.QColorDialog.getColor(QtGui.QColor(testo[n]))
        else:
                color = QtWidgets.QColorDialog.getColor()
        if (color.isValid()):
                if type == 'sfondo':
                        sfondo[n] = color.name()
                        item.setStyleSheet("background-color: " + sfondo[n] + ";")

                if type == 'testo':
                        testo[n] = color.name()
                        item.setStyleSheet("color: " + testo[n] + ";")

        else:
                if type == 'sfondo':
                        sfondo[n] = ''
                        item.setStyleSheet("")

                if type == 'testo':
                        testo[n] = ''
                        item.setStyleSheet("")

        self.onChange(n)

    def trovatesto(self,n):

        global line_cerca
        global lbn_esempio
        global btn_testo
        global btn_sfondo

        Stile = ''

        item_da = line_cerca[n]
        item_su = lbn_esempio[n]

        item_testo = btn_testo
        item_sfondo = btn_sfondo


        testodacercare = item_da.text()
        contenuto = item_su.text()
        if testodacercare != '':
            if testodacercare in contenuto:

                testo_s = btn_testo[n].styleSheet()
                sfondo_s = btn_sfondo[n].styleSheet()
                es = "border: 1px solid Gray;"
                if testo_s:
                    Stile = Stile + testo_s #+ ";"

                if sfondo_s:
                    Stile = Stile + sfondo_s #+ ";"

                Stile = Stile+es

                lbn_esempio[n].setStyleSheet(Stile)


            else:
                lbn_esempio[n].setStyleSheet("border: 1px solid Gray; color: " + " " + "; background-color: " + " ;")

        else:
            lbn_esempio[n].setStyleSheet("border: 1px solid Gray;")



    def addEvidenz(self):
        global nEvidenz
        if nEvidenz < 20:
            dim = 70 + (nEvidenz * 35)
            MainWindow3.resize(850, dim)
            nEvidenz = nEvidenz + 1

    def onChange(self,id):
        global line_cerca
        global lbn_esempio
        lbn_esempio[id].setText(line_cerca[id].text())
        self.trovatesto(id)
        self.saveEvidenz(id)

    def setupUi(self, MainWindow3):

        global checkbox_abilitato
        global line_cerca
        global label_in
        global combobox_in
        global label_con
        global btn_testo
        global btn_sfondo
        global lbn_esempio
        global lbn_id

        checkbox_abilitato = []
        line_cerca = []
        label_in = []
        combobox_in = []
        label_con = []
        btn_testo = []
        btn_sfondo = []
        lbn_esempio = []
        lbn_id = []

        MainWindow3.setObjectName("MainWindow3")
        #MainWindow.resize(850, 70)
        MainWindow3.setMinimumSize(QtCore.QSize(850, 715))
        MainWindow3.setMaximumSize(QtCore.QSize(850, 715))
        MainWindow3.setWindowIcon(QtGui.QIcon('ico/evidenz.png'))

        items = range(0, 20)

        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")

        for item in items:

            if item == 0:
                pos = 15
            else:
                pos = (pos+35)

            lbn_id.append(QtWidgets.QLabel(self.centralwidget))
            lbn_id[item].setGeometry(QtCore.QRect(0, pos, 22, 22))
            lbn_id[item].setObjectName('label_con_' + str(item))
            lbn_id[item].setText('ID'+ str(item))
            lbn_id[item].setVisible(0)

            checkbox_abilitato.append(QtWidgets.QCheckBox(self.centralwidget))
            checkbox_abilitato[item].setGeometry(QtCore.QRect(12, pos, 22, 22))
            checkbox_abilitato[item].setObjectName('checkbox_abilitato_'+str(item))
            checkbox_abilitato[item].stateChanged.connect(lambda x, item=item: self.onChange(item))

            line_cerca.append(QtWidgets.QLineEdit(self.centralwidget))
            line_cerca[item].setGeometry(QtCore.QRect(40, pos, 180, 22))
            line_cerca[item].setObjectName('line_cerca_'+str(item))
            line_cerca[item].setText("")

            line_cerca[item].textEdited.connect(lambda x, item=item: self.onChange(item))

            label_in.append(QtWidgets.QLabel(self.centralwidget))
            label_in[item].setGeometry(QtCore.QRect(240, pos, 22, 22))
            label_in[item].setObjectName('label_in_'+str(item))

            combobox_in.append(QtWidgets.QComboBox(self.centralwidget))
            combobox_in[item].setGeometry(QtCore.QRect(270, pos, 130, 22))
            combobox_in[item].setObjectName('combobox_in_'+str(item))
            combobox_in[item].addItem("Fornitore")
            combobox_in[item].addItem("Numero Documento")
            combobox_in[item].currentIndexChanged.connect(lambda x, item=item: self.onChange(item))


            label_con.append(QtWidgets.QLabel(self.centralwidget))
            label_con[item].setGeometry(QtCore.QRect(420, pos, 22, 22))
            label_con[item].setObjectName('label_con_'+str(item))

            btn_testo.append(QtWidgets.QPushButton(self.centralwidget))
            btn_testo[item].setGeometry(QtCore.QRect(450, pos, 75, 22))
            btn_testo[item].setObjectName("btn_testo_"+str(item))
            btn_testo[item].clicked.connect(lambda x, item=item: self.colorpicker('testo', btn_testo[item+x], item+x))

            btn_sfondo.append(QtWidgets.QPushButton(self.centralwidget))
            btn_sfondo[item].setGeometry(QtCore.QRect(540, pos, 75, 22))
            btn_sfondo[item].setStyleSheet("")
            btn_sfondo[item].setObjectName("btn_sfondo_"+str(item))
            btn_sfondo[item].clicked.connect(lambda x, item=item: self.colorpicker('sfondo', btn_sfondo[item], item))

            lbn_esempio.append(QtWidgets.QLabel(self.centralwidget))
            lbn_esempio[item].setGeometry(QtCore.QRect(640, pos, 200, 22))
            lbn_esempio[item].setStyleSheet("border: 1px solid Gray;")
            lbn_esempio[item].setText("Esempio " + str(item))
            lbn_esempio[item].setObjectName("label_Esempio_"+str(item))



        #self.menuBar = QtWidgets.QMenuBar(MainWindow)
        #self.menuBar.setGeometry(QtCore.QRect(0, 0, 853, 21))
        #self.menuBar.setObjectName("menuBar")

        #MainWindow.setMenuBar(self.menuBar)

        #self.menuEvidenziatore = QtWidgets.QMenu(self.menuBar)
        #self.menuEvidenziatore.setObjectName("menuEvidenziatore")

        #self.actionEvidenziatore = QtWidgets.QAction(MainWindow)
        #self.actionEvidenziatore.setObjectName("actionEvidenziatore")
        #self.actionEvidenziatore.triggered.connect(self.addEvidenz)

        #self.actionSalvaEvidenziatore = QtWidgets.QAction(MainWindow)
        #self.actionSalvaEvidenziatore.setObjectName("actionSalvaEvidenziatore")
        #self.actionSalvaEvidenziatore.triggered.connect(lambda: self.saveEvidenz(0))

        #self.menuEvidenziatore.addAction(self.actionEvidenziatore)
        #self.menuEvidenziatore.addAction(self.actionSalvaEvidenziatore)

        #self.menuBar.addAction(self.menuEvidenziatore.menuAction())
        MainWindow3.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

        self.loadEvidenz()

    def retranslateUi(self, MainWindow3):

        global checkbox_abilitato
        global line_cerca
        global label_in
        global combobox_in
        global label_con
        global btn_testo
        global btn_sfondo
        global lbn_esempio

        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "Imposta Evidenziatori"))

        items = range(0, 20)
        for item in items:
            label_in[item].setText(_translate("MainWindow3", "in"))
            label_con[item].setText(_translate("MainWindow3", "con"))
            btn_testo[item].setText(_translate("MainWindow3", "Testo"))
            btn_sfondo[item].setText(_translate("MainWindow3", "Sfondo"))

        #self.menuEvidenziatore.setTitle(_translate("MainWindow", "Evidenziatore"))
        #self.actionSalvaEvidenziatore.setText(_translate("MainWindow", "Salva"))
        #self.actionEvidenziatore.setText(_translate("MainWindow", "Aggiungi"))