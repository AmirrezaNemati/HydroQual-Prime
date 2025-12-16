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


class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(586, 570)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        about.setWindowIcon(icon)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(about)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(about)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(about)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/images/logo.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(about)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.about_textBrowser = QtWidgets.QTextBrowser(about)
        self.about_textBrowser.setObjectName("about_textBrowser")
        self.verticalLayout.addWidget(self.about_textBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.about_persian_pushButton = QtWidgets.QPushButton(about)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_persian_pushButton.sizePolicy().hasHeightForWidth())
        self.about_persian_pushButton.setSizePolicy(sizePolicy)
        self.about_persian_pushButton.setObjectName("about_persian_pushButton")
        self.horizontalLayout_2.addWidget(self.about_persian_pushButton)
        self.about_english_pushButton = QtWidgets.QPushButton(about)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_english_pushButton.sizePolicy().hasHeightForWidth())
        self.about_english_pushButton.setSizePolicy(sizePolicy)
        self.about_english_pushButton.setObjectName("about_english_pushButton")
        self.horizontalLayout_2.addWidget(self.about_english_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "About"))
        self.about_textBrowser.setHtml(_translate("about", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt; font-weight:600; color:#003366;\">Water Quality Monitoring Software (HydroQual Prime) - Version 1.0.1</span><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt; font-weight:600;\"> </span></h1>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:12pt;\">This software is a tool for precise and comprehensive analysis of water quality in various applications including drinking, agriculture, and industry. </span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt; font-weight:600; color:#003366;\">Key Features</span><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt; font-weight:600;\"> </span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt;\" style=\" margin-top:12px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-size:16px; font-weight:600;\">Quality Index-Based Assessment</span><span style=\" font-size:16px;\">: Utilizing the latest scientific research, this software calculates water quality indices and accurately evaluates and reports its status. </span></li>\n"
"<li style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt;\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-size:16px; font-weight:600;\">Comprehensive Graphical Analysis</span><span style=\" font-size:16px;\">: By drawing 10 practical charts, the software helps you gain deep insights into water quality quickly and intuitively. </span></li>\n"
"<li style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt;\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-size:16px; font-weight:600;\">Detailed Statistical Summary</span><span style=\" font-size:16px;\">: The software provides comprehensive descriptive statistics, offering key information about water quality data. </span></li>\n"
"<li style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-size:16px; font-weight:600;\">Validation of Tests</span><span style=\" font-size:16px;\">: By calculating the charge balance error, the software helps you ensure the accuracy of laboratory results. </span></li></ul>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt; font-weight:600; color:#003366;\">Developer Information</span><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt; font-weight:600;\"> </span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:12pt;\">Developer: Amirreza Nemati Mansour</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:12pt;\">Organization: Water Research Institute – Ministry of Energy </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:12pt;\">Contact Number: +98-21-77000300 </span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt; font-weight:600; color:#003366;\">License</span><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:8pt; font-weight:600;\"> </span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:180%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:12pt;\">© 2024 Water Research Institute. All rights reserved.</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))
        self.about_persian_pushButton.setText(_translate("about", "فارسی"))
        self.about_english_pushButton.setText(_translate("about", "English"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about = QtWidgets.QWidget()
    ui = Ui_about()
    ui.setupUi(about)
    about.show()
    sys.exit(app.exec_())
