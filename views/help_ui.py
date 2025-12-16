
# """

# ----------------------------------------
# Water Quality Monitoring Software  
# (HydroQual Prime) - Version 1.0.1  
# ----------------------------------------

# Developed by: Amirreza Nemati Mansour  
# Specialized in: Python, Qt, and Water Engineering Applications  
# Contact: amirreza.nemati@ut.ac.ir(mailto:amirreza.nemati@ut.ac.ir)  

# This software is designed to analyze water quality data efficiently and accurately.  
# It features advanced statistical analysis, interactive visualization tools, and an intuitive UI  
# for a seamless user experience in water quality assessment.  

# © 2025 Amirreza Nemati Mansour. All rights reserved.  

# """


# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_help(object):
#     def setupUi(self, help):
#         help.setObjectName("help")
#         help.resize(539, 548)
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap("resources/images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         help.setWindowIcon(icon)
#         self.gridLayout = QtWidgets.QGridLayout(help)
#         self.gridLayout.setObjectName("gridLayout")
#         self.textBrowser = QtWidgets.QTextBrowser(help)
#         self.textBrowser.setObjectName("textBrowser")
        
#         # --- CHANGE START ---
#         # یک فونت پایه برای ویجت تنظیم می‌کنیم. این کار به قابلیت زوم داخلی
#         # اجازه می‌دهد که به درستی با بزرگنمایی این فونت پایه، کار کند.
#         # می‌توانید اندازه اولیه را به دلخواه تغییر دهید.
#         base_font = QtGui.QFont()
#         base_font.setPointSize(10)
#         self.textBrowser.setFont(base_font)
#         # --- CHANGE END ---
        
#         self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

#         self.retranslateUi(help)
#         QtCore.QMetaObject.connectSlotsByName(help)

#     def retranslateUi(self, help):
#         _translate = QtCore.QCoreApplication.translate
#         help.setWindowTitle(_translate("help", "Help (Ctrl+Scroll to Zoom)"))
        
#         # --- CHANGE START ---
#         # تمام مقادیر 'font-size' از کد HTML حذف شده‌اند تا به ویجت QTextBrowser
#         # اجازه داده شود اندازه کل متن را به صورت پویا کنترل کند.
#         # ---
#         self.textBrowser.setHtml(_translate("help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-weight:400; font-style:normal;\">\n"
# "<h2 align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\'; font-weight:600;\">Parameters and Their Units</span></h2>\n"
# "<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:37px; margin-right:37px; border-collapse:collapse;\" align=\"center\" cellspacing=\"2\" cellpadding=\"0\">\n"
# "<tr>\n"
# "<td bgcolor=\"#f2f2f2\" style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\'; font-weight:600; background-color:#f2f2f2;\">Parameter</span></p></td>\n"
# "<td bgcolor=\"#f2f2f2\" style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\'; font-weight:600; background-color:#f2f2f2;\">Unit</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">EC (Electrical Conductivity)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Microsiemens per centimeter (µS/cm)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">TDS (Total Dissolved Solids)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">pH</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Unitless (logarithmic scale)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Ca (Calcium)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Mg (Magnesium)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Na (Sodium)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">K (Potassium)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">HCO₃ (Bicarbonate)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">CO₃ (Carbonate)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Cl (Chloride)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">SO₄ (Sulfate)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">DO (Dissolved Oxygen)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">BOD (Biochemical Oxygen Demand)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">TEMP (Temperature)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Degrees Celsius (°C)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">TRAN (Transparency)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Centimeters (cm)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">TON (Total Organic Nitrogen)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">MRP (Molybdate Reactive Phosphorus)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">DIN (Dissolved Inorganic Nitrogen)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">NO₃ (Nitrate)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">As (Arsenic)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Micrograms per liter (µg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Hg (Mercury)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Micrograms per liter (µg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Pb (Lead)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Micrograms per liter (µg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Cd (Cadmium)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Micrograms per liter (µg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Ni (Nickel)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Micrograms per liter (µg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">NH₄ (Ammonium)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Cr (Chromium)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Micrograms per liter (µg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Mn (Manganese)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">PO₄ (Phosphate)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Fe (Iron)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">FC (Fecal Coliform)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">CFU per 100 mL (CFU/100mL)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">TC (Total Coliform)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">CFU per 100 mL (CFU/100mL)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">COD (Chemical Oxygen Demand)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">TSS (Total Suspended Solids)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">TRUB (Turbidity)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Nephelometric Turbidity Units (NTU)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">B (Boron)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Fl (Fluoride)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Al (Aluminum)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Cu (Copper)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr>\n"
# "<tr>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Zn (Zinc)</span></p></td>\n"
# "<td style=\" padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#dddddd; border-right-color:#dddddd; border-bottom-color:#dddddd; border-left-color:#dddddd; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Tahoma\',\'Geneva\',\'Verdana\',\'sans-serif\';\">Milligrams per liter (mg/L)</span></p></td></tr></table></body></html>"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     help = QtWidgets.QWidget()
#     ui = Ui_help()
#     ui.setupUi(help)
#     help.show()
#     sys.exit(app.exec_())






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


class Ui_help(object):
    def setupUi(self, help):
        help.setObjectName("help")
        help.resize(650, 548) # اندازه پنجره کمی بزرگتر شد تا جدول جدید جا شود
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        help.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(help)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(help)
        self.textBrowser.setObjectName("textBrowser")
        
        base_font = QtGui.QFont()
        base_font.setPointSize(10)
        self.textBrowser.setFont(base_font)
        
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(help)
        QtCore.QMetaObject.connectSlotsByName(help)

    def retranslateUi(self, help):
        _translate = QtCore.QCoreApplication.translate
        help.setWindowTitle(_translate("help", "Help (Ctrl+Scroll to Zoom)"))
        
        # محتوای HTML شامل هر دو جدول
        html_content = """
        <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
        <html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
        p, li { white-space: pre-wrap; }
        </style></head><body style=\" font-family:'MS Shell Dlg 2'; font-weight:400; font-style:normal;\">
        
        <!-- Table 1: Parameters and Units -->
        <h2 align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI','Tahoma','Geneva','Verdana','sans-serif\'; font-weight:600;\">Parameters and Their Units</span></h2>
        <table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; border-collapse:collapse;\" align=\"center\" cellspacing=\"2\" cellpadding=\"0\">
        <!-- ... ردیف های جدول اول ... -->
        <tr>
        <td bgcolor=\"#f2f2f2\" style=\" padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span style=\" font-family:'Segoe UI'; font-weight:600;\">Parameter</span></p></td>
        <td bgcolor=\"#f2f2f2\" style=\" padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span style=\" font-family:'Segoe UI'; font-weight:600;\">Unit</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>EC (Electrical Conductivity)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Microsiemens per centimeter (µS/cm)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>TDS (Total Dissolved Solids)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>pH</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Unitless (logarithmic scale)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Ca (Calcium)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Mg (Magnesium)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Na (Sodium)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>K (Potassium)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>HCO₃ (Bicarbonate)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>CO₃ (Carbonate)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Cl (Chloride)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>SO₄ (Sulfate)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>DO (Dissolved Oxygen)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>BOD (Biochemical Oxygen Demand)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>TEMP (Temperature)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Degrees Celsius (°C)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>TRAN (Transparency)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Centimeters (cm)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>TON (Total Organic Nitrogen)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>MRP (Molybdate Reactive Phosphorus)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>DIN (Dissolved Inorganic Nitrogen)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>NO₃ (Nitrate)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>As (Arsenic)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Micrograms per liter (µg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Hg (Mercury)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Micrograms per liter (µg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Pb (Lead)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Micrograms per liter (µg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Cd (Cadmium)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Micrograms per liter (µg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Ni (Nickel)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Micrograms per liter (µg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>NH₄ (Ammonium)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Cr (Chromium)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Micrograms per liter (µg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Mn (Manganese)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>PO₄ (Phosphate)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Fe (Iron)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>FC (Fecal Coliform)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>CFU per 100 mL (CFU/100mL)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>TC (Total Coliform)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>CFU per 100 mL (CFU/100mL)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>COD (Chemical Oxygen Demand)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>TSS (Total Suspended Solids)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>TRUB (Turbidity)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Nephelometric Turbidity Units (NTU)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>B (Boron)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Fl (Fluoride)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Al (Aluminum)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Cu (Copper)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Zn (Zinc)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Milligrams per liter (mg/L)</span></p></td></tr>
        </table>
        
        <!-- Table 2: Water Quality Indices and Their Applicability -->
        <br>
        <h2 align=\"center\" style=\"margin-top:24px; margin-bottom:12px; font-family:'Segoe UI','Tahoma','Geneva','Verdana','sans-serif'; font-weight:600;\">Water Quality Indices and Their Applicability</h2>
        <p align=\"center\" style=\"margin-top:0px; margin-bottom:12px; font-family:'Segoe UI','Tahoma','Geneva','Verdana','sans-serif';\">The following table indicates the suitability of various water quality indices for assessment in different water use sectors, including drinking, agricultural, and industrial purposes.</p>
        <table border=\"0\" style=\"margin-top:0px; margin-bottom:0px; border-collapse:collapse;\" align=\"center\" cellspacing=\"2\" cellpadding=\"0\">
            <thead>
                <tr>
                    <td bgcolor=\"#f2f2f2\" style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span style=\"font-family:'Segoe UI'; font-weight:600;\">Index Full Name</span></p></td>
                    <td bgcolor=\"#f2f2f2\" style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span style=\"font-family:'Segoe UI'; font-weight:600;\">Drinking Water Use</span></p></td>
                    <td bgcolor=\"#f2f2f2\" style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span style=\"font-family:'Segoe UI'; font-weight:600;\">Agricultural Use</span></p></td>
                    <td bgcolor=\"#f2f2f2\" style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span style=\"font-family:'Segoe UI'; font-weight:600;\">Industrial Use</span></p></td>
                </tr>
            </thead>
            <tbody>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>British Columbia Water Quality Index (BCWQI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Sometimes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Sometimes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Drinking Water Quality Index (DWQI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>No</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>No</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Groundwater Quality Index (GQI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Irish Water Quality Index (IWQI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Sometimes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Iran Water Quality Index (IranWQI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Canadian Water Quality Index (CWQI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Liou Pollution Index (LPI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>No</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>No</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Langelier Saturation Index (LSI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>No</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>No</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Heavy Metal Pollution Index (HMPI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>No</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Sometimes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>National Sanitation Foundation Water Quality Index (NSFWQI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Organ Index (OI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>No</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>No</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Sometimes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>PoS Index (PI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>No</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Weighted Arithmetic Water Quality Index (WAWQI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Sometimes</span></p></td></tr>
                <tr><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Water Quality Index (WQI)</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td><td style=\"padding:8px; border:1px solid #dddddd;\"><p align=\"center\" style=\"margin:0;\"><span>Yes</span></p></td></tr>
            </tbody>
        </table>

        </body></html>
        """
        self.textBrowser.setHtml(_translate("help", html_content))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help = QtWidgets.QWidget()
    ui = Ui_help()
    ui.setupUi(help)
    help.show()
    sys.exit(app.exec_())
