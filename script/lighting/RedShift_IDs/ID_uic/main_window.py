# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Fri Jul 28 11:37:16 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_redshift_IDs(object):
    def setupUi(self, redshift_IDs):
        redshift_IDs.setObjectName("redshift_IDs")
        redshift_IDs.resize(330, 372)
        self.verticalLayout = QtGui.QVBoxLayout(redshift_IDs)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_box_lay = QtGui.QHBoxLayout()
        self.button_box_lay.setSpacing(0)
        self.button_box_lay.setObjectName("button_box_lay")
        self.Add_btn = QtGui.QPushButton(redshift_IDs)
        self.Add_btn.setObjectName("Add_btn")
        self.button_box_lay.addWidget(self.Add_btn)
        self.sel_obj_id_btn = QtGui.QPushButton(redshift_IDs)
        self.sel_obj_id_btn.setObjectName("sel_obj_id_btn")
        self.button_box_lay.addWidget(self.sel_obj_id_btn)
        self.clear_btn = QtGui.QPushButton(redshift_IDs)
        self.clear_btn.setObjectName("clear_btn")
        self.button_box_lay.addWidget(self.clear_btn)
        self.verticalLayout.addLayout(self.button_box_lay)
        self.frame = QtGui.QFrame(redshift_IDs)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(26, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.zero_btn = QtGui.QToolButton(self.frame)
        self.zero_btn.setMinimumSize(QtCore.QSize(25, 15))
        self.zero_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.zero_btn.setObjectName("zero_btn")
        self.gridLayout.addWidget(self.zero_btn, 0, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 5, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setStyleSheet("color: rgb(12, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 7, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 6, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 10, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 8, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setStyleSheet("color: rgb(0, 4, 255);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 9, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.add_item_scrollArea = QtGui.QScrollArea(redshift_IDs)
        self.add_item_scrollArea.setWidgetResizable(True)
        self.add_item_scrollArea.setObjectName("add_item_scrollArea")
        self.scrollArea_layout = QtGui.QWidget()
        self.scrollArea_layout.setGeometry(QtCore.QRect(0, 0, 328, 311))
        self.scrollArea_layout.setObjectName("scrollArea_layout")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollArea_layout)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_item_lay = QtGui.QVBoxLayout()
        self.add_item_lay.setSpacing(0)
        self.add_item_lay.setObjectName("add_item_lay")
        self.verticalLayout_2.addLayout(self.add_item_lay)
        spacerItem6 = QtGui.QSpacerItem(20, 304, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.add_item_scrollArea.setWidget(self.scrollArea_layout)
        self.verticalLayout.addWidget(self.add_item_scrollArea)
        self.label = QtGui.QLabel(redshift_IDs)
        self.label.setStyleSheet("background-color: rgb(0, 14, 33);\n"
"color: rgb(255, 128, 0);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(redshift_IDs)
        QtCore.QMetaObject.connectSlotsByName(redshift_IDs)

    def retranslateUi(self, redshift_IDs):
        redshift_IDs.setWindowTitle(QtGui.QApplication.translate("redshift_IDs", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.Add_btn.setText(QtGui.QApplication.translate("redshift_IDs", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.sel_obj_id_btn.setText(QtGui.QApplication.translate("redshift_IDs", "Sel_Obj_Id", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_btn.setText(QtGui.QApplication.translate("redshift_IDs", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.zero_btn.setText(QtGui.QApplication.translate("redshift_IDs", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("redshift_IDs", "Red", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("redshift_IDs", "Matte name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("redshift_IDs", "Green", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("redshift_IDs", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("redshift_IDs", "ID:", None, QtGui.QApplication.UnicodeUTF8))
