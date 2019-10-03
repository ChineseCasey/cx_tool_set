# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item_aov.ui'
#
# Created: Fri Jul 28 11:37:17 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 66)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.item_aov_frame = QtGui.QFrame(Dialog)
        self.item_aov_frame.setStyleSheet("")
        self.item_aov_frame.setFrameShape(QtGui.QFrame.Box)
        self.item_aov_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.item_aov_frame.setLineWidth(1)
        self.item_aov_frame.setMidLineWidth(1)
        self.item_aov_frame.setObjectName("item_aov_frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.item_aov_frame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.aov_name_label = QtGui.QLabel(self.item_aov_frame)
        self.aov_name_label.setStyleSheet("font: 75 9pt \"Consolas\";\n"
"color: rgb(230, 230, 0);\n"
"color: rgb(70, 206, 255);")
        self.aov_name_label.setText("")
        self.aov_name_label.setObjectName("aov_name_label")
        self.horizontalLayout_2.addWidget(self.aov_name_label)
        spacerItem = QtGui.QSpacerItem(90, 18, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.ID_btn_lay = QtGui.QHBoxLayout()
        self.ID_btn_lay.setSpacing(0)
        self.ID_btn_lay.setObjectName("ID_btn_lay")
        self.ID_Red_btn = QtGui.QToolButton(self.item_aov_frame)
        self.ID_Red_btn.setStyleSheet("font: 75 9pt \"Consolas\";")
        self.ID_Red_btn.setAutoRaise(True)
        self.ID_Red_btn.setObjectName("ID_Red_btn")
        self.ID_btn_lay.addWidget(self.ID_Red_btn)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ID_btn_lay.addItem(spacerItem2)
        self.ID_Green_btn_ = QtGui.QToolButton(self.item_aov_frame)
        self.ID_Green_btn_.setStyleSheet("font: 75 9pt \"Consolas\";")
        self.ID_Green_btn_.setAutoRaise(True)
        self.ID_Green_btn_.setObjectName("ID_Green_btn_")
        self.ID_btn_lay.addWidget(self.ID_Green_btn_)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ID_btn_lay.addItem(spacerItem3)
        self.ID_Blue_btn = QtGui.QToolButton(self.item_aov_frame)
        self.ID_Blue_btn.setStyleSheet("font: 75 9pt \"Consolas\";")
        self.ID_Blue_btn.setAutoRaise(True)
        self.ID_Blue_btn.setObjectName("ID_Blue_btn")
        self.ID_btn_lay.addWidget(self.ID_Blue_btn)
        self.horizontalLayout_2.addLayout(self.ID_btn_lay)
        self.line = QtGui.QFrame(self.item_aov_frame)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.delete_btn = QtGui.QToolButton(self.item_aov_frame)
        self.delete_btn.setStyleSheet("color: rgb(255, 0, 4);")
        self.delete_btn.setAutoRaise(True)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_2.addWidget(self.delete_btn)
        self.horizontalLayout.addWidget(self.item_aov_frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.ID_Red_btn.setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.ID_Green_btn_.setText(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.ID_Blue_btn.setText(QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_btn.setText(QtGui.QApplication.translate("Dialog", "X", None, QtGui.QApplication.UnicodeUTF8))

