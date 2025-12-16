"""

----------------------------------------
Water Quality Monitoring Software  
(HydroQual Prime) - Version 1.0.1  
----------------------------------------

Developed by: Amirreza Nemati Mansour  
Specialized in: Python, Qt, and Water Engineering Applications  
Contact: amirreza.nemati@ut.ac.ir(mailto:amirreza.nemati@ut.ac.ir)  

This software is designed to analyze water quality data efficiently and accurately.  
It features advanced statistical analysis, interactive visualization tools, and an intuitive UI  
for a seamless user experience in water quality assessment.  

© 2025 Amirreza Nemati Mansour. All rights reserved.  

"""

from PyQt5 import QtWidgets, QtCore
from views.help_ui import Ui_help

class HelpWindow(QtWidgets.QWidget):
    def __init__(self, mediator):
        super().__init__()
        self.mediator = mediator
        self.mediator.set_help_window(self)

        self.help_ui = Ui_help()
        self.help_ui.setupUi(self)
