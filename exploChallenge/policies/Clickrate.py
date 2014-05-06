
__author__ = 'dai.shi'

import random as rn
import operator
import math
import numpy as np

from exploChallenge.policies.ContextualBanditPolicy import ContextualBanditPolicy

'''
def id_max(x):
    return max(x.iteritems(), key=operator.itemgetter(1))[0]
'''

def rargmax(x):
    m = np.amax(x)
    indices = np.nonzero(x == m)[0]
    return rn.choice(indices)

class Clickrate(ContextualBanditPolicy):


    def __init__(self):
        self.counts = {}
        self.rates = {}
        return




    def getActionToPerform(self, visitor,possibleActions):

        for action in possibleActions:
            if action.getID() not in self.counts:
                self.rates[action.getID()] = 1.0
                self.counts[action.getID()] = 1.0
            #psrates[action.getID()] = self.rates[action.getID()]

        psrates = [self.rates[a.getID()] for a in possibleActions]


        action = possibleActions[rargmax(psrates)]
        return action



    def updatePolicy(self, content, chosen_arm, reward):
        self.counts[chosen_arm.getID()] += 1
        n = self.counts[chosen_arm.getID()]

        rate = self.rates[chosen_arm.getID()]
        new_rate = rate + (reward - rate) / (n + 1)
        self.rates[chosen_arm.getID()] = new_rate
        return



