import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from records import Ui_MainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('data/records.sqlite')
        self.rec()


    def rec(self):
        # вывод таблицы с рекордами
        cur = self.con.cursor()
        result = cur.execute("""SELECT name, kol_vo_score FROM records
            ORDER BY kol_vo_score DESC""").fetchall()
        self.results_table_widget.setColumnCount(2)
        self.results_table_widget.setRowCount(0)
        self.results_table_widget.setHorizontalHeaderLabels(["Имя", "Счет"])
        for i, row in enumerate(result):
            self.results_table_widget.setRowCount(self.results_table_widget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.results_table_widget.setItem(i, j, QTableWidgetItem(str(elem)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
