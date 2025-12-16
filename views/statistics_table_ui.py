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


class Ui_statistics_tabel_window(object):
    def setupUi(self, statistics_tabel_window):
        statistics_tabel_window.setObjectName("statistics_tabel_window")
        statistics_tabel_window.resize(743, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        statistics_tabel_window.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(statistics_tabel_window)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.statistics_tabel_widget = QtWidgets.QTableWidget(statistics_tabel_window)
        self.statistics_tabel_widget.setObjectName("statistics_tabel_widget")
        self.statistics_tabel_widget.setColumnCount(0)
        self.statistics_tabel_widget.setRowCount(0)
        self.verticalLayout.addWidget(self.statistics_tabel_widget)
        self.export_statistics_push_button = QtWidgets.QPushButton(statistics_tabel_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_statistics_push_button.sizePolicy().hasHeightForWidth())
        self.export_statistics_push_button.setSizePolicy(sizePolicy)
        self.export_statistics_push_button.setObjectName("export_statistics_push_button")
        self.verticalLayout.addWidget(self.export_statistics_push_button)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(statistics_tabel_window)
        QtCore.QMetaObject.connectSlotsByName(statistics_tabel_window)

    def retranslateUi(self, statistics_tabel_window):
        _translate = QtCore.QCoreApplication.translate
        statistics_tabel_window.setWindowTitle(_translate("statistics_tabel_window", "Statistics result"))
        self.export_statistics_push_button.setText(_translate("statistics_tabel_window", "Export data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    statistics_tabel_window = QtWidgets.QWidget()
    ui = Ui_statistics_tabel_window()
    ui.setupUi(statistics_tabel_window)
    statistics_tabel_window.show()
    sys.exit(app.exec_())
