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

class YahooArticle:

    yid = 0

    def __init__(self, yid):
        self.yid = yid


    def getID(self):
        return self.yid


    #@Override
    def __eq__(self, other):
        if other.__class__ == self.__class__:
            return other.getID() == self.yid

        return False




