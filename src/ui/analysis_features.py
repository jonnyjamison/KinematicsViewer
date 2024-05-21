from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import math
import numpy as np


class AnalysisFeatures:
    """
    A class for plotting analysis of geometry and calculating metrics such as camber, toe, and caster.
    """

    def __init__(self, plotting_features, ui):
        """
        Initialize AnalysisFeatures object.

        Parameters:
            plotting_features (PlottingFeatures): An instance of PlottingFeatures containing data for plotting.
            ui (UIWidget): An instance of UIWidget (KinematicsViewer) for interacting with the user interface.
        """
        self.ui = ui
        #self.ui = plotting_features.ui
        self.ax = plotting_features.ax
        self.kinData_values = plotting_features.kinData_values
        self.setup_connections()
        self.calculate_camber()
        self.calculate_toe()
        self.calculate_caster()
            
    def setup_connections(self):
        """
        Set up connections between UI widget signals and corresponding methods.
        """
        self.ui.checkWheelAxis.stateChanged.connect(self.handle_checkWheelAxis_state_changed)        
        self.ui.checkRollCentre.stateChanged.connect(self.handle_checkRollCentre_state_changed)
        self.ui.checkShowTyres.stateChanged.connect(self.handle_checkShowTyres_state_changed)
       
    def handle_checkWheelAxis_state_changed(self, state):
        """
        Handle the state change of the checkWheelAxis checkbox.

        Parameters:
            state (Qt.CheckState): The new state of the checkbox.
        """   
       # Clear previously plotted lines when button unchecked
        if hasattr(self, 'extended_WheelAxis_lines'):
            for line in self.extended_WheelAxis_lines:
                line.remove()
            del self.extended_WheelAxis_lines
    
        if state == Qt.Checked:
            self.extended_WheelAxis_lines = []
            for axle in ['front', 'rear']:
                # Coordinates of the upper upright pivot
                x_upper = self.get_hardpoint(axle,'upper_upright_pivot')[0]
                y_upper = self.get_hardpoint(axle,'upper_upright_pivot')[1]
                z_upper = self.get_hardpoint(axle,'upper_upright_pivot')[2]
                # Coordinates of the lower upright pivot
                x_lower = self.get_hardpoint(axle,'lower_upright_pivot')[0]
                y_lower = self.get_hardpoint(axle,'lower_upright_pivot')[1]
                z_lower = self.get_hardpoint(axle,'lower_upright_pivot')[2]

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
        """
        Plot the roll centre of the vehicle based on kinematic data when checkbox ticked
        """
        if hasattr(self, 'RollCentre_plot'):
            for plot in self.RollCentre_plot:
                plot.remove()
            del self.RollCentre_plot
        
        if state == Qt.Checked:
            self.RollCentre_plot = []
            
            for axle in ['front', 'rear']:
                # Coordinates of the upper and lower wishbone hardpoints
                upper_leading_pivot = self.get_hardpoint(axle, 'upper_leading_pivot')
                lower_leading_pivot = self.get_hardpoint(axle, 'lower_leading_pivot')
                upper_trailing_pivot = self.get_hardpoint(axle, 'upper_trailling_pivot')
                lower_trailing_pivot = self.get_hardpoint(axle, 'lower_trailling_pivot')
                               
                # Calculate vectors representing the wishbones
                wishbone1_vec = upper_trailing_pivot - upper_leading_pivot[0]  # Vector along the first wishbone
                wishbone2_vec = lower_trailing_pivot - lower_leading_pivot # Vector along the second wishbone
                
                # Calculate the normal vectors to the wishbones
                normal_vec = np.cross(wishbone1_vec, wishbone2_vec)
                
                roll_centre = np.array([0, 0, 0])
                if normal_vec[1] != 0:
                    roll_centre = np.cross(normal_vec, [0, 1, 0])
                    if roll_centre[1] != 0:
                        roll_centre /= roll_centre[1]  # Normalize by y-coordinate to get a point on the y = 0 plane
                    else:
                        roll_centre[1] = 0  # Set y-coordinate to zero if division by zero occurs
                           
                # Plot roll centre if calculated successfully
                if not np.allclose([roll_centre[0], roll_centre[2]], [0, 0]):
                    roll_centre_marker = self.ax.plot(roll_centre[0], roll_centre[1] ,roll_centre[2], marker='*', linewidth=1)[0]
                    self.RollCentre_plot.append(roll_centre_marker)
                else:
                    print("Roll center is at origin [0, 0, 0], indicating an error in calculation, possibly due to parallel wishbones") 
                      
    def handle_checkShowTyres_state_changed(self, state):
        """
        Plot representations of tyres on the vehicle based on 
        kinematic data when checkbox ticked
        """
        if hasattr(self, 'tyre_plots'):
            for plot in self.tyre_plots:
                plot.remove()
            del self.tyre_plots
        
        if state == Qt.Checked:
            self.tyre_plots = []
            
            for axle in ['front', 'rear']:
                upper_upright_pivot = np.array(self.get_hardpoint(axle, 'upper_leading_pivot'))
                lower_upright_pivot = np.array(self.get_hardpoint(axle, 'lower_upright_pivot'))
                                
                # Calculate the midpoint between hardpoints 
                midpoint = (upper_upright_pivot + lower_upright_pivot) / 2

                # Define the diameter of the tyre
                tyre_diameter = upper_upright_pivot[1] + lower_upright_pivot[1]

                # Number of circles to to represent tyre width
                num_circles = 10
                tyre_radius = tyre_diameter / 2
                tyre_width = 0.15

                for x_direction in [1, -1]: # To plot mirrored tyres for other side of vehicle
                    for i in range(num_circles):
                        tyre_x = (midpoint[0] + (i * (tyre_width / num_circles)) * np.ones(100)) * x_direction
                        tyre_z = midpoint[2] + np.cos(np.linspace(0, 2*np.pi, 100)) * tyre_radius
                        tyre_y = midpoint[1] + np.sin(np.linspace(0, 2*np.pi, 100)) * tyre_radius
                        tyre_plot = self.ax.plot(tyre_x, tyre_y, tyre_z)
                        self.tyre_plots.append(tyre_plot)

    def calculate_camber(self):
        """
        Calculate and update the camber angles of the vehicle's wheels.
        """
        for axle in ['front', 'rear']:
            # Coordinates of upright pivot
            upper_upright_pivot = self.get_hardpoint(axle, 'upper_upright_pivot')
            lower_upright_pivot = self.get_hardpoint(axle, 'lower_upright_pivot')

            # Calculate angle in radians
            angle_radians = math.atan2(upper_upright_pivot[1] - lower_upright_pivot[1], upper_upright_pivot[0] - lower_upright_pivot[0])

            # Convert angle from radians to degrees
            angle_degrees = math.degrees(angle_radians)

            # The angle with the y-axis is complementary to the angle with the x-axis
            camber_angle_degrees = 90 - angle_degrees
            
            # Populate tableOutput with camber value
            if axle == 'front':
                self.ui.tableOutput.setItem(0, 0, QTableWidgetItem(str(camber_angle_degrees)[0:6]))
            else:
                self.ui.tableOutput.setItem(0, 1, QTableWidgetItem(str(camber_angle_degrees)[0:6]))
                
    
    def calculate_toe(self):
        """
        Calculate and update the toe angles of the vehicle's wheels.
        """
        for axle in ['front', 'rear']:
            # Coordinates of the upper and lower upright pivot
            upper_upright_pivot = self.get_hardpoint(axle, 'upper_upright_pivot')
            lower_upright_pivot = self.get_hardpoint(axle, 'lower_upright_pivot')

            # Project the vectors onto the xz-plane by setting their y-components to 0
            vec_upper_proj = np.array([upper_upright_pivot[0], 0, upper_upright_pivot[2]]) # x & z
            vec_lower_proj = np.array([lower_upright_pivot[0], 0, lower_upright_pivot[2]]) # x & z

            # Calculate the angle between the projected vectors
            cos_angle = np.dot(vec_upper_proj, vec_lower_proj) / (np.linalg.norm(vec_upper_proj) * np.linalg.norm(vec_lower_proj))
            angle_radians = np.arccos(cos_angle)
            angle_degrees = np.degrees(angle_radians)

            # Update tableOutput
            if axle == 'front':
                self.ui.tableOutput.setItem(1, 0, QTableWidgetItem(str(angle_degrees)[0:6]))
            else:
                self.ui.tableOutput.setItem(1, 1, QTableWidgetItem(str(angle_degrees)[0:6]))
                
                
    def calculate_caster(self):
        """
        Calculate and update the caster angles of the vehicle's wheels.
        """
        for axle in ['front', 'rear']:
            # Coordinates of the upper and lower upright 
            upper_upright_pivot = self.get_hardpoint(axle, 'upper_upright_pivot')
            lower_upright_pivot = self.get_hardpoint(axle, 'lower_upright_pivot')

            # Vector from lower to upper pivot
            vec_pivot = np.array([upper_upright_pivot[0] - lower_upright_pivot[0], 
                                  upper_upright_pivot[1] - lower_upright_pivot[1], 
                                  upper_upright_pivot[2] - lower_upright_pivot[2]])

            # Vector in the vertical direction
            vec_vertical = np.array([0, 1, 0])

            # Calculate the angle between the pivot vector and the vertical
            cos_angle = np.dot(vec_pivot, vec_vertical) / (np.linalg.norm(vec_pivot) * np.linalg.norm(vec_vertical))
            angle_radians = np.arccos(cos_angle)
            angle_degrees = np.degrees(angle_radians)
            angle_string = str(round(angle_degrees, 2)) + "°"

            # Update tableOutput 
            if axle == 'front':
                self.ui.tableOutput.setItem(1, 0, QTableWidgetItem(angle_string))
            else:
                self.ui.tableOutput.setItem(1, 1, QTableWidgetItem(angle_string))
    
    def get_hardpoint(self, axle, location):
        """
        Retrieve the coordinates of a specific hardpoint based on the axle and location.
        Axle is either 'front' or 'rear'
        """
        return self.kinData_values[axle][location]