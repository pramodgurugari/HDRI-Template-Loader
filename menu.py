import nuke
import nukescripts
from PySide2 import QtWidgets, QtCore, QtGui
import os

class HDRITemplateLoader(QtWidgets.QDialog):
    def __init__(self):
        super(HDRITemplateLoader, self).__init__()
        self.setWindowTitle("HDRI TEMPLATE LOADER - PramodG")
        self.setMinimumSize(300, 150)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # Colorful Label
        title_label = QtWidgets.QLabel("HDRI TEMPLATE LOADER")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                    stop:0 red, stop:0.5 orange, stop:1 purple);
            }
        """)
        layout.addWidget(title_label)

        # Load Button
        load_btn = QtWidgets.QPushButton("Load HDRI Template")
        load_btn.setStyleSheet("background-color: #5FB878; color: white; font-size: 14px; padding: 8px;")
        load_btn.clicked.connect(self.load_hdri_template)
        layout.addWidget(load_btn)

        # Credits Label
        credit = QtWidgets.QLabel("Created by PramodG")
        credit.setAlignment(QtCore.Qt.AlignCenter)
        credit.setStyleSheet("color: #999; font-size: 12px;")
        layout.addWidget(credit)

        # Links
        links = QtWidgets.QLabel('<a href="https://www.artstation.com/pramod_pro">ArtStation</a> | <a href="https://www.linkedin.com/in/pramod-g-38064a53/">LinkedIn</a>')
        links.setAlignment(QtCore.Qt.AlignCenter)
        links.setOpenExternalLinks(True)
        layout.addWidget(links)

    def load_hdri_template(self):
        file_path = os.path.expanduser("~/.nuke/HDRI_Template.nk")
        if os.path.exists(file_path):
            nuke.nodePaste(file_path)
            nuke.message("HDRI Template Loaded Successfully!")
        else:
            nuke.message("File not found:\n" + file_path)

# Function to launch the panel
def launch_hdri_loader():
    global hdri_loader_dialog
    try:
        hdri_loader_dialog.close()
    except:
        pass
    hdri_loader_dialog = HDRITemplateLoader()
    hdri_loader_dialog.show()

# Add to Nuke menu
nuke.menu("Nuke").addCommand("ProTools/HDRI TEMPLATE LOADER", launch_hdri_loader)
