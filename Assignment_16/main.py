from asyncio.windows_events import NULL
import sqlite3
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtUiTools import  QUiLoader
from functools import partial
import qdarkstyle


class ContactList(QMainWindow):
      def __init__(self ,ui):
          super().__init__()
          self.db = NULL
          self.ui = ui
          self.ui.show()
          self.conn = sqlite3.connect("Contacts.db")
          self.my_cursor = self.conn.cursor()
          self.ui.remove_selected.clicked.connect(partial(self.remove_selected_contacts))
          self.ui.remove_All.clicked.connect(partial(self.remove_All_contacts))
          self.ui.save.clicked.connect(partial(self.Form))
          self.load_data()


      def load_data(self):
            self.my_cursor.execute("SELECT * FROM Persons")
            self.db = self.my_cursor.fetchall()  
            self.update_table()

      def remove_selected_contacts(self):
          selected = self.ui.tableWidget.currentRow()
          self.ui.tableWidget.removeRow(selected)
          self.my_cursor.execute(f"DELETE FROM Persons WHERE name ='{self.db[selected][1]}';")
          self.conn.commit()
          self.db.pop(selected)

      def remove_All_contacts(self):
          self.ui.tableWidget.setRowCount(0)
          self.db = NULL
          self.my_cursor.execute(f"DELETE FROM Persons;")
          self.conn.commit()          

      def Form(self):
          if self.ui.name_input.text() != '' or self.ui.family_input.text() !='' or self.ui.mobile_input.text() !='' or self.ui.phone_input.text() !='' or self.ui.email_input.text() !='':
            new_contact = (0,self.ui.name_input.text(),self.ui.family_input.text(),self.ui.mobile_input.text(),self.ui.phone_input.text(),self.ui.email_input.text())
            self.db.append(new_contact)
            self.my_cursor.execute(f"INSERT INTO Persons (name,family,mobile_number,phone_number,email)VALUES ('{self.ui.name_input.text()}', '{self.ui.family_input.text()}', '{self.ui.mobile_input.text()}','{self.ui.phone_input.text()}','{self.ui.email_input.text()}');")
            self.conn.commit()
            self.update_table()
            self.ui.name_input.setText("")
            self.ui.family_input.setText("")
            self.ui.mobile_input.setText("")
            self.ui.phone_input.setText("")
            self.ui.email_input.setText("")

      def update_table(self):

          self.ui.tableWidget.setColumnCount(5)  
          self.ui.tableWidget.setRowCount(len(self.db))
          self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
          self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
          self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
          self.ui.tableWidget.setSortingEnabled(True)  
          myListOfHeaderLabels = ['Name' , 'Family' , 'Mobile' , 'Phone' , 'Email']
          self.ui.tableWidget.setHorizontalHeaderLabels(myListOfHeaderLabels)       

          for i in range(0,len(self.db)):
              for j in range (1,6):             
               self.ui.tableWidget.setItem(i,j-1, QTableWidgetItem(self.db[i][j]))      


app = QApplication()
app.setStyleSheet(qdarkstyle.load_stylesheet())
loader = QUiLoader()
ui = loader.load("design.ui")

def change_theme():
    if ui.checkBox.isChecked():
      app.setStyleSheet(qdarkstyle.load_stylesheet())
    else:
      app.setStyleSheet(None)

ui.checkBox.clicked.connect(partial(change_theme))
contactlist = ContactList(ui)
app.exec()