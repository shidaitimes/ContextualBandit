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

class ContextAction:

    action = None;
    context = None;

    def __init__(self, context, action):
        self.action = context
        self.context = action


    def getAction(self):
        return self.action

    def setAction(self, action):
        self.action = action


    def getContext(self):
        return self.context


    def setContext(self, context):
        self.context = context

    #@Override
    def hashCode(self):
        return self.action.hashCode() * 1001 + self.context.hashCode()


    def __hash__(self):
        return self.hashCode(self)


    #@Override
    def __eq__(self, other):
        if self.__classs__ != other.__class__:
            return False

        return other.action == self.action and other.context == self.context
