# Form implementation generated from reading ui file 'app_manager.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import resources_from_qt_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setWhatsThis("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1920, 1080))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setStyleSheet("font: 12pt \"Calibri\";\n"
"\n"
"\n"
"")
        self.tabWidget.setIconSize(QtCore.QSize(45, 45))
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_table = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_table.setGeometry(QtCore.QRect(10, 60, 901, 881))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.tableWidget_table.setFont(font)
        self.tableWidget_table.setMouseTracking(False)
        self.tableWidget_table.setStyleSheet("font: 25 10pt \"Calibri\";\n"
"selection-background-color: #b0e0e6\n"
"")
        self.tableWidget_table.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.tableWidget_table.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tableWidget_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tableWidget_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_table.setAlternatingRowColors(True)
        self.tableWidget_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_table.setShowGrid(False)
        self.tableWidget_table.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.tableWidget_table.setWordWrap(True)
        self.tableWidget_table.setCornerButtonEnabled(True)
        self.tableWidget_table.setRowCount(0)
        self.tableWidget_table.setColumnCount(7)
        self.tableWidget_table.setObjectName("tableWidget_table")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(6, item)
        self.tableWidget_table.horizontalHeader().setVisible(True)
        self.tableWidget_table.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_table.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_table.horizontalHeader().setHighlightSections(True)
        self.tableWidget_table.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_table.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_table.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_table.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_table.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_table.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget_table.verticalHeader().setStretchLastSection(False)
        self.label_specialist = QtWidgets.QLabel(self.tab)
        self.label_specialist.setGeometry(QtCore.QRect(1720, 0, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_specialist.setFont(font)
        self.label_specialist.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_specialist.setStyleSheet("border-radius: 4px;\n"
"background-color: #b0e0e6;\n"
"color:white")
        self.label_specialist.setText("")
        self.label_specialist.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_specialist.setWordWrap(False)
        self.label_specialist.setObjectName("label_specialist")
        self.textBrowser_email_1 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_email_1.setGeometry(QtCore.QRect(920, 150, 961, 671))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_email_1.setFont(font)
        self.textBrowser_email_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_email_1.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_email_1.setOpenExternalLinks(True)
        self.textBrowser_email_1.setObjectName("textBrowser_email_1")
        self.label_sender = QtWidgets.QLabel(self.tab)
        self.label_sender.setGeometry(QtCore.QRect(920, 50, 961, 31))
        self.label_sender.setStyleSheet("font: 25 16pt \"Microsoft YaHei UI\";\n"
"\n"
"")
        self.label_sender.setText("")
        self.label_sender.setObjectName("label_sender")
        self.label_time_send = QtWidgets.QLabel(self.tab)
        self.label_time_send.setGeometry(QtCore.QRect(960, 10, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_time_send.setFont(font)
        self.label_time_send.setStyleSheet("font: 9pt \"Calibri\";\n"
"border-radius: 4px;\n"
"background-color: #b0e0e6;\n"
"color:white")
        self.label_time_send.setText("")
        self.label_time_send.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_time_send.setObjectName("label_time_send")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(920, 820, 961, 121))
        self.tableWidget.setStyleSheet("selection-background-color: #b0e0e6")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(96)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(400)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.label_attachments = QtWidgets.QLabel(self.tab)
        self.label_attachments.setEnabled(True)
        self.label_attachments.setGeometry(QtCore.QRect(920, 10, 31, 31))
        self.label_attachments.setStyleSheet("image: url(:/images/image/folder.png);")
        self.label_attachments.setText("")
        self.label_attachments.setObjectName("label_attachments")
        self.label_subject = QtWidgets.QLabel(self.tab)
        self.label_subject.setGeometry(QtCore.QRect(920, 90, 961, 21))
        self.label_subject.setStyleSheet("font: 75 12pt \"Tahoma\";")
        self.label_subject.setText("")
        self.label_subject.setObjectName("label_subject")
        self.toolButton_reply = QtWidgets.QToolButton(self.tab)
        self.toolButton_reply.setGeometry(QtCore.QRect(1150, 10, 51, 41))
        self.toolButton_reply.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.toolButton_reply.setStyleSheet("QToolButton { /* all types of tool button */\n"
"    border: 2px solid #b0e0e6;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"    padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 2px solid gray;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(downarrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/image/reply.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_reply.setIcon(icon)
        self.toolButton_reply.setIconSize(QtCore.QSize(45, 45))
        self.toolButton_reply.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.toolButton_reply.setObjectName("toolButton_reply")
        self.toolButton_accept = QtWidgets.QToolButton(self.tab)
        self.toolButton_accept.setGeometry(QtCore.QRect(70, 10, 101, 41))
        self.toolButton_accept.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.toolButton_accept.setToolTip("")
        self.toolButton_accept.setStatusTip("")
        self.toolButton_accept.setWhatsThis("")
        self.toolButton_accept.setStyleSheet("QToolButton { /* all types of tool button */\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    border: 2px solid #98f08b;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"    padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 2px solid gray;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(downarrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/image/add_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_accept.setIcon(icon1)
        self.toolButton_accept.setIconSize(QtCore.QSize(45, 45))
        self.toolButton_accept.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_accept.setObjectName("toolButton_accept")
        self.toolButton_refresh = QtWidgets.QToolButton(self.tab)
        self.toolButton_refresh.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.toolButton_refresh.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.toolButton_refresh.setStyleSheet("QToolButton { /* all types of tool button */\n"
"    border: 2px solid #b0e0e6;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"    padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 2px solid gray;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(downarrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/image/refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_refresh.setIcon(icon2)
        self.toolButton_refresh.setIconSize(QtCore.QSize(45, 45))
        self.toolButton_refresh.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.toolButton_refresh.setObjectName("toolButton_refresh")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(920, 120, 41, 21))
        self.label.setStyleSheet("font: 25 8pt \"Calibri\";")
        self.label.setObjectName("label")
        self.label_copy = QtWidgets.QLabel(self.tab)
        self.label_copy.setGeometry(QtCore.QRect(960, 120, 921, 21))
        self.label_copy.setStyleSheet("font: 25 8pt \"Microsoft JhengHei Light\";")
        self.label_copy.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_copy.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_copy.setMidLineWidth(0)
        self.label_copy.setText("")
        self.label_copy.setScaledContents(False)
        self.label_copy.setWordWrap(False)
        self.label_copy.setObjectName("label_copy")
        self.label_statusneworder = QtWidgets.QLabel(self.tab)
        self.label_statusneworder.setGeometry(QtCore.QRect(310, 20, 301, 21))
        self.label_statusneworder.setStyleSheet("font: 75 9pt \"Calibri\";\n"
"")
        self.label_statusneworder.setText("")
        self.label_statusneworder.setObjectName("label_statusneworder")
        self.radioButton_all = QtWidgets.QRadioButton(self.tab)
        self.radioButton_all.setGeometry(QtCore.QRect(630, 16, 82, 31))
        self.radioButton_all.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.radioButton_all.setStyleSheet("font: 9pt \"Calibri\";\n"
"border-radius: 5px;\n"
"background-color: rgb(152, 151, 247);\n"
"color:white")
        self.radioButton_all.setShortcut("")
        self.radioButton_all.setObjectName("radioButton_all")
        self.radioButton_accepted = QtWidgets.QRadioButton(self.tab)
        self.radioButton_accepted.setGeometry(QtCore.QRect(720, 16, 82, 31))
        self.radioButton_accepted.setStyleSheet("font: 9pt \"Calibri\";\n"
"border-radius: 4px;\n"
"background-color:rgb(152, 151, 247);\n"
"color:white")
        self.radioButton_accepted.setObjectName("radioButton_accepted")
        self.radioButton_closed = QtWidgets.QRadioButton(self.tab)
        self.radioButton_closed.setGeometry(QtCore.QRect(810, 16, 82, 31))
        self.radioButton_closed.setStyleSheet("font: 9pt \"Calibri\";\n"
"border-radius: 4px;\n"
"background-color: rgb(152, 151, 247);\n"
"color:white")
        self.radioButton_closed.setObjectName("radioButton_closed")
        self.toolButton_closeorder = QtWidgets.QToolButton(self.tab)
        self.toolButton_closeorder.setGeometry(QtCore.QRect(180, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.toolButton_closeorder.setFont(font)
        self.toolButton_closeorder.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.toolButton_closeorder.setStyleSheet("QToolButton { /* all types of tool button */\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    border: 2px solid #32CD32;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"    padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 2px solid gray;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(downarrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/image/icons8-close order.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_closeorder.setIcon(icon3)
        self.toolButton_closeorder.setIconSize(QtCore.QSize(45, 45))
        self.toolButton_closeorder.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_closeorder.setObjectName("toolButton_closeorder")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_email_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_email_2.setGeometry(QtCore.QRect(10, 10, 1361, 481))
        self.textBrowser_email_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_email_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_email_2.setOpenExternalLinks(True)
        self.textBrowser_email_2.setObjectName("textBrowser_email_2")
        self.toolButton_Attachments = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_Attachments.setGeometry(QtCore.QRect(710, 490, 81, 81))
        self.toolButton_Attachments.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.toolButton_Attachments.setStyleSheet("QToolButton { /* all types of tool button */\n"
"    border: 2px solid #b0e0e6;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"    padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 2px solid gray;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(downarrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/image/folder.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_Attachments.setIcon(icon4)
        self.toolButton_Attachments.setIconSize(QtCore.QSize(45, 45))
        self.toolButton_Attachments.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_Attachments.setObjectName("toolButton_Attachments")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_order_tblwork = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_order_tblwork.setGeometry(QtCore.QRect(10, 60, 821, 811))
        self.tableWidget_order_tblwork.setStyleSheet("font: 25 10pt \"Calibri\";\n"
"selection-background-color: #b0e0e6")
        self.tableWidget_order_tblwork.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.tableWidget_order_tblwork.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tableWidget_order_tblwork.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_order_tblwork.setShowGrid(False)
        self.tableWidget_order_tblwork.setRowCount(0)
        self.tableWidget_order_tblwork.setObjectName("tableWidget_order_tblwork")
        self.tableWidget_order_tblwork.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order_tblwork.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order_tblwork.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order_tblwork.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order_tblwork.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order_tblwork.setHorizontalHeaderItem(4, item)
        self.tableWidget_order_tblwork.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_order_tblwork.horizontalHeader().setDefaultSectionSize(159)
        self.tableWidget_order_tblwork.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_order_tblwork.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_order_tblwork.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget_order_tblwork.verticalHeader().setStretchLastSection(False)
        self.tableWidget_order_tbldone = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_order_tbldone.setGeometry(QtCore.QRect(850, 60, 821, 811))
        self.tableWidget_order_tbldone.setStyleSheet("font: 25 10pt \"Calibri\";\n"
"selection-background-color: #b0e0e6")
        self.tableWidget_order_tbldone.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.tableWidget_order_tbldone.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tableWidget_order_tbldone.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_order_tbldone.setShowGrid(False)
        self.tableWidget_order_tbldone.setRowCount(0)
        self.tableWidget_order_tbldone.setObjectName("tableWidget_order_tbldone")
        self.tableWidget_order_tbldone.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order_tbldone.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order_tbldone.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order_tbldone.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order_tbldone.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order_tbldone.setHorizontalHeaderItem(4, item)
        self.tableWidget_order_tbldone.horizontalHeader().setDefaultSectionSize(159)
        self.tableWidget_order_tbldone.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_order_tbldone.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_order_tbldone.verticalHeader().setSortIndicatorShown(True)
        self.label_inwork = QtWidgets.QLabel(self.tab_3)
        self.label_inwork.setGeometry(QtCore.QRect(360, 10, 111, 31))
        self.label_inwork.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_inwork.setStyleSheet("background-color:  #b0e0e6;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_inwork.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_inwork.setObjectName("label_inwork")
        self.label_done = QtWidgets.QLabel(self.tab_3)
        self.label_done.setGeometry(QtCore.QRect(1190, 10, 111, 31))
        self.label_done.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_done.setStyleSheet("background-color:  #b0e0e6;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_done.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_done.setObjectName("label_done")
        self.label_orderinwork = QtWidgets.QLabel(self.tab_3)
        self.label_orderinwork.setGeometry(QtCore.QRect(1680, 30, 151, 41))
        self.label_orderinwork.setStyleSheet("border-radius: 4px;\n"
"background-color: rgb(152, 151, 247);")
        self.label_orderinwork.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_orderinwork.setObjectName("label_orderinwork")
        self.label_orderinworkcount = QtWidgets.QLabel(self.tab_3)
        self.label_orderinworkcount.setGeometry(QtCore.QRect(1840, 30, 61, 41))
        self.label_orderinworkcount.setStyleSheet("border-radius: 4px;\n"
"background-color: rgb(152, 151, 247);")
        self.label_orderinworkcount.setText("")
        self.label_orderinworkcount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_orderinworkcount.setObjectName("label_orderinworkcount")
        self.label_orderdone = QtWidgets.QLabel(self.tab_3)
        self.label_orderdone.setGeometry(QtCore.QRect(1680, 80, 151, 41))
        self.label_orderdone.setStyleSheet("border-radius: 4px;\n"
"background-color: rgb(152, 151, 247);")
        self.label_orderdone.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_orderdone.setObjectName("label_orderdone")
        self.label_orderindonecount = QtWidgets.QLabel(self.tab_3)
        self.label_orderindonecount.setGeometry(QtCore.QRect(1840, 80, 61, 41))
        self.label_orderindonecount.setStyleSheet("border-radius: 4px;\n"
"background-color: rgb(152, 151, 247);")
        self.label_orderindonecount.setText("")
        self.label_orderindonecount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_orderindonecount.setObjectName("label_orderindonecount")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.action_Settings = QtGui.QAction(MainWindow)
        self.action_Settings.setObjectName("action_Settings")
        self.action_newspecialict = QtGui.QAction(MainWindow)
        self.action_newspecialict.setObjectName("action_newspecialict")
        self.menuFile.addAction(self.action_Settings)
        self.menuFile.addAction(self.action_newspecialict)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.label_specialist.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop.AlignHCenter)
        self.tableWidget.setShowGrid(False)

        self.tableWidget.setColumnWidth(0, 190)
        self.tableWidget.setColumnHidden(1, True)
        # self.tableWidget_table.setColumnHidden(0, True)

        self.label_attachments.setVisible(False)

        self.label_copy.setVisible(False)
        self.label.setVisible(False)
        self.tableWidget_table.resizeColumnToContents(0)



        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget_table.setSortingEnabled(False)
        item = self.tableWidget_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тема"))
        item = self.tableWidget_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Автор"))
        item = self.tableWidget_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Отправитель"))
        item = self.tableWidget_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Копия"))
        item = self.tableWidget_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Дата создания"))
        item = self.tableWidget_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Вложение"))
        self.textBrowser_email_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Вложение"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ссылка"))
        self.toolButton_reply.setText(_translate("MainWindow", "Ответить"))
        self.toolButton_accept.setText(_translate("MainWindow", "Принять"))
        self.toolButton_refresh.setText(_translate("MainWindow", "Ответить"))
        self.label.setText(_translate("MainWindow", "Копия :"))
        self.radioButton_all.setText(_translate("MainWindow", "Все заявки"))
        self.radioButton_accepted.setText(_translate("MainWindow", "Принятые"))
        self.radioButton_closed.setText(_translate("MainWindow", "Закрытые"))
        self.toolButton_closeorder.setText(_translate("MainWindow", "Закрыть"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Table"))
        self.textBrowser_email_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.toolButton_Attachments.setText(_translate("MainWindow", "Вложение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Email"))
        self.tableWidget_order_tblwork.setSortingEnabled(True)
        item = self.tableWidget_order_tblwork.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_order_tblwork.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тема"))
        item = self.tableWidget_order_tblwork.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Автор"))
        item = self.tableWidget_order_tblwork.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Принято"))
        item = self.tableWidget_order_tblwork.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Специалист"))
        self.tableWidget_order_tbldone.setSortingEnabled(True)
        item = self.tableWidget_order_tbldone.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_order_tbldone.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тема"))
        item = self.tableWidget_order_tbldone.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Автор"))
        item = self.tableWidget_order_tbldone.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Выполнено"))
        item = self.tableWidget_order_tbldone.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Специалист"))
        self.label_inwork.setText(_translate("MainWindow", "В РАБОТЕ"))
        self.label_done.setText(_translate("MainWindow", "ВЫПОЛНЕНО"))
        self.label_orderinwork.setText(_translate("MainWindow", "В РАБОТЕ"))
        self.label_orderdone.setText(_translate("MainWindow", "ВЫПОЛНЕНО"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Order"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_Settings.setText(_translate("MainWindow", "Settings"))
        self.action_newspecialict.setText(_translate("MainWindow", "Завести нового специалиста"))
