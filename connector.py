from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()

    def create_query(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("expences_db.db")
        if not db.open():
            QtWidgets.QMessageBox.critical(None, "База данных не найдена", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS project (ID integer primary key AUTOINCREMENT, Allsum integer, sumTree integer, sumTree125 integer, sumTree1 integer, recovery integer, recoveryLichen integer, recoverySoil integer")
        return True

    def execute_query(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()


    def add_project(self, date):
        sql_query = "INSERT INTO project (Allsum, sumTree, sumTree125, sumTree1, recovery, recoveryLichen, recoverySoil) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.execute_query(sql_query, date)

    def delete_project(self, id):
        sql_query = "DELETE FROM project WHERE ID=?"

        self.execute_query(sql_query, [id])

    def get_all_projects(self):
        sql_query = "SELECT id from project"
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        query.exec()
        if query.next():
            return query
        return None

    def get_project(self, id):
        sql_query = f"SELECT * from project where ID = {id}"
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        query.exec()
        if query.next():
            return query
        return None

