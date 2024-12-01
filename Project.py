# Importing essential modules
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

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
        super(UI, self).__init__()

        # Load the .ui file
        uic.loadUi('main menu.ui', self)

        

        # Connect Submit Button to Event Handling Code
        self.CustomerComboBox.clicked.connect(self.open_master_form)

    



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
        uic.loadUi('main menu.ui', self)

        

        # Connect Submit Button to Event Handling Code
        self.CustomerComboBox.clicked.connect(self.open_master_form)

    



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
