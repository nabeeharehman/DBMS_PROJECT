# Importing essential modules
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QLineEdit,QPushButton,QLabel,QComboBox,QDateEdit,QRadioButton,QCheckBox,QTextEdit,QMessageBox
import sys
import pyodbc


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(UI, self).__init__()

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initialize the main UI window.

        This constructor is called when an instance of the UI class is created.
        It performs the following tasks:
        1. Calls the constructor of the inherited class.
        2. Loads the user interface (UI) from the 'MainWindow.ui' file.
        3. Populates the 'orderTable' with data.
        4. Connects the "Insert Order" button to the event handler for opening the
        master transaction form.

        Note:
        - The 'MainWindow.ui' file should exist and contain the required UI elements.

        Returns:
        None
        """
        # Call the inherited classes __init__ method
        super(MainScreen, self).__init__()

        # Load the .ui file
        uic.loadUi('main menu.ui', self)
        self.show()

        

        # Connect Submit Button to Event Handling Code
        self.CustomerComboBox.currentTextChanged.connect(self.change_mode)
        
        current=self.CustomerComboBox.currentText()
        
        if current=='Customer':
            self.SignIN.clicked.connect(self.customer_signIN)
            # self.SignUP.clicked.connect(self.customer_signUP)
            
        elif current=="Employee":
            self.SignUP.setEnabled(False)
        #     # self.SignIN.clicked.connect(self.manager_signIN)
    
    
    def change_mode(self):
        current=self.CustomerComboBox.currentText()
        
        if current=='Customer':
            self.SignIN.clicked.connect(self.customer_signIN)
            # self.SignUP.clicked.connect(self.customer_signUP)
            
        elif current=="Manager":
            self.SignUP.setEnabled(False)
            # self.SignIN.clicked.connect(self.manager_signIN)
            
    def customer_signIN(self):
        self.customer= CustomerSignIN()
        self.customer.show()
        
    # def customer_signUP(self):
    #     self.customer= CustomerSignUP()
    #     self.customer.show()
    
    # def cmanager_signIN(self):
    #     self.manager= ManagerSignIN()
    #     self.manager.show()
        
        
        
            
        

    




        
class CustomerSignIN(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initialize the main UI window.

        This constructor is called when an instance of the UI class is created.
        It performs the following tasks:
        1. Calls the constructor of the inherited class.
        2. Loads the user interface (UI) from the 'MainWindow.ui' file.
        3. Populates the 'orderTable' with data.
        4. Connects the "Insert Order" button to the event handler for opening the
        master transaction form.

        Note:
        - The 'MainWindow.ui' file should exist and contain the required UI elements.

        Returns:
        None
        """
        # Call the inherited classes __init__ method
        super(CustomerSignIN, self).__init__()

        # Load the .ui file
        uic.loadUi('SignIn.ui', self)
        self.show()

        

        # Connect Submit Button to Event Handling Code
        self.LogIN.clicked.connect(self.login)
        
    def login(self):
        username=self.UserName.text()
        password=self.Password.text()
        
        server = 'USER-PC\\MYSQLSERVER1'
        database = 'project_database'  # Name of your Northwind database
        use_windows_authentication = True  # Set to True to use Windows Authentication
        username = 'your_username'  # Specify a username if not using Windows Authentication
        password = 'your_password'  # Specify a password if not using Windows Authentication


        # Create the connection string based on the authentication method chosen
        if use_windows_authentication:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        else:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor to interact with the database
        cursor = connection.cursor()
        
        stored_procedure = "EXEC LoginClient @ClientUserName=?,@ClientPassword=?"
        cursor.execute(stored_procedure, username, password)
        result = cursor.fetchone()
        if result:
            message = result[0]  
            QMessageBox.information(self, "Login Status", message)
        else:
            QMessageBox.warning(self, "Login Status", "Invalid username or password.")
        connection.close()
        
        

        
def main():
    app = QApplication(sys.argv)
    window = MainScreen()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

    



    
