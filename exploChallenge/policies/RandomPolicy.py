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
#package exploChallenge.policies;

import random

from exploChallenge.policies.ContextualBanditPolicy import ContextualBanditPolicy

class RandomPolicy(ContextualBanditPolicy):

    def __init__(self):
        pass

    #@Override
    def getActionToPerform(self, ctx, possibleActions):
        randomIndex = random.randint(0, len(possibleActions) - 1)
        return possibleActions[randomIndex]

    #@Override
    def updatePolicy(self, c, a, reward):
        pass


