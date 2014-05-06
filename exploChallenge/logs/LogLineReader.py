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

class LogLineReader:

    def read(self):
        raise NotImplementedError

    def hasNext(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    #@returns the possible actions corresponding to the last read log line.
    def getPossibleActions(self):
        raise NotImplementedError

