import sqlite3
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtUiTools import  QUiLoader
from functools import partial



class MainWindow(QMainWindow):
      def __init__(self):
          super().__init__()

          loader = QUiLoader()
          self.ui = loader.load("design.ui")
          self.ui.show()
          self.conn = sqlite3.connect("Contacts.db")
          self.my_cursor = self.conn.cursor()

          self.load_data()

      def load_data(self):
          self.my_cursor.execute("SELECT * FROM Persons")
          Result = self.my_cursor.fetchall()  

          for i in range(len(Result)):
            label = QLabel()
            label.setText(Result[i][1])
            self.ui.verticalLayout.addWidget(label)




app = QApplication()
main__window = MainWindow()
app.exec()
