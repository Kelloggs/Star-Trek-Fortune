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

import os
from random import randint

class QuoteParser():
    def __init__(self, directoryPath):
        self._fileLocation = directoryPath + 'contents/code/quotes/'
        self._files = os.listdir(self._fileLocation)
        self._quotes = []
        for file in self._files:    
            textTmp = ''
            with open(self._fileLocation + file) as quoteFile:
                for line in quoteFile.readlines():
                    textTmp += line
            self._quotes.extend(textTmp.split('%'))
        if '' in self._quotes:
            self._quotes.remove('')
                                
                         
    def getRandomQuote(self):
        randFile = randint(0, (len(self._quotes) - 1))
        return self._quotes[randFile].strip('\n')           
