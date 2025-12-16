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


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_charge_balance_error_window(object):
    def setupUi(self, charge_balance_error_window):
        charge_balance_error_window.setObjectName("charge_balance_error_window")
        charge_balance_error_window.resize(330, 537)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        charge_balance_error_window.setWindowIcon(icon)
        self.ChargeBalanceError_tableWidget = QtWidgets.QTableWidget(charge_balance_error_window)
        self.ChargeBalanceError_tableWidget.setGeometry(QtCore.QRect(0, -1, 331, 538))
        self.ChargeBalanceError_tableWidget.setObjectName("ChargeBalanceError_tableWidget")
        self.ChargeBalanceError_tableWidget.setColumnCount(0)
        self.ChargeBalanceError_tableWidget.setRowCount(0)

        self.retranslateUi(charge_balance_error_window)
        QtCore.QMetaObject.connectSlotsByName(charge_balance_error_window)

    def retranslateUi(self, charge_balance_error_window):
        _translate = QtCore.QCoreApplication.translate
        charge_balance_error_window.setWindowTitle(_translate("charge_balance_error_window", "Charge Balance Error"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    charge_balance_error_window = QtWidgets.QWidget()
    ui = Ui_charge_balance_error_window()
    ui.setupUi(charge_balance_error_window)
    charge_balance_error_window.show()
    sys.exit(app.exec_())
