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
        fileLocation = directoryPath + 'contents/code/quotes/'
        files = os.listdir(fileLocation)
        self._quotes = []
        filter = '\n', '', '\0'
        for file in files:     
            # do not parse hidden or temp files  
            if not file.startswith(".") and not file.endswith("~"):
                with open(fileLocation + file) as quoteFile:
                    tmpString = ''
                    for line in quoteFile.readlines():                    
                        if not line.startswith('%'):
                            tmpString += line
                        if line.startswith('%'):
                            if tmpString not in filter:
                                tmpString = tmpString.strip('\n')
                                tmpString = tmpString.strip()
                                self._quotes.append(tmpString)  
                            tmpString = ''                 
                                
                         
    def getRandomQuote(self):
        randFile = randint(0, (len(self._quotes) - 1))
        return unicode(self._quotes[randFile], "UTF-8")           
