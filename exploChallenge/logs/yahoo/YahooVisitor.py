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

class YahooVisitor:
    timestamp = None
    features = None

    def __init__(self, timestamp, features):

        self.features = features
        self.timestamp = timestamp

    def getTimestamp(self):
        return self.timestamp


    def getFeatures(self):
        return self.features
