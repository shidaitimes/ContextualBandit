#-------------------------------------------------------------------------------
# Copyright (c) 2012 Jose Antonio Martin H..
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v3.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/gpl.html
#
# Contributors:
#     Jose Antonio Martin H. - Translation to Python from Java
#-------------------------------------------------------------------------------
#package exploChallenge.logs.yahoo;


import array

from exploChallenge.logs.LogLineReader import LogLineReader
from exploChallenge.logs.yahoo.YahooLogLine import YahooLogLine
from exploChallenge.logs.yahoo.YahooArticle import YahooArticle
from exploChallenge.logs.yahoo.YahooVisitor import YahooVisitor
from exploChallenge.logs.scanner import Scanner



class YahooLogLineReader(LogLineReader):

    indexSize = 2
    scan = Scanner()
    nbOfFeatures = 0
    possibleActions = list()
    currentFile = 0
    lastFile = 0
    filePrefix = ""

    def buildNextScanner(self):
        self.currentFile += 1
        file_id = str(self.currentFile)

        while (len(file_id) < self.indexSize):
            file_id = "0" + file_id

        file_id = self.filePrefix + file_id
        with open(file_id) as f:
            data = f.read()

        self.scan = Scanner(data)
        self.scan.useDelimiter("\n")

    def __init__(self, a, b, c = None, d = None):
        if c is None and d is None:
            self.__init1__(a, b)
        else:
            self.__init2__(a, b, c, d)


    def __init1__(self, filePath, nbOfFeatures):
        self.nbOfFeatures = nbOfFeatures

        with open(filePath) as f:
            data = f.read()

        self.scan = Scanner(data)
        self.scan.useDelimiter("\n")
        self.currentFile = 0
        self.lastFile = 0


    def __init2__(self, prefix, firstFile, lastFile, nbOfFeatures):
        self.nbOfFeatures = nbOfFeatures
        self.currentFile = firstFile - 1
        self.lastFile = lastFile
        self.filePrefix = prefix
        self.buildNextScanner()




    #@Override
    def read(self):
        if not self.hasNext():
            raise IOError("no next line to read")
        line = self.scan.next()
        idScan = Scanner(line)
        idScan.useDelimiter("\\s+\\|id-")

        scanLine = Scanner(idScan.next())
        scanLine.useDelimiter("[\\s]+")
        
        features = array.array('B', [0] * self.nbOfFeatures) # an array of unsigned ints (1 byte per value)

        visitor = YahooVisitor(scanLine.nextLong(), features)
        article = YahooArticle(int(scanLine.next()[3:]))
        logLine = YahooLogLine(visitor, article, scanLine.nextInt() == 1)
        scanLine.next()

        while scanLine.hasNext():
            features[scanLine.nextInt() - 1] = 1

        self.possibleActions = list()
        while idScan.hasNext():
            self.possibleActions.append(YahooArticle(idScan.nextInt()))

        return logLine;


    #@Override
    def hasNext(self):
        if self.scan.hasNext():
            return True
        if self.currentFile == self.lastFile:
            return False

        self.buildNextScanner()
        return self.hasNext()


    #@Override
    def close(self):
        pass


    #@Override
    def getPossibleActions(self):
        return self.possibleActions

