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

from PyQt4.QtCore import Qt, SIGNAL, QSizeF, QPointF, QTimer
from PyQt4.QtGui import QColor, QFont, QGraphicsLinearLayout

from PyKDE4.kdeui import KPageDialog, KDialog, KIcon
from PyKDE4.plasma import Plasma
from PyKDE4.kdecore import i18n
from PyKDE4 import plasmascript

from quoteParser import QuoteParser
from stfConfig import STFConfig
 
class StarTrekFortunes(plasmascript.Applet):
    
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)

    def init(self): 
        self._text = None
        self._quoteParser = QuoteParser(self.package().path())
        
        # set configuration
        self.conf = self.config('startrekfortune-plasmoid')

        # parse or initialize configurations
        self._textColor = QColor(self.conf.readEntry("textColor", "#000000"))
        self._shadowColor = QColor(self.conf.readEntry("shadowColor", "#FFFFFF"))
        self._font = QFont(self.conf.readEntry("font", QFont("Sans-Serif", 12, QFont.Bold)))
        self._showBackground = self.conf.readEntry("showBackground", "False").toBool()
        self._showSVG = self.conf.readEntry("showSVG", "True").toBool()
        self._updateInterval = self.conf.readEntry("updateInterval", 5).toInt()[0]

        # set timer
        self._updateTimer = QTimer()
        self.setTimer()
        
        self.setPlasmaBackground()
            
        # set layout and initial size
        self.layout = QGraphicsLinearLayout(Qt.Horizontal, self.applet)
        self.setAspectRatioMode(Plasma.KeepAspectRatio)
        self.setHasConfigurationInterface(True)
        if self.conf.readEntry("size_initialized", "0").toString() == "0":
            self.resize(385, 277)
            self.conf.writeEntry("size_initialized", "1")
    
        
    def showConfigurationInterface(self):
        dialog = KPageDialog()
        dialog.setWindowTitle("Star Trek Fortune Settings")
        dialog.setFaceType(KPageDialog.List)
        dialog.setButtons(KDialog.ButtonCode(KDialog.Ok | KDialog.Cancel))

        # Appearance Settings
        defaultConfig = {"textColor":self._textColor,"shadowColor":self._shadowColor,
                         "font":self._font,"hideBackground":self._showBackground, 
                         "hideSVG":self._showSVG, "updateInterval":self._updateInterval}
        self._configDialog = STFConfig(self, defaultConfig)
        appearancePage = dialog.addPage(self._configDialog,i18n("Appearance"))
        appearancePage.setIcon(KIcon("preferences-desktop-color"))
        
        self.connect(dialog, SIGNAL("okClicked()"), self.configAccepted)
        self.connect(dialog, SIGNAL("cancelClicked()"), self.configDenied)
        dialog.resize(540,330)
        dialog.exec_()
        
    def configAccepted(self):
        # apply new settings
        self._textColor = self._configDialog.getTextColor()
        self._shadowColor = self._configDialog.getShadowColor()  
        self._font = self._configDialog.getFont()   
        self._showBackground = self._configDialog.getShowBackground()
        self._showSVG = self._configDialog.getShowSVG()
        self._updateInterval = self._configDialog.getUpdateInterval()
        
        # save new configuration
        self.conf.writeEntry("textColor", self._textColor.name())
        self.conf.writeEntry("shadowColor", self._shadowColor.name())
        self.conf.writeEntry("font", self._font.toString())
        self.conf.writeEntry("showBackground", str(self._showBackground))
        self.conf.writeEntry("showSVG", str(self._showSVG))
        self.conf.writeEntry("updateInterval", str(self._updateInterval))
        
        self.setTimer()
        self.setPlasmaBackground()
        self.update()

    def configDenied(self):
        pass
    
    def setPlasmaBackground(self):
        # show plasma background if preference is set
        if self._showBackground:
            self.setBackgroundHints(Plasma.Applet.DefaultBackground)
        else:
            self.setBackgroundHints(Plasma.Applet.NoBackground)
 
    def paintInterface(self, painter, option, rect):
        painter.save()
        
        # show UFP logo if preference is set 
        if self._showSVG:
            svg_current = Plasma.Svg()
            svg_current.setImagePath(self.package().path() + "contents/icons/ufp.svg")
            svg_current.resize(QSizeF(rect.size()))
            svg_current.paint(painter, QPointF(rect.topLeft()))          
        if self._text is None:
            self._text = self.getFortune()

        # first paint text for dropshadow and then paint the text
        painter.setPen(self._shadowColor)
        rect.moveTo(rect.left() + 1, rect.top() + 1)
        painter.setFont(self._font)
        painter.drawText(rect,Qt.TextWordWrap | Qt.AlignCenter, self._text)
        rect.moveTo(rect.left() - 1, rect.top() - 1)
        painter.setPen(self._textColor)
        painter.setFont(self._font)
        painter.drawText(rect, Qt.TextWordWrap | Qt.AlignCenter, self._text)
        painter.restore()

    def getFortune(self):
        return self._quoteParser.getRandomQuote()
    
    def updateFortune(self):
        self._text = self.getFortune()
        self.update()
        
    def setTimer(self):
        if not self._updateInterval is 0:        
            self._updateTimer.setInterval(self._updateInterval * 60 * 1000)
            self._updateTimer.setSingleShot(False)
            self.connect(self._updateTimer, SIGNAL("timeout()"), self.updateFortune)
            self._updateTimer.start()
        else:
            self._updateTimer.stop()
            
 
def CreateApplet(parent):
    return StarTrekFortunes(parent)
 
