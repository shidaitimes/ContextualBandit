__author__ = 'dai.shi'

import numpy as np
import random as rn
import operator
import math

from exploChallenge.policies.ContextualBanditPolicy import ContextualBanditPolicy


def rargmax(x):
    m = np.amax(x)
    indices = np.nonzero(x == m)[0]
    return rn.choice(indices)

class Mostclick(ContextualBanditPolicy):


    def __init__(self):
        self.values = {}
        return




    def getActionToPerform(self, visitor,possibleActions):

        for action in possibleActions:
            if action.getID() not in self.values:
                self.values[action.getID()] = 1.0

        psvalues = [ self.values[a.getID()] for a in possibleActions]

        action = possibleActions[rargmax(psvalues)]

        return action

    def updatePolicy(self, content, chosen_arm, reward):
        self.values[chosen_arm.getID()] += reward
        return





