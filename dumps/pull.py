# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/pull.ui'
#
# Created: Sat Apr 25 15:06:07 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 674)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox_bar = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_bar.setMinimumSize(QtCore.QSize(0, 40))
        self.groupbox_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.groupbox_bar.setFlat(False)
        self.groupbox_bar.setCheckable(False)
        self.groupbox_bar.setObjectName("groupbox_bar")
        self.horizontallayout_bar = QtGui.QHBoxLayout(self.groupbox_bar)
        self.horizontallayout_bar.setSpacing(0)
        self.horizontallayout_bar.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_bar.setObjectName("horizontallayout_bar")
        self.pushButton_3 = QtGui.QPushButton(self.groupbox_bar)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 35))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontallayout_bar.addWidget(self.pushButton_3)
        self.pushButton = QtGui.QPushButton(self.groupbox_bar)
        self.pushButton.setObjectName("pushButton")
        self.horizontallayout_bar.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.groupbox_bar)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontallayout_bar.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.groupbox_bar)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)
        self.button_thumbnail = QtGui.QPushButton(self.groupBox)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setObjectName("button_thumbnail")
        self.gridLayout.addWidget(self.button_thumbnail, 7, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_description = QtGui.QLabel(self.groupBox)
        self.label_description.setObjectName("label_description")
        self.gridLayout.addWidget(self.label_description, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.textedit_description = QtGui.QTextEdit(self.groupBox)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 90))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 90))
        self.textedit_description.setObjectName("textedit_description")
        self.gridLayout.addWidget(self.textedit_description, 6, 0, 1, 2)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.action_import_maya = QtGui.QAction(MainWindow)
        self.action_import_maya.setObjectName("action_import_maya")
        self.action_reference_maya = QtGui.QAction(MainWindow)
        self.action_reference_maya.setObjectName("action_reference_maya")
        self.action_import_usd = QtGui.QAction(MainWindow)
        self.action_import_usd.setObjectName("action_import_usd")
        self.action_reference_usd = QtGui.QAction(MainWindow)
        self.action_reference_usd.setObjectName("action_reference_usd")
        self.action_open_source = QtGui.QAction(MainWindow)
        self.action_open_source.setObjectName("action_open_source")
        self.action_pull_replace = QtGui.QAction(MainWindow)
        self.action_pull_replace.setObjectName("action_pull_replace")
        self.action_pull = QtGui.QAction(MainWindow)
        self.action_pull.setObjectName("action_pull")
        self.action_open_location = QtGui.QAction(MainWindow)
        self.action_open_location.setObjectName("action_open_location")
        self.menuFile.addAction(self.action_import_maya)
        self.menuFile.addAction(self.action_reference_maya)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_import_usd)
        self.menuFile.addAction(self.action_reference_usd)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_pull_replace)
        self.menuFile.addAction(self.action_pull)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_open_source)
        self.menuFile.addAction(self.action_open_location)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Location", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).setText(1, QtGui.QApplication.translate("MainWindow", "sssssss", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(1, QtGui.QApplication.translate("MainWindow", "ssssssssss", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "New Subitem", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "sss", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).setText(1, QtGui.QApplication.translate("MainWindow", "sss", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(3).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(3).setText(1, QtGui.QApplication.translate("MainWindow", "sss", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "sgopi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "interactive", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Caption", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Character", None, QtGui.QApplication.UnicodeUTF8))
        self.button_thumbnail.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "sgopi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Batman", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_description.setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_import_maya.setText(QtGui.QApplication.translate("MainWindow", "Import Maya", None, QtGui.QApplication.UnicodeUTF8))
        self.action_reference_maya.setText(QtGui.QApplication.translate("MainWindow", "Reference Maya", None, QtGui.QApplication.UnicodeUTF8))
        self.action_import_usd.setText(QtGui.QApplication.translate("MainWindow", "Import USD", None, QtGui.QApplication.UnicodeUTF8))
        self.action_reference_usd.setText(QtGui.QApplication.translate("MainWindow", "Reference USD", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open_source.setText(QtGui.QApplication.translate("MainWindow", "Open Source", None, QtGui.QApplication.UnicodeUTF8))
        self.action_pull_replace.setText(QtGui.QApplication.translate("MainWindow", "Pull with Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.action_pull.setText(QtGui.QApplication.translate("MainWindow", "Pull without Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open_location.setText(QtGui.QApplication.translate("MainWindow", "Open Location", None, QtGui.QApplication.UnicodeUTF8))

