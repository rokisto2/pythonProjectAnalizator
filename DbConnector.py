import sqlite3;

class DbConnector:
    def __init__(self):
        self.con = sqlite3.connect("metanit.db")
