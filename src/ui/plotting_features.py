from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QToolBar 
from PyQt5.QtWidgets import QTableWidgetItem, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class PlottingFeatures:
    """
    This class is for the processing of the coordinates within
    the kinData table to allow them to be plotted. 
    """
    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()


    def setup_connections(self):
        self.ui.plotButton.clicked.connect(self.handle_plot_button_click)


    def handle_plot_button_click(self):
        self.kinData_values = self.get_kinData_values()
        self.plot_coordinates()
        
        # Re-enable plot viewing buttons
        self.ui.frontView.setEnabled(True)
        self.ui.topView.setEnabled(True)
        self.ui.sideView.setEnabled(True)
        self.ui.rearView.setEnabled(True)

    def get_kinData_values(self):

        # Nested dictionary with 'front' and 'rear' nested
        self.kinData_values = {}

        # Access the tab widget containing the tables
        tab_widget = self.ui.kinData

        for position in ["front", "rear"]:
            self.kinData_values[position] = {}
            
            # Access the correct table widget based on the position
            table_widget_name = f"{position}Input"
            table_widget = tab_widget.findChild(QtWidgets.QTableWidget, table_widget_name)
            
            for i, coordinate_name in enumerate(["upper_leading_pivot",
                                                "upper_trailling_pivot",
                                                "upper_upright_pivot",
                                                "lower_leading_pivot",
                                                "lower_trailling_pivot",
                                                "lower_upright_pivot"]):
                
                self.kinData_values[position][coordinate_name] = []
                
                for column in range(3):
                    # Accessing the item from the current table widget
                    item = table_widget.item(i, column)
                    if item is not None and item.text() != "":
                        self.kinData_values[position][coordinate_name].append(float(item.text()))
                    
        return self.kinData_values
                    
    def plot_coordinates(self):

        # Clear the plot area
        layout = self.ui.plotArea.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

        # Create a Matplotlib figure and canvas
        fig = Figure()
        canvas = FigureCanvas(fig)

        # Add a 3D subplot to the figure
        ax = fig.add_subplot(111, projection='3d')

        # Plot Origin
        ax.scatter(0, 0, 0, c='r', marker='X')

        # Plot the kinData coordinates
        for position, values in self.kinData_values.items():
            x_values = [value[0] for value in values.values()]
            y_values = [value[1] for value in values.values()]
            z_values = [value[2] for value in values.values()]
            ax.scatter(x_values, y_values, z_values, label=position)
            
        # Plot mirrored coordinates (for opposite side)
        for position, values in self.kinData_values.items():
            x_values_mirrored = [value[0]*-1 for value in values.values()]
            y_values = [value[1] for value in values.values()]
            z_values = [value[2] for value in values.values()]
            ax.scatter(x_values_mirrored, y_values, z_values, label=position)
        
        # Plot wishbones
        self.plot_wishbones(ax)
        # x_line = [self.kinData_values['front']['upper_leading_pivot'][0], self.kinData_values['front']['upper_upright_pivot'][0]]
        # y_line = [self.kinData_values['front']['upper_leading_pivot'][1], self.kinData_values['front']['upper_upright_pivot'][1]]
        # z_line = [self.kinData_values['front']['upper_leading_pivot'][2], self.kinData_values['front']['upper_upright_pivot'][2]]
        # #ax.plot(self.kinData_values['front']['upper_leading_pivot'], self.kinData_values['front']['upper_upright_pivot'])
        # ax.plot(x_line, y_line, z_line)
        
        # Hide grid lines and axis
        ax.grid(False)
        ax.axis('off')

        # Create a navigation toolbar for the plot
        toolbar = NavigationToolbar(canvas, self.ui.centralwidget)  # Change self.ui to self.ui.centralwidget

        # Clear the plotArea layout and add the Matplotlib canvas and toolbar
        layout = QVBoxLayout(self.ui.plotArea)
        layout.addWidget(toolbar)
        layout.addWidget(canvas)

        # Update the plotArea widget
        self.ui.plotArea.setLayout(layout)
        
        
    def plot_wishbones(self,ax):
        
        for axle in ['front', 'rear']:
            for position in ['upper', 'lower']:
                for wishbone in ['leading', 'trailling']:
                    
                    x_line = [self.kinData_values[axle][f'{position}_{wishbone}_pivot'][0], self.kinData_values[axle][f'{position}_upright_pivot'][0]]
                    x_line_mirrored = [self.kinData_values[axle][f'{position}_{wishbone}_pivot'][0]*-1, self.kinData_values[axle][f'{position}_upright_pivot'][0]*-1]
                    y_line = [self.kinData_values[axle][f'{position}_{wishbone}_pivot'][1], self.kinData_values[axle][f'{position}_upright_pivot'][1]]
                    z_line = [self.kinData_values[axle][f'{position}_{wishbone}_pivot'][2], self.kinData_values[axle][f'{position}_upright_pivot'][2]]
                    ax.plot(x_line, y_line, z_line)
                    # Plot mirrored wishbones for other side of car
                    ax.plot(x_line, y_line, z_line)
                    ax.plot(x_line_mirrored, y_line, z_line)
                    
                # # Plot Leading
                # x_line = [self.kinData_values[axle][f'{position}_leading_pivot'][0], self.kinData_values[axle][f'{position}_upright_pivot'][0]]
                # y_line = [self.kinData_values[axle][f'{position}_leading_pivot'][1], self.kinData_values[axle][f'{position}_upright_pivot'][1]]
                # z_line = [self.kinData_values[axle][f'{position}_leading_pivot'][2], self.kinData_values[axle][f'{position}_upright_pivot'][2]]
                # ax.plot(x_line, y_line, z_line)
                
                # # Plot Trailling 
                # x_line = [self.kinData_values[axle][f'{position}_trailling_pivot'][0], self.kinData_values[axle][f'{position}_upright_pivot'][0]]
                # y_line = [self.kinData_values[axle][f'{position}_trailling_pivot'][1], self.kinData_values[axle][f'{position}_upright_pivot'][1]]
                # z_line = [self.kinData_values[axle][f'{position}_trailling_pivot'][2], self.kinData_values[axle][f'{position}_upright_pivot'][2]]
                # ax.plot(x_line, y_line, z_line)
                
                # x_line = [self.kinData_values['front']['upper_leading_pivot'][0], self.kinData_values['front']['upper_upright_pivot'][0]]
                # y_line = [self.kinData_values['front']['upper_leading_pivot'][1], self.kinData_values['front']['upper_upright_pivot'][1]]
                # z_line = [self.kinData_values['front']['upper_leading_pivot'][2], self.kinData_values['front']['upper_upright_pivot'][2]]
                
                # ax.plot(x_line, y_line, z_line)