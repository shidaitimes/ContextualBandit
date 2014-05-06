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
#package myPolicy;

import random

from exploChallenge.policies.ContextualBanditPolicy import ContextualBanditPolicy

class MyPolicy(ContextualBanditPolicy):

    def __init__(self):
        #Any initialization of your algorithm should be done here.
        pass


    #@Override
    def getActionToPerform(self, visitor, possibleActions):
        # Given a visitor, you have to choose the "best" article in the list.
        #return possibleActions[-1]#// here we choose the last article !
        return possibleActions[0] #// here we choose the first article !
        #return random.choice(possibleActions)
        #return random.gauss()



    #@Override
    def updatePolicy(self, c, a, reward):
        # update your policy given the visitor, the displayed article and
        # the associated reward (click or not click)
        pass


