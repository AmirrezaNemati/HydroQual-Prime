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


class Ui_draw_diagram_window(object):
    def setupUi(self, draw_diagram_window):
        draw_diagram_window.setObjectName("draw_diagram_window")
        draw_diagram_window.resize(774, 643)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(draw_diagram_window.sizePolicy().hasHeightForWidth())
        draw_diagram_window.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        draw_diagram_window.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(draw_diagram_window)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(draw_diagram_window)
        self.frame.setMinimumSize(QtCore.QSize(181, 181))
        self.frame.setMaximumSize(QtCore.QSize(181, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.chadha_label = QtWidgets.QLabel(self.frame)
        self.chadha_label.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.chadha_label.setText("")
        self.chadha_label.setPixmap(QtGui.QPixmap("resources/images/chadha.png"))
        self.chadha_label.setScaledContents(True)
        self.chadha_label.setObjectName("chadha_label")
        self.chadha_pushButton = QtWidgets.QPushButton(self.frame)
        self.chadha_pushButton.setGeometry(QtCore.QRect(0, 0, 181, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.chadha_pushButton.setFont(font)
        self.chadha_pushButton.setAutoFillBackground(False)
        self.chadha_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"    border: none;\n"
"    color: rgba(0, 0, 0, 0.5); /* متن کم‌رنگ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(0, 0, 0, 1); /* متن پررنگ‌تر هنگام کلیک */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: transparent; /* تغییر رنگ هنگام hover (موس روی دکمه) */\n"
"}\n"
"")
        self.chadha_pushButton.setObjectName("chadha_pushButton")
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_10 = QtWidgets.QFrame(draw_diagram_window)
        self.frame_10.setMinimumSize(QtCore.QSize(181, 181))
        self.frame_10.setMaximumSize(QtCore.QSize(181, 181))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.durvo_label = QtWidgets.QLabel(self.frame_10)
        self.durvo_label.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.durvo_label.setText("")
        self.durvo_label.setPixmap(QtGui.QPixmap("resources/images/durvo.png"))
        self.durvo_label.setScaledContents(True)
        self.durvo_label.setObjectName("durvo_label")
        self.durvo_pushButton = QtWidgets.QPushButton(self.frame_10)
        self.durvo_pushButton.setGeometry(QtCore.QRect(0, 0, 181, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.durvo_pushButton.setFont(font)
        self.durvo_pushButton.setAutoFillBackground(False)
        self.durvo_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"    border: none;\n"
"    color: rgba(0, 0, 0, 0.5); /* متن کم‌رنگ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(0, 0, 0, 1); /* متن پررنگ‌تر هنگام کلیک */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: transparent; /* تغییر رنگ هنگام hover (موس روی دکمه) */\n"
"}\n"
"")
        self.durvo_pushButton.setObjectName("durvo_pushButton")
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(draw_diagram_window)
        self.frame_9.setMinimumSize(QtCore.QSize(181, 181))
        self.frame_9.setMaximumSize(QtCore.QSize(181, 181))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gaillardet_label = QtWidgets.QLabel(self.frame_9)
        self.gaillardet_label.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.gaillardet_label.setText("")
        self.gaillardet_label.setPixmap(QtGui.QPixmap("resources/images/gaillardet.png"))
        self.gaillardet_label.setScaledContents(True)
        self.gaillardet_label.setObjectName("gaillardet_label")
        self.gaillardet_pushButton = QtWidgets.QPushButton(self.frame_9)
        self.gaillardet_pushButton.setGeometry(QtCore.QRect(0, 0, 181, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.gaillardet_pushButton.setFont(font)
        self.gaillardet_pushButton.setAutoFillBackground(False)
        self.gaillardet_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"    border: none;\n"
"    color: rgba(0, 0, 0, 0.5); /* متن کم‌رنگ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(0, 0, 0, 1); /* متن پررنگ‌تر هنگام کلیک */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: transparent; /* تغییر رنگ هنگام hover (موس روی دکمه) */\n"
"}\n"
"")
        self.gaillardet_pushButton.setObjectName("gaillardet_pushButton")
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(draw_diagram_window)
        self.frame_8.setMinimumSize(QtCore.QSize(181, 181))
        self.frame_8.setMaximumSize(QtCore.QSize(181, 181))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gibbs_label = QtWidgets.QLabel(self.frame_8)
        self.gibbs_label.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.gibbs_label.setText("")
        self.gibbs_label.setPixmap(QtGui.QPixmap("resources/images/gibbs.png"))
        self.gibbs_label.setScaledContents(True)
        self.gibbs_label.setObjectName("gibbs_label")
        self.gibbs_pushButton = QtWidgets.QPushButton(self.frame_8)
        self.gibbs_pushButton.setGeometry(QtCore.QRect(0, 0, 181, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.gibbs_pushButton.setFont(font)
        self.gibbs_pushButton.setAutoFillBackground(False)
        self.gibbs_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"    border: none;\n"
"    color: rgba(0, 0, 0, 0.5); /* متن کم‌رنگ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(0, 0, 0, 1); /* متن پررنگ‌تر هنگام کلیک */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: transparent; /* تغییر رنگ هنگام hover (موس روی دکمه) */\n"
"}\n"
"")
        self.gibbs_pushButton.setObjectName("gibbs_pushButton")
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(draw_diagram_window)
        self.frame_7.setMinimumSize(QtCore.QSize(181, 181))
        self.frame_7.setMaximumSize(QtCore.QSize(181, 181))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.hfed_label = QtWidgets.QLabel(self.frame_7)
        self.hfed_label.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.hfed_label.setText("")
        self.hfed_label.setPixmap(QtGui.QPixmap("resources/images/hfed.png"))
        self.hfed_label.setScaledContents(True)
        self.hfed_label.setObjectName("hfed_label")
        self.hfed_pushButton = QtWidgets.QPushButton(self.frame_7)
        self.hfed_pushButton.setGeometry(QtCore.QRect(0, 0, 181, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.hfed_pushButton.setFont(font)
        self.hfed_pushButton.setAutoFillBackground(False)
        self.hfed_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"    border: none;\n"
"    color: rgba(0, 0, 0, 0.5); /* متن کم‌رنگ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(0, 0, 0, 1); /* متن پررنگ‌تر هنگام کلیک */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: transparent; /* تغییر رنگ هنگام hover (موس روی دکمه) */\n"
"}\n"
"")
        self.hfed_pushButton.setObjectName("hfed_pushButton")
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(draw_diagram_window)
        self.frame_6.setMinimumSize(QtCore.QSize(181, 181))
        self.frame_6.setMaximumSize(QtCore.QSize(181, 181))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.piper_label = QtWidgets.QLabel(self.frame_6)
        self.piper_label.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.piper_label.setText("")
        self.piper_label.setPixmap(QtGui.QPixmap("resources/images/piper.png"))
        self.piper_label.setScaledContents(True)
        self.piper_label.setObjectName("piper_label")
        self.piper_pushButton = QtWidgets.QPushButton(self.frame_6)
        self.piper_pushButton.setGeometry(QtCore.QRect(0, 0, 181, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.piper_pushButton.setFont(font)
        self.piper_pushButton.setAutoFillBackground(False)
        self.piper_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"    border: none;\n"
"    color: rgba(0, 0, 0, 0.5); /* متن کم‌رنگ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(0, 0, 0, 1); /* متن پررنگ‌تر هنگام کلیک */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: transparent; /* تغییر رنگ هنگام hover (موس روی دکمه) */\n"
"}\n"
"")
        self.piper_pushButton.setObjectName("piper_pushButton")
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(draw_diagram_window)
        self.frame_5.setMinimumSize(QtCore.QSize(181, 181))
        self.frame_5.setMaximumSize(QtCore.QSize(181, 181))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.rectanglePiper_label = QtWidgets.QLabel(self.frame_5)
        self.rectanglePiper_label.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.rectanglePiper_label.setText("")
        self.rectanglePiper_label.setPixmap(QtGui.QPixmap("resources/images/rectangle_piper.png"))
        self.rectanglePiper_label.setScaledContents(True)
        self.rectanglePiper_label.setObjectName("rectanglePiper_label")
        self.rectanglePiper_pushButton = QtWidgets.QPushButton(self.frame_5)
        self.rectanglePiper_pushButton.setGeometry(QtCore.QRect(0, 0, 181, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.rectanglePiper_pushButton.setFont(font)
        self.rectanglePiper_pushButton.setAutoFillBackground(False)
        self.rectanglePiper_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"    border: none;\n"
"    color: rgba(0, 0, 0, 0.5); /* متن کم‌رنگ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(0, 0, 0, 1); /* متن پررنگ‌تر هنگام کلیک */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: transparent; /* تغییر رنگ هنگام hover (موس روی دکمه) */\n"
"}\n"
"")
        self.rectanglePiper_pushButton.setObjectName("rectanglePiper_pushButton")
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(draw_diagram_window)
        self.frame_4.setMinimumSize(QtCore.QSize(181, 181))
        self.frame_4.setMaximumSize(QtCore.QSize(181, 181))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.schoeller_label = QtWidgets.QLabel(self.frame_4)
        self.schoeller_label.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.schoeller_label.setText("")
        self.schoeller_label.setPixmap(QtGui.QPixmap("resources/images/schoeller.png"))
        self.schoeller_label.setScaledContents(True)
        self.schoeller_label.setObjectName("schoeller_label")
        self.schoeller_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.schoeller_pushButton.setGeometry(QtCore.QRect(0, 0, 181, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.schoeller_pushButton.setFont(font)
        self.schoeller_pushButton.setAutoFillBackground(False)
        self.schoeller_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"    border: none;\n"
"    color: rgba(0, 0, 0, 0.5); /* متن کم‌رنگ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(0, 0, 0, 1); /* متن پررنگ‌تر هنگام کلیک */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: transparent; /* تغییر رنگ هنگام hover (موس روی دکمه) */\n"
"}\n"
"")
        self.schoeller_pushButton.setObjectName("schoeller_pushButton")
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(draw_diagram_window)
        self.frame_3.setMinimumSize(QtCore.QSize(181, 181))
        self.frame_3.setMaximumSize(QtCore.QSize(181, 181))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.stiff_label = QtWidgets.QLabel(self.frame_3)
        self.stiff_label.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.stiff_label.setText("")
        self.stiff_label.setPixmap(QtGui.QPixmap("resources/images/stiff.png"))
        self.stiff_label.setScaledContents(True)
        self.stiff_label.setObjectName("stiff_label")
        self.stiff_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.stiff_pushButton.setGeometry(QtCore.QRect(0, 0, 181, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.stiff_pushButton.setFont(font)
        self.stiff_pushButton.setAutoFillBackground(False)
        self.stiff_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"    border: none;\n"
"    color: rgba(0, 0, 0, 0.5); /* متن کم‌رنگ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(0, 0, 0, 1); /* متن پررنگ‌تر هنگام کلیک */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: transparent; /* تغییر رنگ هنگام hover (موس روی دکمه) */\n"
"}\n"
"")
        self.stiff_pushButton.setObjectName("stiff_pushButton")
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(draw_diagram_window)
        self.frame_2.setMinimumSize(QtCore.QSize(181, 181))
        self.frame_2.setMaximumSize(QtCore.QSize(181, 181))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.wilcox_label = QtWidgets.QLabel(self.frame_2)
        self.wilcox_label.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.wilcox_label.setText("")
        self.wilcox_label.setPixmap(QtGui.QPixmap("resources/images/wilcox.jpg"))
        self.wilcox_label.setScaledContents(True)
        self.wilcox_label.setObjectName("wilcox_label")
        self.wilcox_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.wilcox_pushButton.setGeometry(QtCore.QRect(0, 0, 181, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.wilcox_pushButton.setFont(font)
        self.wilcox_pushButton.setAutoFillBackground(False)
        self.wilcox_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"    border: none;\n"
"    color: rgba(0, 0, 0, 0.5); /* متن کم‌رنگ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(0, 0, 0, 1); /* متن پررنگ‌تر هنگام کلیک */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: transparent; /* تغییر رنگ هنگام hover (موس روی دکمه) */\n"
"}\n"
"")
        self.wilcox_pushButton.setObjectName("wilcox_pushButton")
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(draw_diagram_window)
        QtCore.QMetaObject.connectSlotsByName(draw_diagram_window)

    def retranslateUi(self, draw_diagram_window):
        _translate = QtCore.QCoreApplication.translate
        draw_diagram_window.setWindowTitle(_translate("draw_diagram_window", "Draw Diagram"))
        self.chadha_pushButton.setText(_translate("draw_diagram_window", "Chadha"))
        self.durvo_pushButton.setText(_translate("draw_diagram_window", "Durov"))
        self.gaillardet_pushButton.setText(_translate("draw_diagram_window", "Gaillardet"))
        self.gibbs_pushButton.setText(_translate("draw_diagram_window", "Gibbs"))
        self.hfed_pushButton.setText(_translate("draw_diagram_window", "Hfed"))
        self.piper_pushButton.setText(_translate("draw_diagram_window", "Piper"))
        self.rectanglePiper_pushButton.setText(_translate("draw_diagram_window", "rectangle piper"))
        self.schoeller_pushButton.setText(_translate("draw_diagram_window", "Schoeller"))
        self.stiff_pushButton.setText(_translate("draw_diagram_window", "Stiff"))
        self.wilcox_pushButton.setText(_translate("draw_diagram_window", "Wilcox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    draw_diagram_window = QtWidgets.QWidget()
    ui = Ui_draw_diagram_window()
    ui.setupUi(draw_diagram_window)
    draw_diagram_window.show()
    sys.exit(app.exec_())
