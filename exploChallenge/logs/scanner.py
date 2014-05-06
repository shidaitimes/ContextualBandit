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
'''
Created on 12/03/2012

@author: Jose Antonio Martin H.
'''
from collections import deque
import re

class Scanner():
    '''
    My attempt to get a Java-like Scanner class for this!
    '''
    data = ""
    tokens = deque()

    def __init__(self, data = ""):
        '''
        Constructor
        '''
        self.data = data.strip()

    def useDelimiter(self, delimiter):
        self.tokens = deque(re.split(delimiter, self.data))

    def next(self):
        return self.tokens.popleft()

    def hasNext(self):
        return len(self.tokens) > 0

    def nextInt(self):
        return int(self.tokens.popleft())

    def nextLong(self):
        try:
            x = self.tokens.popleft()
            a = float(x)
        except:
            print "problem:[", x, "]"
            print self.data
            raise
        return a

    def close(self):
        pass


