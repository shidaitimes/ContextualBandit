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

class LogLine:

    reward = None;
    action = None;
    context = None;


    def __init__(self, context = None, action = None, reward = None):


        self.setContext(context)
        self.setAction(action)
        self.setReward(reward)


    def getReward(self):
        return self.reward


    def setReward(self, reward):
        self.reward = reward


    def getAction(self):
        return self.action


    def setAction(self, action):
        self.action = action


    def getContext(self):
        return self.context


    def setContext(self, context):
        self.context = context
