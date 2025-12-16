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

from PyQt5.QtCore import Qt, QEvent
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from views.about_ui import Ui_about


class AboutWindow(QtWidgets.QWidget):
    def __init__(self, mediator):
        super().__init__()
        
        self.mediator = mediator
        self.mediator.set_about_window(self)

        self.about_ui = Ui_about()
        self.about_ui.setupUi(self)

        # --- START: New Definitive Zoom Implementation ---

        # 1. Set an initial base font size for the entire document.
        # This will be the reference for our relative 'em' units in CSS.
        default_font = self.about_ui.about_textBrowser.font()
        default_font.setPointSize(12) # Set a comfortable starting size (e.g., 12pt)
        self.about_ui.about_textBrowser.document().setDefaultFont(default_font)

        # 2. Install the event filter to capture Ctrl+Scroll.
        self.about_ui.about_textBrowser.installEventFilter(self)
        
        # --- END: New Definitive Zoom Implementation ---

        self.event_about_window()
        # Set default text on startup
        self.set_english_text()

    def eventFilter(self, obj, event):
        """
        This event filter manually changes the document's base font size,
        which provides a robust and reliable zoom for all elements.
        """
        if obj is self.about_ui.about_textBrowser and event.type() == QEvent.Type.Wheel:
            if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
                # Get the document's current default font
                font = obj.document().defaultFont()
                current_size = font.pointSize()
                
                delta = event.angleDelta().y()
                if delta > 0:
                    # Increase font size on zoom in
                    font.setPointSize(current_size + 1)
                else:
                    # Decrease font size on zoom out (with a minimum size limit)
                    if current_size > 6:
                        font.setPointSize(current_size - 1)
                
                # Apply the new font size as the base for the entire document
                obj.document().setDefaultFont(font)
                
                return True # Event handled
        
        return super().eventFilter(obj, event)

    def event_about_window(self):
        self.about_ui.about_persian_pushButton.clicked.connect(self.set_farsi_text)
        self.about_ui.about_english_pushButton.clicked.connect(self.set_english_text)

    def set_english_text(self):
        # --- MODIFIED: Font sizes now use relative 'em' units ---
        # --- FIXED: Full English text is now included ---
        about_text = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    line-height: 1.8;
                    font-size: 1em; /* 1em means 100% of the base font size */
                }
                h1, h2 {
                    color: #003366;
                    font-weight: bold;
                }
                h1 {
                    font-size: 1.5em; /* 150% of the base font size */
                }
                h2 {
                    font-size: 1.25em; /* 125% of the base font size */
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                }
                ul li::before {
                    content: "• ";
                    color: black;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1>Water Quality Monitoring Software (HydroQual Prime) - Version 1.0.2</h1>
            <p>This software is a tool for precise and comprehensive analysis of water quality in various applications including drinking, agriculture, and industry.</p>
        
            <h2>Key Features</h2>
            <ul>
                <li><strong>Quality Index-Based Assessment</strong>: Utilizing the latest scientific research, this software calculates water quality indices and accurately evaluates and reports its status.</li>
                <li><strong>Comprehensive Graphical Analysis</strong>: By drawing 10 practical charts, the software helps you gain deep insights into water quality quickly and intuitively.</li>
                <li><strong>Detailed Statistical Summary</strong>: The software provides comprehensive descriptive statistics, offering key information about water quality data.</li>
                <li><strong>Validation of Tests</strong>: By calculating the charge balance error, the software helps you ensure the accuracy of laboratory results.</li>
            </ul>
        
            <h2>Developer Information</h2>
            <p>Developer: Amirreza Nemati Mansour</p>
            <p>Organization: Water Research Institute – Ministry of Energy</p>
            <p>Contact Number: +98-21-77000300</p>
        
            <h2>License</h2>
            <p>&copy; 2025 Water Research Institute. All rights reserved.</p>
        </body>
        </html>
        """
        self.about_ui.about_textBrowser.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.about_ui.about_textBrowser.setHtml(about_text)

    def set_farsi_text(self):
        # --- MODIFIED: Font sizes now use relative 'em' units ---
        about_text = """
        <!DOCTYPE html>
        <html lang="fa">
        <head>
            <meta charset="UTF-8">
            <style>
                body {
                    font-family: 'Tahoma', sans-serif;
                    line-height: 1.8;
                    font-size: 1em; /* 1em means 100% of the base font size */
                }
                h1, h2 {
                    color: #003366;
                    font-weight: bold;
                }
                h1 {
                    font-size: 1.5em; /* 150% of the base font size */
                }
                h2 {
                    font-size: 1.25em; /* 125% of the base font size */
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                }
                ul li::before {
                    content: "• ";
                    color: black;
                    font-weight: bold;
                }
            </style>
        </head>
        <body dir="rtl">
            <h1>نرم‌افزار پایش کیفیت آب (HydroQual Prime) - نسخه 1.0.2</h1>
            <p>این نرم‌افزار، ابزاری برای تحلیل دقیق و جامع کیفیت آب در کاربردهای مختلف از جمله شرب، کشاورزی و صنعت است.</p>
        
            <h2>ویژگی‌های کلیدی</h2>
            <ul>
                <li><strong>ارزیابی مبتنی بر شاخص‌های کیفی</strong>: با بهره‌گیری از آخرین تحقیقات علمی، این نرم‌افزار شاخص‌های کیفی آب را محاسبه کرده و وضعیت آن را به طور دقیق ارزیابی و گزارش می‌کند.</li>
                <li><strong>تحلیل گرافیکی جامع</strong>: با رسم ۱۰ نمودار کاربردی، نرم‌افزار به شما کمک می‌کند تا به طور شهودی و سریع به بینش‌های عمیقی درباره کیفیت آب دست پیدا کنید.</li>
                <li><strong>خلاصه آماری دقیق</strong>: نرم‌افزار با ارائه آمار توصیفی جامع، اطلاعات کلیدی درباره داده‌های کیفیت آب را در اختیار شما قرار می‌دهد.</li>
                <li><strong>بررسی صحت آزمایش‌ها</strong>: با محاسبه خطای تعادل بار، نرم‌افزار به شما کمک می‌کند تا از صحت نتایج آزمایشگاهی اطمینان حاصل کنید.</li>
            </ul>
        
            <h2>اطلاعات توسعه‌دهنده</h2>
            <p>توسعه‌دهنده: امیررضا نعمتی منصور</p>
            <p>سازمان: موسسه تحقیقات آب – وزارت نیرو</p>
            <p>شماره تماس: ۷۷۰۰۰۳۰۰(۰۲۱)</p>
        
            <h2>مجوز</h2>
            <p>&copy; ۲۰۲۵ موسسه تحقیقات آب. تمام حقوق محفوظ است.</p>
        </body>
        </html>
        """
        self.about_ui.about_textBrowser.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.about_ui.about_textBrowser.setHtml(about_text)