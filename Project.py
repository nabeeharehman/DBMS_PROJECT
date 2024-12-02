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
        self.Close.clicked.connect(self.close)
        self.CustomerComboBox.currentTextChanged.connect(self.change_mode)
        self.change_mode()
            
        
    def close(self):
        sys.exit()
    
    
    def change_mode(self):
        current=self.CustomerComboBox.currentText()
        
        if current == 'Customer':
            self.SignUP.setEnabled(True)
            self.SignIN.clicked.connect(self.customer_signIN)
            self.SignUP.clicked.connect(self.customer_signUP)
        elif current=='Employee':  
            self.SignUP.setEnabled(False)
            self.SignIN.clicked.connect(self.cmanager_signIN)
            
    def customer_signIN(self):
        self.customer= CustomerSignIN()
        self.customer.show()
        
    def customer_signUP(self):
        self.customer= CustomerSignUP()
        self.customer.show()
    
    def cmanager_signIN(self):
        self.manager= ManagerSignIN()
        self.manager.show()
        
        
        
            
        

class CustomerSignUP(QtWidgets.QMainWindow):
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
        super(CustomerSignUP, self).__init__()

        # Load the .ui file
        uic.loadUi('Customer\\SignUp.ui', self)
        self.show()
        
        self.CustomerConfirm.clicked.connect(self.CsignUP)
        
    
    def CsignUP(self):
        name=self.CustomerName.text()
        cnic= self.CustomerCNIC.text()
        address=self.CustomerAddress.text()
        email=self.CustomerEmailAddress.text()
        phone=self.CustomerPhone.text()
        username=self.CustomerUserName.text()
        password=self.CustomerPassword.text()
        
        server = 'USER-PC\\MYSQLSERVER1'
        database = 'project1'  # Name of your Northwind database
        use_windows_authentication = True  # Set to True to use Windows Authentication
        


        # Create the connection string based on the authentication method chosen
        if use_windows_authentication:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        else:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor to interact with the database
        cursor = connection.cursor()
        
        stored_procedure="EXEC SignupClient @ClientName=?,@ClientUserName=?,@ClientPassword=?,@ClientCNIC=?,@ClientAddress=?,@ClientEmail=?,@ClientPhoneNumber=?"
        cursor.execute(stored_procedure,name,username,password,cnic,address,email,phone)
        if cursor.rowcount > 0: 
            connection.commit()
        else:
            connection.rollback()
        result = cursor.fetchall()
        if result:
            message = result[0]
            QMessageBox.information(self, "SignUP Status", message)
            
            
        else:
            QMessageBox.warning(self, "SignUP Status", "Sign Up failed. Try Again.")
        connection.close()




class ManagerSignIN(QtWidgets.QMainWindow):
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
        super(ManagerSignIN, self).__init__()

        # Load the .ui file
        uic.loadUi('SignIn.ui', self)
        self.show()

        

        # Connect Submit Button to Event Handling Code
        self.LogIN.clicked.connect(self.login)
        
    def login(self):
        username=self.UserName.text()
        password=self.Password.text()
        
        server = 'USER-PC\\MYSQLSERVER1'
        database = 'project1'  # Name of your Northwind database
        use_windows_authentication = True  # Set to True to use Windows Authentication
        


        # Create the connection string based on the authentication method chosen
        if use_windows_authentication:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        else:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor to interact with the database
        cursor = connection.cursor()
        # print(username)
        # print(password)
        stored_procedure = "EXEC LoginManager @ManagerUserName=?,@ManagerPassword=?"
        cursor.execute(stored_procedure, username, password)
        result = cursor.fetchone()
        if result:
            message = result[0]  
            QMessageBox.information(self, "Login Status", message)
            query="select ManagerID from Manager where ManagerUserName=?"
            cursor.execute(query,username)
            managerID=cursor.fetchone()[0]
            print(managerID)
            self.dashboard= ManagerDashboard(managerID)
            self.dashboard.show()
            
            
        else:
            QMessageBox.warning(self, "Login Status", "Invalid username or password.")
        connection.close()
        
        
        

        

        




        
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
        database = 'project1'  # Name of your Northwind database
        use_windows_authentication = True  # Set to True to use Windows Authentication
        


        # Create the connection string based on the authentication method chosen
        if use_windows_authentication:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        else:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor to interact with the database
        cursor = connection.cursor()
        print(username)
        print(password)
        stored_procedure = "EXEC LoginClient @ClientUserName=?,@ClientPassword=?"
        cursor.execute(stored_procedure, username, password)
        result = cursor.fetchone()
        if result:
            message = result[0]  
            QMessageBox.information(self, "Login Status", message)
            query="select ClientID from Client where ClientUsername=?"
            cursor.execute(query,username)
            clientID=cursor.fetchone()[0]
            print(clientID)
            self.dashboard= CustomerDashBoard(clientID)
            self.dashboard.show()
            
            
            
        else:
            QMessageBox.warning(self, "Login Status", "Invalid username or password.")
        connection.close()
        
        

