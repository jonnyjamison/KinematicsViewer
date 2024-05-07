from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import math



class AnalysisFeatures:
    """
    A class for plotting analysis of geomtery and 
    calculating metrics such as camber etc.
    """
    def __init__(self, plotting_features, ui):
        self.ui = ui
        #self.ui = plotting_features.ui
        self.ax = plotting_features.ax
        self.kinData_values = plotting_features.kinData_values
        self.setup_connections()
        self.calculate_camber()
            
        
    def setup_connections(self):
        self.ui.checkWheelAxis.stateChanged.connect(self.handle_checkWheelAxis_state_changed)        
        self.ui.checkRollCentre.stateChanged.connect(self.handle_checkRollCentre_state_changed)
        self.ui.checkSideViewIC.stateChanged.connect(self.handle_checkSideViewIC_state_changed)
       
        
    def handle_checkWheelAxis_state_changed(self, state):   
       # Clear previously plotted lines when button unchecked
        if hasattr(self, 'extended_WheelAxis_lines'):
            for line in self.extended_WheelAxis_lines:
                line.remove()
            del self.extended_WheelAxis_lines
    
        if state == Qt.Checked:
            self.extended_WheelAxis_lines = []
            for position in ['front', 'rear']:
                # Coordinates of the upper upright pivot
                x_upper = self.kinData_values[position]['upper_upright_pivot'][0]
                y_upper = self.kinData_values[position]['upper_upright_pivot'][1]
                z_upper = self.kinData_values[position]['upper_upright_pivot'][2]

                # Coordinates of the lower upright pivot
                x_lower = self.kinData_values[position]['lower_upright_pivot'][0]
                y_lower = self.kinData_values[position]['lower_upright_pivot'][1]
                z_lower = self.kinData_values[position]['lower_upright_pivot'][2]

                # Calculate slope of line between the two points
                slope = (y_upper - y_lower) / (x_upper - x_lower)

                # Calculate the y-intercept of the line
                y_intercept = y_lower - slope * x_lower

                # Calculate x-coordinate where line intersects y-axis at y = 0
                x_intersect_y0 = -y_intercept / slope

                # Extend upper coordinate by 50% to make line protrude past upper joint
                y_desired = y_upper * 1.5

                # Calculate x-coordinate where line intersects 
                x_intersect_desired_y = (y_desired - y_intercept) / slope

                # Extend the line to intersect y = (upper*1.5) and y = 0
                x_line_extended = [x_lower, x_intersect_y0, x_intersect_desired_y]
                y_line_extended = [y_lower, 0, y_desired]
                z_line_extended = [z_lower, z_lower, z_lower]
                
                # Plot extended wheel axis line
                line = self.ax.plot(x_line_extended, y_line_extended, z_line_extended, linestyle='--', linewidth=1, color='red')[0]
                self.extended_WheelAxis_lines.append(line)
                
                # For other side of car (mirror in x axis)
                x_line_extended_mirror = [-x for x in x_line_extended]

                # Plot the mirror image of the extended line
                line_mirrored = self.ax.plot(x_line_extended_mirror, y_line_extended, z_line_extended, linestyle='--', linewidth=1, color='red')[0]
                self.extended_WheelAxis_lines.append(line_mirrored)
                    

    def handle_checkRollCentre_state_changed(self, state):
        if hasattr(self, 'RollCentre_lines'):
            for line in self.RollCentre_lines:
                line.remove()
            del self.RollCentre_lines
        
        if state == Qt.Checked:
            self.RollCentre_lines = []
            for position in ['front', 'rear']:
                print("WIP")
            
        
            
    
    def handle_checkSideViewIC_state_changed(self, state):
        print("WIP")
        
        
    def calculate_camber(self):
        for position in ['front', 'rear']:
            # Coordinates of upright pivot
            x_upper = self.kinData_values[position]['upper_upright_pivot'][0]
            y_upper = self.kinData_values[position]['upper_upright_pivot'][1]
            x_lower = self.kinData_values[position]['lower_upright_pivot'][0]
            y_lower = self.kinData_values[position]['lower_upright_pivot'][1]

            # Calculate the slope
            slope = (y_upper - y_lower) / (x_upper - x_lower)

            # Calculate the angle in radians
            angle_radians = math.atan2(y_upper - y_lower, x_upper - x_lower)

            # Convert angle from radians to degrees
            angle_degrees = math.degrees(angle_radians)

            # The angle with the y-axis is complementary to the angle with the x-axis
            camber = 90 - angle_degrees
            
            # Populate tableOutput with camber value
            if position == 'front':
                self.ui.tableOutput.setItem(0, 0, QTableWidgetItem(str(camber)[0:6]))
            else:
                self.ui.tableOutput.setItem(0, 1, QTableWidgetItem(str(camber)[0:6]))