from PyQt5.QtWidgets import QToolBar  # Import QToolBar from PyQt5.QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class PlottingFeatures:
    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()

    def setup_connections(self):
        self.ui.plotButton.clicked.connect(self.handle_plot_button_click)

    def handle_plot_button_click(self):
        upper_wishbone_values = self.get_upper_wishbone_values()
        self.plot_upper_wishbone(upper_wishbone_values)

    def get_upper_wishbone_values(self):
        upper_wishbone_values = []
        for column in range(self.ui.frontInput.columnCount()):
            item = self.ui.frontInput.item(0, column)
            if item is not None:
                upper_wishbone_values.append(float(item.text()))  # Convert to float
            else:
                upper_wishbone_values.append(None)
        return upper_wishbone_values

    def plot_upper_wishbone(self, values):
        x_values = values[::3]
        y_values = values[1::3]
        z_values = values[2::3]

        # Create a Matplotlib figure and canvas
        fig = Figure()
        canvas = FigureCanvas(fig)

        # Add a 3D subplot to the figure
        ax = fig.add_subplot(111, projection='3d')

        # Plot the upper wishbone coordinates
        ax.scatter(x_values, y_values, z_values, c='r', marker='o')

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