class CustomerDashBoard(QtWidgets.QMainWindow):
    
    def __init__(self, clientID:int):
        
        # Call the inherited classes __init__ method
        super(CustomerDashBoard, self).__init__()
        
        self.ClientID= clientID

        # Load the .ui file
        uic.loadUi('Customer\\Customer Dashboard.ui', self)
        self.show()
        
        server = 'USER-PC\\MYSQLSERVER1'
        database = 'project1'  # Name of your Northwind database
        use_windows_authentication = True  # Set to True to use Windows Authentication
        


        # Create the connection string based on the authentication method chosen
        if use_windows_authentication:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        else:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor to interact with the database
        cursor = connection.cursor()
        query="select ClientName,ClientPhoneNumber,ClientCNIC from Client where ClientID=?"
        cursor.execute(query,clientID)
        result=cursor.fetchone()
        name,phone,cnic=result
        name= "Welcome, "+name
        phone=str(phone)
        cnic=str(cnic)
        
        self.Name.setText(name)
        self.Name.setEnabled(False)
        self.Phone.setText(phone)
        self.Phone.setEnabled(False)
        self.CNIC.setText(cnic)
        self.CNIC.setEnabled(False)
        
        self.BookAppointment.clicked.connect(lambda:self.book(clientID))
        self.ViewAppointments.clicked.connect(lambda:self.view(clientID))
        
    def book(self,clientID:int):
        self.booking=BookAppointment(clientID)
        self.booking.show()
        
    def view(self,clientID:int):
        self.view= ViewAppointment(clientID)
        self.view.show()
        

class BookAppointment(QtWidgets.QMainWindow):
    def __init__(self,clientID:int):
        
        # Call the inherited classes __init__ method
        super(BookAppointment, self).__init__()

        # Load the .ui file
        uic.loadUi('BookAppointment.ui', self)
        self.show()
        
        
        
class ViewAppointment(QtWidgets.QMainWindow):
    def __init__(self,clientID:int):
        
        # Call the inherited classes __init__ method
        super(ViewAppointment, self).__init__()

        # Load the .ui file
        uic.loadUi('Customer\\ViewAppointments.ui', self)
        self.show()
        
        self.ClientID=clientID
        
        server = 'USER-PC\\MYSQLSERVER1'
        database = 'project1'  # Name of your Northwind database
        use_windows_authentication = True  # Set to True to use Windows Authentication
        


        # Create the connection string based on the authentication method chosen
        if use_windows_authentication:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        else:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor to interact with the database
        cursor = connection.cursor()
        query="EXEC PastAppointments @ClientID=?"
        cursor.execute(query,clientID)
        result=cursor.fetchall()
        
        for row_index, row_data in enumerate(result):
            self.History.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.History.setItem(row_index, col_index, item)
                
        
        query1="EXEC FutureAppointments @ClientID=?"
        cursor.execute(query1,clientID)
        result1=cursor.fetchall()
        
        for row_index, row_data in enumerate(result1):
            self.Upcoming.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.Upcoming.setItem(row_index, col_index, item)
                
class ManagerDashboard(QtWidgets.QMainWindow):
    def __init__(self,ManagerID:int):
        
        # Call the inherited classes __init__ method
        super(ManagerDashboard, self).__init__()

        # Load the .ui file
        uic.loadUi('Manager\\ManagerDashboard.ui', self)
        self.show() 
        
        self.Manage.clicked.connect(lambda:self.manage(ManagerID))
        
        
    def manage(self,ID:int):
        self.manage=ManageAppointments(ID)
        self.manage.show()
        
        

class ManageAppointments(QtWidgets.QMainWindow):
    def __init__(self,ManagerID:int):
        
        # Call the inherited classes __init__ method
        super(ManageAppointments, self).__init__()

        # Load the .ui file
        uic.loadUi('Manager\\ManageAppointments.ui', self)
        self.show()
        
        server = 'USER-PC\\MYSQLSERVER1'
        database = 'project1'  # Name of your Northwind database
        use_windows_authentication = True  # Set to True to use Windows Authentication
        


        # Create the connection string based on the authentication method chosen
        if use_windows_authentication:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        else:
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor to interact with the database
        cursor = connection.cursor()
        query="select* from Appointments"
        cursor.execute(query)
        result=cursor.fetchall()
        
        for row_index, row_data in enumerate(result):
            self.Appointment.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.Appointment.setItem(row_index, col_index, item)
                
                
        self.Assign.clicked.connect(lambda:self.assign(ManagerID))
        
#     def assign(ID:int):
        
# class ManageAppointments(QtWidgets.QMainWindow):
#     def __init__(self,ManagerID:int):
        
#         # Call the inherited classes __init__ method
#         super(ManageAppointments, self).__init__()

#         # Load the .ui file
#         uic.loadUi('Manager\\ManageAppointments.ui', self)
#         self.show()
        
        
         

        
        
        
        
        
        
        
        
        
        
        
        
    

        

             

        
def main():
    app = QApplication(sys.argv)
    window = MainScreen()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

    



    
