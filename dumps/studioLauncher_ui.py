# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/studioLauncher_ui.ui'
#
# Created: Sun Apr 26 21:58:44 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 333)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_shows = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_shows.sizePolicy().hasHeightForWidth())
        self.groupBox_shows.setSizePolicy(sizePolicy)
        self.groupBox_shows.setMinimumSize(QtCore.QSize(160, 0))
        self.groupBox_shows.setMaximumSize(QtCore.QSize(160, 16777215))
        self.groupBox_shows.setObjectName("groupBox_shows")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_shows)
        self.verticalLayout.setContentsMargins(10, 25, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtGui.QListWidget(self.groupBox_shows)
        self.listWidget.setMinimumSize(QtCore.QSize(128, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(128, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.groupBox_shows)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox_applications = QtGui.QGroupBox(self.splitter)
        self.groupBox_applications.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_applications.setObjectName("groupBox_applications")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_applications)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setContentsMargins(1, 25, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_package = QtGui.QLabel(self.groupBox_applications)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_package.sizePolicy().hasHeightForWidth())
        self.label_package.setSizePolicy(sizePolicy)
        self.label_package.setLineWidth(2)
        self.label_package.setText("")
        self.label_package.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_package.setObjectName("label_package")
        self.verticalLayout_2.addWidget(self.label_package)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.button_studioShow = QtGui.QPushButton(self.groupBox_applications)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_studioShow.sizePolicy().hasHeightForWidth())
        self.button_studioShow.setSizePolicy(sizePolicy)
        self.button_studioShow.setText("")
        self.button_studioShow.setDefault(True)
        self.button_studioShow.setFlat(False)
        self.button_studioShow.setObjectName("button_studioShow")
        self.verticalLayout_2.addWidget(self.button_studioShow)
        self.textEdit_output = QtGui.QTextEdit(self.splitter)
        self.textEdit_output.setObjectName("textEdit_output")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 685, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu_file = QtGui.QMenu(self.menuBar)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QtGui.QMenu(self.menuBar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_publish = QtGui.QMenu(self.menuBar)
        self.menu_publish.setObjectName("menu_publish")
        self.menu_help = QtGui.QMenu(self.menuBar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menuBar)
        self.action_removeThumbs = QtGui.QAction(MainWindow)
        self.action_removeThumbs.setObjectName("action_removeThumbs")
        self.action_removePYC = QtGui.QAction(MainWindow)
        self.action_removePYC.setObjectName("action_removePYC")
        self.actionPatch = QtGui.QAction(MainWindow)
        self.actionPatch.setObjectName("actionPatch")
        self.action_minor = QtGui.QAction(MainWindow)
        self.action_minor.setObjectName("action_minor")
        self.action_major = QtGui.QAction(MainWindow)
        self.action_major.setObjectName("action_major")
        self.actionLish = QtGui.QAction(MainWindow)
        self.actionLish.setObjectName("actionLish")
        self.action_aboutApplication = QtGui.QAction(MainWindow)
        self.action_aboutApplication.setObjectName("action_aboutApplication")
        self.action_new = QtGui.QAction(MainWindow)
        self.action_new.setObjectName("action_new")
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_patch = QtGui.QAction(MainWindow)
        self.action_patch.setObjectName("action_patch")
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_exit)
        self.menu_edit.addAction(self.action_removeThumbs)
        self.menu_edit.addAction(self.action_removePYC)
        self.menu_publish.addAction(self.action_patch)
        self.menu_publish.addAction(self.action_minor)
        self.menu_publish.addAction(self.action_major)
        self.menu_help.addAction(self.action_aboutApplication)
        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_edit.menuAction())
        self.menuBar.addAction(self.menu_publish.menuAction())
        self.menuBar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_shows.setTitle(QtGui.QApplication.translate("MainWindow", "Shows", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_applications.setTitle(QtGui.QApplication.translate("MainWindow", "Applications", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_edit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_publish.setTitle(QtGui.QApplication.translate("MainWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_help.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_removeThumbs.setText(QtGui.QApplication.translate("MainWindow", "Remove Thumbs", None, QtGui.QApplication.UnicodeUTF8))
        self.action_removePYC.setText(QtGui.QApplication.translate("MainWindow", "Remove PYC", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPatch.setText(QtGui.QApplication.translate("MainWindow", "lsDf", None, QtGui.QApplication.UnicodeUTF8))
        self.action_minor.setText(QtGui.QApplication.translate("MainWindow", "Minor", None, QtGui.QApplication.UnicodeUTF8))
        self.action_major.setText(QtGui.QApplication.translate("MainWindow", "Major", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLish.setText(QtGui.QApplication.translate("MainWindow", "lish", None, QtGui.QApplication.UnicodeUTF8))
        self.action_aboutApplication.setText(QtGui.QApplication.translate("MainWindow", "About application", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_patch.setText(QtGui.QApplication.translate("MainWindow", "Patch", None, QtGui.QApplication.UnicodeUTF8))
