import sqlite3

global path

path =  "C:\\Users\\Massimiliano\\Documents\\GitHub\\PyFatture\\Fatture_new.db"

def load():
    if len(path) != 0:
        conn = sqlite3.connect(path)
        #query = "SELECT * FROM Fornitori ORDER BY IdFornitore"



        conn.execute("UPDATE Documenti SET NumOperazione=? WHERE NumOperazione=?", (0, ''))

        conn.commit()
        conn.close()

load()



