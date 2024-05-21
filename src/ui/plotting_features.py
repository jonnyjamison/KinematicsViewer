from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QMessageBox
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ui.analysis_features import AnalysisFeatures

class PlottingFeatures:
    """
    This class is for the processing of the coordinates within
    the kinData table to allow them to be plotted. 
    """
    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()
        self.analysis_features = None  # Initialize analysis_features attribute
        
    def setup_connections(self):
        self.ui.plotButton.clicked.connect(self.handle_plot_button_click) # 'Plot!' UI button
        # lambda function as connect expects slot function with 0 arguements
        self.ui.frontViewButton.clicked.connect(lambda: self.handle_plot_view_button_click('front'))
        self.ui.sideViewButton.clicked.connect(lambda: self.handle_plot_view_button_click('side')) 
        self.ui.topViewButton.clicked.connect(lambda: self.handle_plot_view_button_click('top')) 
        self.ui.rearViewButton.clicked.connect(lambda: self.handle_plot_view_button_click('rear')) 

    def handle_plot_button_click(self):
        try:
            self.kinData_values = self.get_kinData_values()
            self.plot_coordinates()
            
            # Re-enable plot viewing buttons
            self.ui.frontViewButton.setEnabled(True)
            self.ui.topViewButton.setEnabled(True)
            self.ui.sideViewButton.setEnabled(True)
            self.ui.rearViewButton.setEnabled(True)
            
            # Re-enable check boxes
            self.ui.checkRollCentre.setEnabled(True)
            self.ui.checkWheelAxis.setEnabled(True)
            self.ui.checkShowTyres.setEnabled(True)

            # Create instance of analysis_features for Roll centre, etc. 
            if not self.analysis_features:
                self.analysis_features = AnalysisFeatures(self, self.ui)
                
        except:
            self.show_coord_error_dialog()

    def get_kinData_values(self):
        # Nested dictionary with 'front' and 'rear' nested
        self.kinData_values = {}

        # Access the tab widget containing the tables
        tab_widget = self.ui.kinData

        for axle in ["front", "rear"]:
            self.kinData_values[axle] = {}
            
            # Access the correct table widget based on the position
            table_widget_name = f"{axle}Input"
            table_widget = tab_widget.findChild(QtWidgets.QTableWidget, table_widget_name)
            
            for i, coordinate_name in enumerate(["upper_leading_pivot",
                                                "upper_trailling_pivot",
                                                "upper_upright_pivot",
                                                "lower_leading_pivot",
                                                "lower_trailling_pivot",
                                                "lower_upright_pivot"]):
                
                self.kinData_values[axle][coordinate_name] = []
                
                for column in range(3):
                    # Accessing the item from the current table widget
                    item = table_widget.item(i, column)
                    if item is not None and item.text() != "":
                        self.kinData_values[axle][coordinate_name].append(float(item.text()))
                    
        return self.kinData_values
                    
    def plot_coordinates(self):
        if not hasattr(self, 'fig'):
            # Create a Matplotlib figure and canvas
            self.fig = Figure()
            self.canvas = FigureCanvas(self.fig)

            # Add a 3D subplot to the figure
            self.ax = self.fig.add_subplot(111, projection='3d')

            # Plot Origin
            self.ax.scatter(0, 0, 0, c='r', marker='X')
            
            # Plot the kinData coordinates
            for position, values in self.kinData_values.items():
                x_values = [value[0] for value in values.values()]
                y_values = [value[1] for value in values.values()]
                z_values = [value[2] for value in values.values()]
                self.ax.scatter(x_values, y_values, z_values, label=position)
                
            # Plot mirrored coordinates (for opposite side)
            for position, values in self.kinData_values.items():
                x_values_mirrored = [value[0]*-1 for value in values.values()]
                y_values = [value[1] for value in values.values()]
                z_values = [value[2] for value in values.values()]
                self.ax.scatter(x_values_mirrored, y_values, z_values, label=position)
            
            # Plot wishbones
            self.plot_wishbones()
            
            # Dynamically work out axis limits to make agnostic of units & origin
            # Equal to +5% from front leading & rear trailing wishbones
            axis_limit_upper = max(self.kinData_values['front']['lower_leading_pivot'][2], self.kinData_values['rear']['lower_trailling_pivot'][2]) * 1.05
            axis_limit_lower = min(self.kinData_values['front']['lower_leading_pivot'][2], self.kinData_values['rear']['lower_trailling_pivot'][2]) * 1.05 
            self.ax.set_xlim(axis_limit_lower, axis_limit_upper)
            self.ax.set_ylim(axis_limit_lower, axis_limit_upper)
            self.ax.set_zlim(axis_limit_lower, axis_limit_upper)
            
            # Hide grid lines and axis
            self.ax.grid(False)
            self.ax.axis('off')

            # Create a navigation toolbar for the plot
            toolbar = NavigationToolbar(self.canvas, self.ui.centralwidget)  # Change self.ui to self.ui.centralwidget

            # Clear the plotArea layout and add the Matplotlib canvas and toolbar
            layout = QVBoxLayout(self.ui.plotArea)
            layout.addWidget(toolbar)
            layout.addWidget(self.canvas)

            # Update the plotArea widget
            self.ui.plotArea.setLayout(layout)

        else:
            # Clear the previous plot
            self.ax.clear()

            # Plot Origin
            self.ax.scatter(0, 0, 0, c='r', marker='X')
            
            # Plot the kinData coordinates
            for position, values in self.kinData_values.items():
                x_values = [value[0] for value in values.values()]
                y_values = [value[1] for value in values.values()]
                z_values = [value[2] for value in values.values()]
                self.ax.scatter(x_values, y_values, z_values, label=position)
                
            # Plot mirrored coordinates (for opposite side)
            for position, values in self.kinData_values.items():
                x_values_mirrored = [value[0]*-1 for value in values.values()]
                y_values = [value[1] for value in values.values()]
                z_values = [value[2] for value in values.values()]
                self.ax.scatter(x_values_mirrored, y_values, z_values, label=position)
            
            # Plot wishbones
            self.plot_wishbones()
            
            # Dynamically work out axis limits to make agnostic of units & origin
            # Equal to +5% from front leading & rear trailing wishbones
            axis_limit_upper = max(self.kinData_values['front']['lower_leading_pivot'][2], self.kinData_values['rear']['lower_trailling_pivot'][2]) * 1.05
            axis_limit_lower = min(self.kinData_values['front']['lower_leading_pivot'][2], self.kinData_values['rear']['lower_trailling_pivot'][2]) * 1.05 
            self.ax.set_xlim(axis_limit_lower, axis_limit_upper)
            self.ax.set_ylim(axis_limit_lower, axis_limit_upper)
            self.ax.set_zlim(axis_limit_lower, axis_limit_upper)
            
            # Set initial view parallel to the x-axis
            self.ax.view_init(elev=180, azim=270)
            canvas = self.ui.plotArea.layout().itemAt(1).widget()
            canvas.draw()
            
            # Hide grid lines and axis
            self.ax.grid(False)
            self.ax.axis('off')

            # Refresh canvas
            self.canvas.draw()            
        
    def plot_wishbones(self):
        for axle in ['front', 'rear']:
            for position in ['upper', 'lower']:
                for wishbone in ['leading', 'trailling']:
                    
                    x_line = [self.kinData_values[axle][f'{position}_{wishbone}_pivot'][0], self.kinData_values[axle][f'{position}_upright_pivot'][0]]
                    x_line_mirrored = [self.kinData_values[axle][f'{position}_{wishbone}_pivot'][0]*-1, self.kinData_values[axle][f'{position}_upright_pivot'][0]*-1]
                    y_line = [self.kinData_values[axle][f'{position}_{wishbone}_pivot'][1], self.kinData_values[axle][f'{position}_upright_pivot'][1]]
                    z_line = [self.kinData_values[axle][f'{position}_{wishbone}_pivot'][2], self.kinData_values[axle][f'{position}_upright_pivot'][2]]
                    self.ax.plot(x_line, y_line, z_line)
                    # Plot mirrored wishbones for other side of car
                    self.ax.plot(x_line, y_line, z_line)
                    self.ax.plot(x_line_mirrored, y_line, z_line)

    def handle_plot_view_button_click(self,view):
        if view == 'front':
            # Set view parallel to the x-axis
            self.ax.view_init(elev=90, azim=270)
            canvas = self.ui.plotArea.layout().itemAt(1).widget()  # Assuming the canvas is the second widget in the layout
            canvas.draw()
            
        elif view == 'side':
            # Set view parallel to the x-axis
            self.ax.view_init(elev=0, azim=0)
            canvas = self.ui.plotArea.layout().itemAt(1).widget()
            canvas.draw()
            
        elif view == 'top':
            # Set view parallel to the x-axis
            self.ax.view_init(elev=180, azim=270)
            canvas = self.ui.plotArea.layout().itemAt(1).widget()  
            canvas.draw()
            
        elif view == 'rear':
            # Set view parallel to the x-axis
            self.ax.view_init(elev=-90, azim=90)
            canvas = self.ui.plotArea.layout().itemAt(1).widget()
            canvas.draw()
              
    def show_coord_error_dialog(self):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Error")
        error_box.setText("Error with coordinates. Please check all values are present and are numeric")
        error_box.setStandardButtons(QMessageBox.Ok)
        error_box.exec_()