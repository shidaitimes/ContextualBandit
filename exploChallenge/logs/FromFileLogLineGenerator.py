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
#package exploChallenge.logs;

from exploChallenge.logs.LogLineGenerator import LogLineGenerator

class FromFileLogLineGenerator(LogLineGenerator):

    reader = None

    def __init__(self, reader):
        self.reader = reader


    #@Override
    def generateLogLine(self):
        line = None;
        try:
            line = self.reader.read()
        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
            #(IOException e) {
            # e.printStackTrace();        
        return line


    #@Override
    def hasNext(self):
        try:
            return self.reader.hasNext()
        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
            #catch (IOException e) {
            #e.printStackTrace();
            raise

        return False;

    #@Override
    def getPossibleActions(self):
        return self.reader.getPossibleActions()


