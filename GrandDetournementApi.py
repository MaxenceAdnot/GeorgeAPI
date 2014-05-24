import sqlite3
import os


class GrandDetournementApi:

    def __init__(self):
        self.__openingDB()

    def __del__(self):
        self.__closingDB()

    def __openingDB(self):
        if os.path.exists("granddetournement.db"):
            self.db_desc = sqlite3.connect("granddetournement.db")
        else:
            self.db_desc = sqlite3.connect(":memory:")

    def __closingDB(self):
        self.db_desc.close()
    
    def returnQuote(self):
        try:
            cur = self.db_desc.cursor()
            cur.execute('''SELECT personnage, replique FROM GrandDetournement ORDER BY RANDOM() LIMIT 1''')
            character, quote = cur.fetchone()
        except Exception:
            print("Can't handle the cursor request")
            character = "Unknown"
            quote = "Try again something went wrong"
        
        return str("%s : %s" % (character, quote))
        
        
