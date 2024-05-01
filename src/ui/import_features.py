from PyQt5.QtWidgets import QFileDialog
from openpyxl import load_workbook
from PyQt5.QtWidgets import QTableWidgetItem


class ImportFeatures:
    """
    This class handles the functionality of importing coordinates
    from the provided xlsx template to the UI Table. 
    """
    
    def __init__(self, ui):
        self.ui = ui 
        self.setup_connections()


    def setup_connections(self):
        self.ui.actionImport_from_xls.triggered.connect(self.handle_import_action_triggered)


    def handle_import_action_triggered(self):
        # Select xlsx file for import using file dialouge
        file_dialog = QFileDialog(self.ui.centralwidget)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Excel Files (*.xlsx)")
        file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)  # Ensure single file selection
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                print("Selected file:", file_path)
                self.read_excel_data(file_path)

                
    def read_excel_data(self, file_path):
        workbook = load_workbook(filename=file_path)
        # Read data from the first sheet
        xlsx_data = workbook.active
                                
        # Add data to kinData UI Table
        # For front 
        # Iterate over rows in the XLSX data
        table_start_row = 0
        table_start_col = 0
        for xlsx_row, table_row in zip(range(3, 9), range(table_start_row, table_start_row + 6)):
            # Iterate over columns in the XLSX data
            for xlsx_col, table_col in zip(range(2, 5), range(table_start_col, table_start_col + 3)):
                # Retrieve the value from the XLSX file
                value = xlsx_data.cell(row=xlsx_row, column=xlsx_col).value
                # Create a QTableWidgetItem with the value
                item = QTableWidgetItem(str(value))
                # Set the item in the table at the corresponding row and column
                self.ui.frontInput.setItem(table_row, table_col, item)
                
        # For rear 
        # Iterate over rows in the xlsx data
        for xlsx_row, table_row in zip(range(3, 9), range(table_start_row, table_start_row + 6)):
            # Iterate over columns in the xlsx data
            for xlsx_col, table_col in zip(range(5, 8), range(table_start_col, table_start_col + 3)):
                # Retrieve the value from the xlsx file
                value = xlsx_data.cell(row=xlsx_row, column=xlsx_col).value
                # Create a QTableWidgetItem with the value
                item = QTableWidgetItem(str(value))
                # Set the item in the table at the corresponding row and column
                self.ui.rearInput.setItem(table_row, table_col, item)