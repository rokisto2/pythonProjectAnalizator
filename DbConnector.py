import sqlite3;

from PySide6 import QtWidgets


class DbConnector:
    def __init__(self):
        self.connector = sqlite3.connect("expences_db.db")

    def add_project(self, data):
        cursor = self.connector.cursor()

        cursor.execute("SELECT ID FROM project")
        ans = cursor.fetchall()

        if len(ans) == 5:
            return -1
        else:

            cursor.execute("INSERT INTO project (AllSum, TreeSum, Tree125Sum, Tree1Sum, recovery, recoveryLichen, recoverySoil) VALUES (?, ?,?, ?,?, ?,? )", data)
            self.connector.commit()
            cursor.execute("SELECT ID FROM project")
            ans = cursor.fetchall()
            id  = ans[len(ans)-1][0]
            return id




    def all_projects(self):
        cursor = self.connector.cursor()

        cursor.execute("SELECT ID FROM project")

        return cursor.fetchall()

    def get_project(self,id):
        cursor = self.connector.cursor()

        cursor.execute(f"SELECT * FROM project WHERE ID = {id}")

        return cursor.fetchall()

    def del_project(self,id):
        cursor = self.connector.cursor()

        cursor.execute(f"DELETE FROM project WHERE ID = {id}")

        self.connector.commit()
