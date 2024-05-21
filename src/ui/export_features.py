## TODO
# Check that the table is not empty

import shutil
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTableWidgetItem
from PyQt5 import QtWidgets
from openpyxl import load_workbook

class ExportFeatures:
    """
    This class handles the functionality of exporting coordinates
    from the UI Table to xslx format using the provided template. 
    """
    
    def __init__(self, ui, plotting_features):
        self.ui = ui
        self.plotting_features = plotting_features
        self.setup_connections()

    def setup_connections(self):
        self.ui.actionExport_to_xls.triggered.connect(self.handle_export_action_triggered)
        

        
    def handle_export_action_triggered(self):    
        
        
        # item = self.ui.frontInput.item(1, 1)
        # if item:  # Check if the item exists
        #     value = item.text()  # Get the text of the item
        #     print(value)
        # else:
        #     print("No item found at specified position")
        
        
        
        
         
        # Select file name and location
        self.export_dialog()
        
    def export_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self.ui, "Save XLSX File", "", "Excel Files (*.xlsx)", options=options)
        if file_name:
             # Dynamically get the directory of the current script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the full path to the template file
            template_path = os.path.join(script_dir, "input", "Excel_Input_Template.xlsx")

            if os.path.exists(template_path):
                # Copy the template file to the specified location
                shutil.copy(template_path, file_name)                
                self.export_file_name = file_name
                self.export_to_excel()
            else:
                print(f"Template file not found at: {self.template_path}, please reinstate Template to this location.")         
                
    def export_to_excel(self):
        # Get kinData_values from plotting_features instance
        #self.kinData_values = self.plotting_features.kinData_values
        
        # Open workbook   
        export_workbook = load_workbook(self.export_file_name)
        sheet = export_workbook.active
        
        # 'Front' tab
        for xlsx_row, table_row in zip(range(3, 9), range(0, 6)): # Iterate over rows
            for xlsx_col, table_col in zip(range(2, 5), range(0, 3)): # Iterate over columns 
                
                # Retrieve value from UITable
                item = self.ui.frontInput.item(1, 1)
                if item:  # Check if the value exists in UITable
                    value = item.text()  # Get the text of the item
                    # Add to xlsx
                    sheet[xlsx_row, xlsx_col] = value
                
                else:
                    print(f"No coordinate found for front {self.ui.frontInput.item(table_row, 0)}")
                
        # Save the workbook
        export_workbook.save(self.export_file_name)
        print(f"Data written to {self.export_file_name}")
        
        
        
        
        
        
        
                
                
    