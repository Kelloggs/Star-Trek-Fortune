# -*- coding: utf-8 -*-

#===============================================================================
# Star Trek Fortune
# Copyright (C) 2009 Jens Cornelis - mail@jenscornelis.de
#
# This file is part of Star Trek Fortune.
#
#  Star Trek Fortune is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Star Trek Fortune is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Star Trek Fortune.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import QString
from configForm_ui import Ui_Dialog

class STFConfig(QWidget,Ui_Dialog):

    def __init__(self,parent,defaultConfig = None):
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.Bold_button.setCheckable(True)
        self.Italic_button.setCheckable(True)
        for value in range(8,40):
            self.fontSize_combo.addItem(QString(str(value)))
        if defaultConfig:
            self.textColor_button.setColor(defaultConfig['textColor'])
            self.shadowColor_button.setColor(defaultConfig['shadowColor'])
            self.Font_combo.setCurrentFont(defaultConfig['font'])
            self.Bold_button.setChecked(defaultConfig['font'].bold())
            self.Italic_button.setChecked(defaultConfig['font'].italic())
            self.fontSize_combo.setCurrentIndex(defaultConfig['font'].pointSize() - 8)
            self.Background_checkbox.setChecked(defaultConfig['hideBackground'])
            self.Logo_checkbox.setChecked(defaultConfig['hideSVG'])
            self.update_SpinBox.setValue(defaultConfig['updateInterval'])
        
    def getTextColor(self):
        textColor = self.textColor_button.color()
        return textColor
    
    def getShadowColor(self):
        shadowColor = self.shadowColor_button.color()
        return shadowColor
    
    def getShowBackground(self):
        return self.Background_checkbox.isChecked()
    
    def getShowSVG(self):
        return self.Logo_checkbox.isChecked()
    
    def getFont(self):
        font = self.Font_combo.currentFont()
        font.setBold(self.Bold_button.isChecked())
        font.setItalic(self.Italic_button.isChecked())
        font.setPointSize(self.fontSize_combo.currentIndex() + 8)
        return font
    
    def getUpdateInterval(self):
        return self.update_SpinBox.value()
        