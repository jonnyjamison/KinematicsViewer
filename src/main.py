import sys
from PyQt5.QtWidgets import QApplication
from ui.kinnematics_viewer_ui import KinematicsViewer

def main():
    app = QApplication(sys.argv)
    window = KinematicsViewer()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()