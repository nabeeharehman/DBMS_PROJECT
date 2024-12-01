# Importing essential modules
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

class UI(QtWidgets.QMainWindow):
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
        super(UI, self).__init__()

        # Load the .ui file
        uic.loadUi('MainWindow.ui', self)

        # Load Orders data
        self.populate_table()

        # Connect Submit Button to Event Handling Code
        self.InsertOrder.clicked.connect(self.open_master_form)

    def populate_table(self):
        """
        Populates the 'orderTable' with data from the Northwind database.

        This function connects to the Northwind database, retrieves orders data,
        and populates the 'orderTable' widget with the fetched data. It also adjusts
        the column widths for better content display.

        Note:
        - Ensure that the 'orderTable' widget is set up and available in the UI.
        - The database connection parameters (server, database, authentication) should
        be correctly configured.

        Returns:
        None
        """
        server = 'USER-PC\MYSQLSERVER1'
        database = 'Northwind'  # Name of your Northwind database
        use_windows_authentication = True
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        # TODO: Provide the  connection string to connect to the Northwind database
        connection = pyodbc.connect(connection_string)

        cursor = connection.cursor()

        # TODO: Write SQL query to fetch orders data
        cursor.execute("SELECT * FROM Orders")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.orderTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.orderTable.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust content display
        header = self.orderTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def open_master_form(self):
        """
        Opens the master transaction form.

        This function is called when the "Insert Order" button is clicked in the main
        UI. It creates and displays the master transaction form (Master class).

        Note:
        - Ensure that the Master class (master_form) is defined and available in the script.

        Returns:
        None
        """
        self.master_form = Master()
        self.master_form.show()