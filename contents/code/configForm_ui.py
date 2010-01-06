# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/configForm.ui'
#
# Created: Tue Jan  5 22:30:55 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(362, 205)
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 341, 135))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textColor_button = KColorButton(self.gridLayoutWidget)
        self.textColor_button.setObjectName("textColor_button")
        self.gridLayout_2.addWidget(self.textColor_button, 0, 1, 1, 1)
        self.Dropshadow_label = QtGui.QLabel(self.gridLayoutWidget)
        self.Dropshadow_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Dropshadow_label.setObjectName("Dropshadow_label")
        self.gridLayout_2.addWidget(self.Dropshadow_label, 1, 0, 1, 1)
        self.shadowColor_button = KColorButton(self.gridLayoutWidget)
        self.shadowColor_button.setObjectName("shadowColor_button")
        self.gridLayout_2.addWidget(self.shadowColor_button, 1, 1, 1, 1)
        self.TextColor_label = QtGui.QLabel(self.gridLayoutWidget)
        self.TextColor_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TextColor_label.setTextFormat(QtCore.Qt.AutoText)
        self.TextColor_label.setObjectName("TextColor_label")
        self.gridLayout_2.addWidget(self.TextColor_label, 0, 0, 1, 1)
        self.Logo_checkbox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.Logo_checkbox.setObjectName("Logo_checkbox")
        self.gridLayout_2.addWidget(self.Logo_checkbox, 2, 1, 1, 1)
        self.Background_checkbox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.Background_checkbox.setObjectName("Background_checkbox")
        self.gridLayout_2.addWidget(self.Background_checkbox, 3, 1, 1, 1)
        self.Interval_label = QtGui.QLabel(self.gridLayoutWidget)
        self.Interval_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Interval_label.setObjectName("Interval_label")
        self.gridLayout_2.addWidget(self.Interval_label, 4, 0, 1, 1)
        self.update_SpinBox = KIntSpinBox(self.gridLayoutWidget)
        self.update_SpinBox.setMaximum(120)
        self.update_SpinBox.setProperty("value", 5)
        self.update_SpinBox.setObjectName("update_SpinBox")
        self.gridLayout_2.addWidget(self.update_SpinBox, 4, 1, 1, 1)
        self.Font_combo = QtGui.QFontComboBox(Dialog)
        self.Font_combo.setGeometry(QtCore.QRect(7, 20, 208, 25))
        self.Font_combo.setObjectName("Font_combo")
        self.Italic_button = QtGui.QPushButton(Dialog)
        self.Italic_button.setGeometry(QtCore.QRect(330, 20, 25, 25))
        self.Italic_button.setObjectName("Italic_button")
        self.fontSize_combo = QtGui.QComboBox(Dialog)
        self.fontSize_combo.setGeometry(QtCore.QRect(215, 20, 91, 25))
        self.fontSize_combo.setObjectName("fontSize_combo")
        self.Bold_button = QtGui.QPushButton(Dialog)
        self.Bold_button.setGeometry(QtCore.QRect(305, 20, 25, 25))
        self.Bold_button.setObjectName("Bold_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.Dropshadow_label.setText(QtGui.QApplication.translate("Dialog", "Dropshadow color", None, QtGui.QApplication.UnicodeUTF8))
        self.TextColor_label.setText(QtGui.QApplication.translate("Dialog", "Text color", None, QtGui.QApplication.UnicodeUTF8))
        self.Logo_checkbox.setText(QtGui.QApplication.translate("Dialog", "Show UFP Flag", None, QtGui.QApplication.UnicodeUTF8))
        self.Background_checkbox.setText(QtGui.QApplication.translate("Dialog", "Show Plasma Background", None, QtGui.QApplication.UnicodeUTF8))
        self.Interval_label.setText(QtGui.QApplication.translate("Dialog", "Update Interval", None, QtGui.QApplication.UnicodeUTF8))
        self.Italic_button.setText(QtGui.QApplication.translate("Dialog", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.Bold_button.setText(QtGui.QApplication.translate("Dialog", "B", None, QtGui.QApplication.UnicodeUTF8))

from PyKDE4.kdeui import KColorButton, KIntSpinBox
