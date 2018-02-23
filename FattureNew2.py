# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fatture2.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox, QTableWidgetItem
import sqlite3
import datetime
import time
import locale
import os
from decimal import Decimal
#from babel.numbers import format_currency
from EditFattura2 import Ui_MainWindow2 , get_DocId

global path
path = ''

global SaldoMensile
SaldoMensile = []


global anno_selezionato
anno_selezionato = str(datetime.datetime.today().strftime('%Y'))

global mese_selezionato
mese_selezionato = str(datetime.datetime.today().strftime('%m'))

global tabmese

global banca_selezionata
banca_selezionata = 0

locale.setlocale(locale.LC_ALL, '')

class Ui_FinestraIniziale(object):

    def errore(self):
        msg = QMessageBox()
        msg.setWindowTitle('Errore Database')
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Il Database non è stato caricato")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def euro(self, valore):
        #conv = format_currency(valore, 'EUR', locale='it_IT')
        conv = '{0:n}'.format(Decimal(str(valore).replace(',',"."))) + " €"
        return conv

    def cellClick(self, row, col):
        #print("Click on " + str(row) + " " + str(col) + " " + self.tableFebbraio.item(row, 0).text())

        global path
        global mese_selezionato
        global tabmese
        global doc_id

        if mese_selezionato == '01':
            tabmese = self.tableGennaio
        if mese_selezionato == '02':
            tabmese = self.tableFebbraio
        if mese_selezionato == '03':
            tabmese = self.tableMarzo
        if mese_selezionato == '04':
            tabmese = self.tableAprile
        if mese_selezionato == '05':
            tabmese = self.tableMaggio
        if mese_selezionato == '06':
            tabmese = self.tableGiugno
        if mese_selezionato == '07':
            tabmese = self.tableLuglio
        if mese_selezionato == '08':
            tabmese = self.tableAgosto
        if mese_selezionato == '09':
            tabmese = self.tableSettembre
        if mese_selezionato == '10':
            tabmese = self.tableOttobre
        if mese_selezionato == '11':
            tabmese = self.tableNovembre
        if mese_selezionato == '12':
            tabmese = self.tableDicembre

        if col == 1:
            if len(path) != 0:
                conn = sqlite3.connect(path)
                EC = tabmese.item(row, 1).text()
                ID = tabmese.item(row, 0).text()
                if EC == ' ':
                    queryUp = "UPDATE Documenti SET EstrattoConto=1 WHERE IdDocumento=" + ID

                if  EC == '  ':
                    queryUp = "UPDATE Documenti SET EstrattoConto=0 WHERE IdDocumento=" + ID

                conn.execute(str(queryUp))
                conn.commit()
                conn.close()
        elif col == 2:
            return None

        elif col == 11:
            if len(path) != 0:
                conn = sqlite3.connect(path)
                Pagato = tabmese.item(row, 11).text()
                ID = tabmese.item(row, 0).text()
                if Pagato == 'NO':
                    queryUp = "UPDATE Documenti SET PagatoRiscosso=1 WHERE IdDocumento=" + ID

                if Pagato == 'SI':
                    queryUp = "UPDATE Documenti SET PagatoRiscosso=0 WHERE IdDocumento=" + ID

                conn.execute(str(queryUp))
                conn.commit()
                conn.close()
        else:
            if len(path) != 0:
                get_DocId(path, tabmese.item(row, 0).text())
                self.MainWindowEdit = QtWidgets.QMainWindow()
                self.UiEdit = Ui_MainWindow2()
                self.UiEdit.setupUi(self.MainWindowEdit)
                self.MainWindowEdit.show()

        self.CalcolaSaldo()
        self.loadFatture()

    def cellChanged(self, row, col):
        #print("Click on " + str(row) + " " + str(col) + " " + self.tableFebbraio.item(row, 0).text())

        global path
        global mese_selezionato
        global tabmese
        global doc_id

        if mese_selezionato == '01':
            tabmese = self.tableGennaio
        if mese_selezionato == '02':
            tabmese = self.tableFebbraio
        if mese_selezionato == '03':
            tabmese = self.tableMarzo
        if mese_selezionato == '04':
            tabmese = self.tableAprile
        if mese_selezionato == '05':
            tabmese = self.tableMaggio
        if mese_selezionato == '06':
            tabmese = self.tableGiugno
        if mese_selezionato == '07':
            tabmese = self.tableLuglio
        if mese_selezionato == '08':
            tabmese = self.tableAgosto
        if mese_selezionato == '09':
            tabmese = self.tableSettembre
        if mese_selezionato == '10':
            tabmese = self.tableOttobre
        if mese_selezionato == '11':
            tabmese = self.tableNovembre
        if mese_selezionato == '12':
            tabmese = self.tableDicembre

        if col == 2:
            if len(path) != 0:

                ID = tabmese.item(row, 0).text()
                nOP = tabmese.item(row, 2).text()

                try:
                    if nOP == '':
                        queryUp = "UPDATE Documenti SET NumOperazione='" + str(nOP) + "' WHERE IdDocumento=" + ID
                    else:
                        nOP_int = int(nOP)
                        if nOP_int in range(1, 21):
                            queryUp = "UPDATE Documenti SET NumOperazione='" + str(nOP) + "' WHERE IdDocumento=" + ID

                    conn = sqlite3.connect(path)
                    conn.execute(str(queryUp))
                    conn.commit()
                    conn.close()
                except:
                    pass

        self.CalcolaSaldo()
        self.loadFatture()

    def cambia_anno(self):
        global anno_selezionato
        anno_selezionato = self.comboBoxAnno.currentText()
        self.CalcolaSaldo()
        self.loadFatture()

    def cambia_mese(self):
        global mese_selezionato
        mese_selezionato = self.TabMesi.currentIndex()+1

        if len(str(mese_selezionato)) == 1:
            mese_selezionato = '0'+str(mese_selezionato)
        else:
            mese_selezionato = str(mese_selezionato)

        self.CalcolaSaldo()
        self.loadFatture()

    def cambia_banca(self):
        global banca_selezionata

        x = self.comboBoxBanca.currentIndex()
        self.comboBoxIdBanca.setCurrentIndex(x)

        banca_selezionata = int(self.comboBoxIdBanca.currentText())

        #self.comboBoxBanca.setCurrentIndex(banca_selezionata-1)

        self.CalcolaSaldo()
        self.loadFatture()

    def loadBanche(self):
        global path

        if len(path) != 0:
            self.comboBoxBanca.blockSignals(1)
            self.comboBoxBanca.clear()
            self.comboBoxIdBanca.clear()

            conn = sqlite3.connect(path)
            query = "SELECT * FROM Banche ORDER BY IdBanca"
            data_Banche = conn.execute(query)

            for row_number, row_data in enumerate(data_Banche):
                self.comboBoxBanca.addItem(str(row_data[1]))
                self.comboBoxIdBanca.addItem(str(row_data[0]))

            conn.close()
            self.comboBoxBanca.blockSignals(0)

    def loadFatture(self):
        #start_timer = time.time()


        global path
        global anno_selezionato
        global banca_selezionata
        global mese_selezionato
        global tabmese
        global SaldoMensile


        if mese_selezionato == '01':
            tabmese = self.tableGennaio
        if mese_selezionato == '02':
            tabmese = self.tableFebbraio
        if mese_selezionato == '03':
            tabmese = self.tableMarzo
        if mese_selezionato == '04':
            tabmese = self.tableAprile
        if mese_selezionato == '05':
            tabmese = self.tableMaggio
        if mese_selezionato == '06':
            tabmese = self.tableGiugno
        if mese_selezionato == '07':
            tabmese = self.tableLuglio
        if mese_selezionato == '08':
            tabmese = self.tableAgosto
        if mese_selezionato == '09':
            tabmese = self.tableSettembre
        if mese_selezionato == '10':
            tabmese = self.tableOttobre
        if mese_selezionato == '11':
            tabmese = self.tableNovembre
        if mese_selezionato == '12':
            tabmese = self.tableDicembre

        if len(path) != 0:
            conn = sqlite3.connect(path)
            query = "SELECT IdDocumento, EstrattoConto, NumOperazione, strftime('%d/%m/%Y',DataDocumento), strftime('%d/%m/%Y',DataBanca), strftime('%d/%m/%Y',DataValuta), TipoDocumento, Fornitore, NumeroDocumento, NumeroAssegno, SpeseIncasso, PagatoRiscosso, Valore " \
                    "FROM Documenti WHERE IdBanca='" + str(banca_selezionata) + "' AND strftime('%m',DataBanca)='" + str(mese_selezionato) + "' AND strftime('%Y',DataBanca)='" + str(anno_selezionato) + "' ORDER BY date(DataBanca), date(DataValuta), NumOperazione, NumeroDocumento"

            Fatture = conn.execute(query)
            tabmese.blockSignals(1)
            tabmese.setRowCount(0)

            if mese_selezionato == '01':
                saldo = SaldoMensile[0]
            else:

                saldo = SaldoMensile[int(mese_selezionato)-1]

            for row_number, row_data in enumerate(Fatture):
                tabmese.insertRow(row_number)
                valori = []
                for column_number, data in enumerate(row_data):
                    if not data:
                        data = "-"

                    valori.append(str(data))
                    Avere = ["Fattura", "Spese", "Fattura con RID", "Riepilogo"]
                    Dare =["Nota Credito","Accredito","Fattura Emessa"]

                    if column_number == 10:  # 10 = SpeseIncasso
                        if valori[10] != '-':
                            tabmese.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(self.euro(data))))
                        else:
                            tabmese.setItem(row_number, column_number,
                                            QtWidgets.QTableWidgetItem(str(data)))

                    elif column_number == 12:  # 12 = Avere
                        if valori[6] in Avere:  # 6 = TipoDocumento
                            column_number = 13  # 13 = Dare
                            tabmese.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(self.euro(data))))
                            if valori[11] == '1':  # 11 = PagatoRiscosso
                                saldo = saldo - Decimal(data.replace(',',"."))

                            tabmese.setItem(row_number, column_number + 1, QtWidgets.QTableWidgetItem(str(self.euro(saldo))))
                        if valori[6] in Dare:
                            tabmese.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(self.euro(data))))
                            if valori[11] == '1':
                                saldo = saldo + Decimal(data.replace(',',"."))

                            tabmese.setItem(row_number, column_number + 2, QtWidgets.QTableWidgetItem(str(self.euro(saldo))))
                    else:
                        tabmese.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    if column_number == 1:  # 1 = EstrattoConto
                        if valori[column_number] == '1':
                            tabmese.item(row_number, column_number).setBackground(QtGui.QColor("red"))
                            tabmese.item(row_number, column_number).setText('  ')  #DOPPIO SPAZIO
                        else:
                           tabmese.item(row_number, column_number).setBackground(QtGui.QColor("white"))
                           tabmese.item(row_number, column_number).setText(' ')  #SINGOLO SPAZIO

                    if column_number == 11:  # 11 = PagatoRiscosso
                        if valori[column_number] == '1':
                            tabmese.item(row_number, column_number).setText('SI')
                        else:
                            tabmese.item(row_number, column_number).setText('NO')


            if mese_selezionato == '01':
                self.valoreSaldoIniziale.setText(str(self.euro(SaldoMensile[0])))
                self.valoreSaldoFinale.setText(str(self.euro(SaldoMensile[int(mese_selezionato)])))

            else:
                self.valoreSaldoIniziale.setText(str(self.euro(SaldoMensile[int(mese_selezionato)-1])))
                self.valoreSaldoFinale.setText(str(self.euro(SaldoMensile[int(mese_selezionato)])))

            conn.close()
            tabmese.blockSignals(0)


            print('caricato')


        else:
            self.errore()
        #print("LoadFatture --- %s ---" % (time.time() - start_timer))

    def CalcolaSaldo(self):
        #start_timer = time.time()
        global path

        if len(path) != 0:

            conn = sqlite3.connect(path)

            global SaldoMensile

            TotaleFattureMese = []
            TotaleFattureMese.append(Decimal(500000))

            query_TotaleFattureMese = []
            mesi = range(1, 13)
            avere = ["Fattura", "Spese", str('Fattura con RID'), "Riepilogo"]
            dare = ["Nota Credito", "Accredito","Fattura Emessa"]

            for mese in mesi:

                ParzialeFattureMese = Decimal(0)

                if len(str(mese)) == 1:
                    mod_mese = '0' + str(mese)
                else:
                    mod_mese = mese

                query_TotaleFattureMese.append("SELECT TipoDocumento, PagatoRiscosso, Valore FROM Documenti WHERE IdBanca='" + str(banca_selezionata) + "' AND strftime('%m',DataBanca)='" + str(mod_mese) + "' AND strftime('%Y',DataBanca)='" + str(anno_selezionato) + "' ORDER BY date(DataBanca), date(DataValuta), NumOperazione, NumeroDocumento")

                data_TotaleFattureMese = conn.execute(str(query_TotaleFattureMese[mese - 1]))

                for riga_number, riga_dati in enumerate(data_TotaleFattureMese):
                    if riga_dati:
                        if str(riga_dati[0]) in avere:  # 6 = TipoDocumento
                            if riga_dati[1] == 1:  # 11 = PagatoRiscosso
                                ParzialeFattureMese = ParzialeFattureMese - Decimal(riga_dati[2].replace(',', "."))

                        elif riga_dati[0] in dare:
                            if riga_dati[1] == 1:
                                ParzialeFattureMese = ParzialeFattureMese + Decimal(riga_dati[2].replace(',', "."))
                    else:
                        ParzialeFattureMese = TotaleFattureMese[mese - 1]

                TotaleFattureMese.append(ParzialeFattureMese)
            conn.close()

            SaldoMensile = []

            mesi = range(0, 13)
            for x in mesi:
                ParzialeSaldoMese = 0

                if x == 0:
                    ParzialeSaldoMese = TotaleFattureMese[x]
                else:
                    ParzialeSaldoMese = SaldoMensile[x-1] + TotaleFattureMese[x]

                SaldoMensile.append(ParzialeSaldoMese)
        else:
            return None
        #print("CalcolaSaldo --- %s ---" % (time.time() - start_timer))


    def browseFile(self):
        global path

        sfoglia = QFileDialog()
        filter = "Database(*.db)"
        percorso = QFileDialog.getOpenFileName(sfoglia, 'Apri Database', '', filter)
        path = percorso[0]

        if percorso[0]:
            self.loadBanche()
            self.CalcolaSaldo()
            self.loadFatture()
        else:
            return None

    def setupUi(self, FinestraIniziale):

        global tabmese

        ncolonne = 15
        nrighe = 40

        desc_colonne = ["ID", "EC", "nOP", "Data", "Data Banca", "Data Valuta", "Tipologia", "Fornitore", "Numero Documento",
                        'Assegno', "Spese", "Pagato", "Dare", "Avere", "Saldo"]
        width_colonne = [0, 30, 30, 90, 90, 90, 100, 173, 160, 100, 50, 50, 90, 90, 90]

        FinestraIniziale.setObjectName("FinestraIniziale")
        FinestraIniziale.setMinimumSize(QtCore.QSize(1280, 720))
        FinestraIniziale.setMaximumSize(QtCore.QSize(1280, 720))
        FinestraIniziale.setWindowIcon(QtGui.QIcon('ico/croceverde.png'))
        FinestraIniziale.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(FinestraIniziale)
        self.centralwidget.setObjectName("centralwidget")
        self.TabMesi = QtWidgets.QTabWidget(self.centralwidget)
        self.TabMesi.setGeometry(QtCore.QRect(10, 20, 1260, 630))
        self.TabMesi.setAutoFillBackground(False)
        self.TabMesi.setObjectName("TabMesi")

        self.tabGennaio = QtWidgets.QWidget()
        self.tabGennaio.setObjectName("tabGennaio")
        self.tableGennaio = QtWidgets.QTableWidget(self.tabGennaio)
        self.tableGennaio.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableGennaio.setToolTipDuration(3)
        self.tableGennaio.setMidLineWidth(2)
        self.tableGennaio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableGennaio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableGennaio.verticalHeader().setDefaultSectionSize(20)
        self.tableGennaio.setObjectName("tableGennaio")
        self.tableGennaio.setColumnCount(ncolonne)
        self.tableGennaio.setRowCount(nrighe)
        self.tableGennaio.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabGennaio, "")

        self.tabFebbraio = QtWidgets.QWidget()
        self.tabFebbraio.setObjectName("tabFebbraio")
        self.tableFebbraio = QtWidgets.QTableWidget(self.tabFebbraio)
        self.tableFebbraio.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableFebbraio.setToolTipDuration(3)
        self.tableFebbraio.setMidLineWidth(2)
        self.tableFebbraio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableFebbraio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableFebbraio.setObjectName("tableFebbraio")
        self.tableFebbraio.setColumnCount(ncolonne)
        self.tableFebbraio.setRowCount(nrighe)
        self.tableFebbraio.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabFebbraio, "")

        self.tabMarzo = QtWidgets.QWidget()
        self.tabMarzo.setObjectName("tabMarzo")
        self.tableMarzo = QtWidgets.QTableWidget(self.tabMarzo)
        self.tableMarzo.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableMarzo.setToolTipDuration(3)
        self.tableMarzo.setMidLineWidth(2)
        self.tableMarzo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableMarzo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableMarzo.setObjectName("tableMarzo")
        self.tableMarzo.setColumnCount(ncolonne)
        self.tableMarzo.setRowCount(nrighe)
        self.tableMarzo.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabMarzo, "")

        self.tabAprile = QtWidgets.QWidget()
        self.tabAprile.setObjectName("tabAprile")
        self.tableAprile = QtWidgets.QTableWidget(self.tabAprile)
        self.tableAprile.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableAprile.setToolTipDuration(3)
        self.tableAprile.setMidLineWidth(2)
        self.tableAprile.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableAprile.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableAprile.setObjectName("tableAprile")
        self.tableAprile.setColumnCount(ncolonne)
        self.tableAprile.setRowCount(nrighe)
        self.tableAprile.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabAprile, "")

        self.tabMaggio = QtWidgets.QWidget()
        self.tabMaggio.setObjectName("tabMaggio")
        self.tableMaggio = QtWidgets.QTableWidget(self.tabMaggio)
        self.tableMaggio.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableMaggio.setToolTipDuration(3)
        self.tableMaggio.setMidLineWidth(2)
        self.tableMaggio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableMaggio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableMaggio.setObjectName("tableMaggio")
        self.tableMaggio.setColumnCount(ncolonne)
        self.tableMaggio.setRowCount(nrighe)
        self.tableMaggio.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabMaggio, "")

        self.tabGiugno = QtWidgets.QWidget()
        self.tabGiugno.setObjectName("tabGiugno")
        self.tableGiugno = QtWidgets.QTableWidget(self.tabGiugno)
        self.tableGiugno.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableGiugno.setToolTipDuration(3)
        self.tableGiugno.setMidLineWidth(2)
        self.tableGiugno.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableGiugno.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableGiugno.setObjectName("tableGiugno")
        self.tableGiugno.setColumnCount(ncolonne)
        self.tableGiugno.setRowCount(nrighe)
        self.tableGiugno.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabGiugno, "")

        self.tabLuglio = QtWidgets.QWidget()
        self.tabLuglio.setObjectName("tabLuglio")
        self.tableLuglio = QtWidgets.QTableWidget(self.tabLuglio)
        self.tableLuglio.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableLuglio.setToolTipDuration(3)
        self.tableLuglio.setMidLineWidth(2)
        self.tableLuglio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableLuglio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableLuglio.setObjectName("tableLuglio")
        self.tableLuglio.setColumnCount(ncolonne)
        self.tableLuglio.setRowCount(nrighe)
        self.tableLuglio.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabLuglio, "")

        self.tabAgosto = QtWidgets.QWidget()
        self.tabAgosto.setObjectName("tabAgosto")
        self.tableAgosto = QtWidgets.QTableWidget(self.tabAgosto)
        self.tableAgosto.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableAgosto.setToolTipDuration(3)
        self.tableAgosto.setMidLineWidth(2)
        self.tableAgosto.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableAgosto.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableAgosto.setObjectName("tableAgosto")
        self.tableAgosto.setColumnCount(ncolonne)
        self.tableAgosto.setRowCount(nrighe)
        self.tableAgosto.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabAgosto, "")

        self.tabSettembre = QtWidgets.QWidget()
        self.tabSettembre.setObjectName("tabSettembre")
        self.tableSettembre = QtWidgets.QTableWidget(self.tabSettembre)
        self.tableSettembre.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableSettembre.setToolTipDuration(3)
        self.tableSettembre.setMidLineWidth(2)
        self.tableSettembre.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableSettembre.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableSettembre.setObjectName("tableSettembre")
        self.tableSettembre.setColumnCount(ncolonne)
        self.tableSettembre.setRowCount(nrighe)
        self.tableSettembre.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabSettembre, "")

        self.tabOttobre = QtWidgets.QWidget()
        self.tabOttobre.setObjectName("tabOttobre")
        self.tableOttobre = QtWidgets.QTableWidget(self.tabOttobre)
        self.tableOttobre.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableOttobre.setToolTipDuration(3)
        self.tableOttobre.setMidLineWidth(2)
        self.tableOttobre.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableOttobre.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableOttobre.setObjectName("tableOttobre")
        self.tableOttobre.setColumnCount(ncolonne)
        self.tableOttobre.setRowCount(nrighe)
        self.tableOttobre.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabOttobre, "")

        self.tabNovembre = QtWidgets.QWidget()
        self.tabNovembre.setObjectName("tabNovembre")
        self.tableNovembre = QtWidgets.QTableWidget(self.tabNovembre)
        self.tableNovembre.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableNovembre.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tableNovembre.setToolTipDuration(3)
        self.tableNovembre.setMidLineWidth(2)
        self.tableNovembre.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableNovembre.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableNovembre.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableNovembre.setObjectName("tableNovembre")
        self.tableNovembre.setColumnCount(ncolonne)
        self.tableNovembre.setRowCount(nrighe)
        self.tableNovembre.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabNovembre, "")

        self.tabDicembre = QtWidgets.QWidget()
        self.tabDicembre.setObjectName("tabDicembre")
        self.tableDicembre = QtWidgets.QTableWidget(self.tabDicembre)
        self.tableDicembre.setGeometry(QtCore.QRect(10, 10, 1235, 580))
        self.tableDicembre.setToolTipDuration(3)
        self.tableDicembre.setMidLineWidth(2)
        self.tableDicembre.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableDicembre.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableDicembre.setObjectName("tableDicembre")
        self.tableDicembre.setColumnCount(ncolonne)
        self.tableDicembre.setRowCount(nrighe)
        self.tableDicembre.setHorizontalHeaderLabels(desc_colonne)
        self.TabMesi.addTab(self.tabDicembre, "")

        self.comboBoxAnno = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxAnno.setGeometry(QtCore.QRect(830, 10, 200, 22))
        self.comboBoxAnno.setObjectName("comboBoxAnno")
        self.comboBoxAnno.addItem("")
        self.comboBoxAnno.addItem("")
        self.comboBoxAnno.addItem("")
        self.comboBoxAnno.addItem("")
        self.comboBoxAnno.addItem("")


        self.comboBoxBanca = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBanca.setGeometry(QtCore.QRect(1050, 10, 200, 22))
        self.comboBoxBanca.setObjectName("comboBoxBanca")
        self.comboBoxBanca.addItem("")

        self.comboBoxIdBanca = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxIdBanca.setGeometry(QtCore.QRect(1255, 10, 22, 22))
        self.comboBoxIdBanca.setVisible(0)
        self.comboBoxIdBanca.setObjectName("comboBoxIdBanca")

        self.labelSaldoIniziale = QtWidgets.QLabel(self.centralwidget)
        self.labelSaldoIniziale.setGeometry(QtCore.QRect(560, 660, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelSaldoIniziale.setFont(font)
        self.labelSaldoIniziale.setObjectName("labelSaldoIniziale")

        self.labelSaldoFinale = QtWidgets.QLabel(self.centralwidget)
        self.labelSaldoFinale.setGeometry(QtCore.QRect(910, 660, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelSaldoFinale.setFont(font)
        self.labelSaldoFinale.setObjectName("labelSaldoFinale")

        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(780, 8, 25, 25))
        self.btnUpdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUpdate.setStyleSheet("")
        self.btnUpdate.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/Refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdate.setIcon(icon)
        self.btnUpdate.setIconSize(QtCore.QSize(25, 25))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnUpdate.clicked.connect(lambda: self.loadFatture())

        self.valoreSaldoIniziale = QtWidgets.QLabel(self.centralwidget)
        self.valoreSaldoIniziale.setGeometry(QtCore.QRect(750, 660, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.valoreSaldoIniziale.setFont(font)
        self.valoreSaldoIniziale.setObjectName("valoreSaldoIniziale")

        self.valoreSaldoFinale = QtWidgets.QLabel(self.centralwidget)
        self.valoreSaldoFinale.setGeometry(QtCore.QRect(1090, 660, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.valoreSaldoFinale.setFont(font)
        self.valoreSaldoFinale.setObjectName("valoreSaldoFinale")

        FinestraIniziale.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(FinestraIniziale)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuAggiungi = QtWidgets.QMenu(self.menubar)
        self.menuAggiungi.setObjectName("menuAggiungi")

        self.menuStatistiche = QtWidgets.QMenu(self.menubar)
        self.menuStatistiche.setObjectName("menuStatistiche")

        FinestraIniziale.setMenuBar(self.menubar)

        self.actionApri_Database = QtWidgets.QAction(FinestraIniziale)
        self.actionApri_Database.setObjectName("actionApri_Database")
        self.actionApri_Database.triggered.connect(self.browseFile)

        self.actionAggiungi_Documenti = QtWidgets.QAction(FinestraIniziale)
        self.actionAggiungi_Documenti.setObjectName("actionAggiungi_Documenti")

        self.actionDocumenti = QtWidgets.QAction(FinestraIniziale)
        self.actionDocumenti.setObjectName("actionDocumenti")

        self.actionFornitore = QtWidgets.QAction(FinestraIniziale)
        self.actionFornitore.setObjectName("actionFornitore")

        self.actionSaldo_Fine_Anno = QtWidgets.QAction(FinestraIniziale)
        self.actionSaldo_Fine_Anno.setObjectName("actionSaldo_Fine_Anno")

        self.actionSaldo_Fine_Anno_2 = QtWidgets.QAction(FinestraIniziale)
        self.actionSaldo_Fine_Anno_2.setObjectName("actionSaldo_Fine_Anno_2")

        self.actionPer_Anno = QtWidgets.QAction(FinestraIniziale)
        self.actionPer_Anno.setObjectName("actionPer_Anno")

        self.actionPer_Mese = QtWidgets.QAction(FinestraIniziale)
        self.actionPer_Mese.setObjectName("actionPer_Mese")

        self.actionAggiorna = QtWidgets.QAction(FinestraIniziale)
        self.actionAggiorna.setObjectName("actionAggiorna")
        self.actionAggiorna.triggered.connect(lambda: self.loadFatture())

        self.actionEsci = QtWidgets.QAction(FinestraIniziale)
        self.actionEsci.setObjectName("actionEsci")
        self.actionEsci.triggered.connect(lambda: sys.exit())

        self.menuFile.addAction(self.actionApri_Database)
        self.menuFile.addAction(self.actionAggiorna)
        self.menuFile.addAction(self.actionEsci)

        self.menuAggiungi.addAction(self.actionDocumenti)
        self.menuAggiungi.addAction(self.actionFornitore)
        self.menuAggiungi.addAction(self.actionSaldo_Fine_Anno)
        self.menuAggiungi.addAction(self.actionSaldo_Fine_Anno_2)

        self.menuStatistiche.addAction(self.actionPer_Anno)
        self.menuStatistiche.addAction(self.actionPer_Mese)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAggiungi.menuAction())
        self.menubar.addAction(self.menuStatistiche.menuAction())

        for larghezze in range(len(width_colonne)):
            self.tableGennaio.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableGennaio.verticalHeader().setVisible(False)
            self.tableGennaio.verticalHeader().setDefaultSectionSize(20)
            self.tableFebbraio.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableFebbraio.verticalHeader().setVisible(False)
            self.tableFebbraio.verticalHeader().setDefaultSectionSize(20)
            self.tableMarzo.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableMarzo.verticalHeader().setVisible(False)
            self.tableMarzo.verticalHeader().setDefaultSectionSize(20)
            self.tableAprile.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableAprile.verticalHeader().setVisible(False)
            self.tableAprile.verticalHeader().setDefaultSectionSize(20)
            self.tableMaggio.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableMaggio.verticalHeader().setVisible(False)
            self.tableMaggio.verticalHeader().setDefaultSectionSize(20)
            self.tableGiugno.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableGiugno.verticalHeader().setVisible(False)
            self.tableGiugno.verticalHeader().setDefaultSectionSize(20)
            self.tableLuglio.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableLuglio.verticalHeader().setVisible(False)
            self.tableLuglio.verticalHeader().setDefaultSectionSize(20)
            self.tableAgosto.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableAgosto.verticalHeader().setVisible(False)
            self.tableAgosto.verticalHeader().setDefaultSectionSize(20)
            self.tableSettembre.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableSettembre.verticalHeader().setVisible(False)
            self.tableSettembre.verticalHeader().setDefaultSectionSize(20)
            self.tableOttobre.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableOttobre.verticalHeader().setVisible(False)
            self.tableOttobre.verticalHeader().setDefaultSectionSize(20)
            self.tableNovembre.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableNovembre.verticalHeader().setVisible(False)
            self.tableNovembre.verticalHeader().setDefaultSectionSize(20)
            self.tableDicembre.setColumnWidth(larghezze, width_colonne[larghezze])
            self.tableDicembre.verticalHeader().setVisible(False)
            self.tableDicembre.verticalHeader().setDefaultSectionSize(20)

        self.retranslateUi(FinestraIniziale)

        self.TabMesi.setCurrentIndex(int(mese_selezionato)-1)
        self.TabMesi.currentChanged.connect(lambda: self.cambia_mese())

        self.comboBoxAnno.setCurrentIndex(1)

        self.tableGennaio.cellDoubleClicked.connect(self.cellClick)
        self.tableGennaio.cellChanged.connect(self.cellChanged)
        self.tableFebbraio.cellDoubleClicked.connect(self.cellClick)
        self.tableFebbraio.cellChanged.connect(self.cellChanged)
        self.tableMarzo.cellDoubleClicked.connect(self.cellClick)
        self.tableMarzo.cellChanged.connect(self.cellChanged)
        self.tableAprile.cellDoubleClicked.connect(self.cellClick)
        self.tableAprile.cellChanged.connect(self.cellChanged)
        self.tableMaggio.cellDoubleClicked.connect(self.cellClick)
        self.tableMaggio.cellChanged.connect(self.cellChanged)
        self.tableGiugno.cellDoubleClicked.connect(self.cellClick)
        self.tableGiugno.cellChanged.connect(self.cellChanged)
        self.tableLuglio.cellDoubleClicked.connect(self.cellClick)
        self.tableLuglio.cellChanged.connect(self.cellChanged)
        self.tableAgosto.cellDoubleClicked.connect(self.cellClick)
        self.tableAgosto.cellChanged.connect(self.cellChanged)
        self.tableSettembre.cellDoubleClicked.connect(self.cellClick)
        self.tableSettembre.cellChanged.connect(self.cellChanged)
        self.tableOttobre.cellDoubleClicked.connect(self.cellClick)
        self.tableOttobre.cellChanged.connect(self.cellChanged)
        self.tableNovembre.cellDoubleClicked.connect(self.cellClick)
        self.tableNovembre.cellChanged.connect(self.cellChanged)
        self.tableDicembre.cellDoubleClicked.connect(self.cellClick)
        self.tableDicembre.cellChanged.connect(self.cellChanged)

        self.comboBoxAnno.currentIndexChanged.connect(lambda: self.cambia_anno())

        self.comboBoxBanca.currentIndexChanged.connect(lambda: self.cambia_banca())

        QtCore.QMetaObject.connectSlotsByName(FinestraIniziale)


    def retranslateUi(self, FinestraIniziale):
        _translate = QtCore.QCoreApplication.translate
        FinestraIniziale.setWindowTitle(_translate("FinestraIniziale", "Fatture Farmacia Santoro"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabGennaio), _translate("FinestraIniziale", "Gennaio"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabFebbraio), _translate("FinestraIniziale", "Febbraio"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabMarzo), _translate("FinestraIniziale", "Marzo"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabAprile), _translate("FinestraIniziale", "Aprile"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabMaggio), _translate("FinestraIniziale", "Maggio"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabGiugno), _translate("FinestraIniziale", "Giugno"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabLuglio), _translate("FinestraIniziale", "Luglio"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabAgosto), _translate("FinestraIniziale", "Agosto"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabSettembre), _translate("FinestraIniziale", "Settembre"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabOttobre), _translate("FinestraIniziale", "Ottobre"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabNovembre), _translate("FinestraIniziale", "Novembre"))
        self.TabMesi.setTabText(self.TabMesi.indexOf(self.tabDicembre), _translate("FinestraIniziale", "Dicembre"))
        self.comboBoxAnno.setItemText(0, _translate("FinestraIniziale", "2017"))
        self.comboBoxAnno.setItemText(1, _translate("FinestraIniziale", "2018"))
        self.comboBoxAnno.setItemText(2, _translate("FinestraIniziale", "2019"))
        self.comboBoxAnno.setItemText(3, _translate("FinestraIniziale", "2020"))
        self.comboBoxAnno.setItemText(4, _translate("FinestraIniziale", "2021"))
        self.comboBoxBanca.setItemText(0, _translate("FinestraIniziale", "Banca"))
        #self.comboBoxBanca.setItemText(1, _translate("FinestraIniziale", "Banca2"))
        #self.comboBoxBanca.setItemText(2, _translate("FinestraIniziale", "Banca3"))
        #self.comboBoxBanca.setItemText(3, _translate("FinestraIniziale", "Banca4"))
        #self.comboBoxBanca.setItemText(4, _translate("FinestraIniziale", "Banca5"))
        #self.comboBoxBanca.setItemText(5, _translate("FinestraIniziale", "Banca6"))
        self.labelSaldoIniziale.setText(_translate("FinestraIniziale", "Saldo Inizio Mese:"))
        self.labelSaldoFinale.setText(_translate("FinestraIniziale", "Saldo Fine Mese:"))
        self.valoreSaldoIniziale.setText(_translate("FinestraIniziale", "0,0 €"))
        self.valoreSaldoFinale.setText(_translate("FinestraIniziale", "0,0 €"))
        self.menuFile.setTitle(_translate("FinestraIniziale", "File"))
        self.menuAggiungi.setTitle(_translate("FinestraIniziale", "Aggiungi"))
        self.menuStatistiche.setTitle(_translate("FinestraIniziale", "Statistiche"))
        self.actionApri_Database.setText(_translate("FinestraIniziale", "Apri Database"))
        self.actionAggiungi_Documenti.setText(_translate("FinestraIniziale", "Aggiungi Documenti"))
        self.actionDocumenti.setText(_translate("FinestraIniziale", "Documenti"))
        self.actionFornitore.setText(_translate("FinestraIniziale", "Fornitore"))
        self.actionSaldo_Fine_Anno.setText(_translate("FinestraIniziale", "Banca"))
        self.actionSaldo_Fine_Anno_2.setText(_translate("FinestraIniziale", "Saldo Fine Anno"))
        self.actionPer_Anno.setText(_translate("FinestraIniziale", "Per Anno"))
        self.actionPer_Mese.setText(_translate("FinestraIniziale", "Per Mese"))
        self.actionAggiorna.setText(_translate("FinestraIniziale", "Aggiorna"))
        self.actionEsci.setText(_translate("FinestraIniziale", "Esci"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    FinestraIniziale = QtWidgets.QMainWindow()
    ui = Ui_FinestraIniziale()
    ui.setupUi(FinestraIniziale)
    FinestraIniziale.show()

    sys.exit(app.exec_())

