__author__ = 'dai.shi'

import random
import operator
import math
import numpy as np

from exploChallenge.policies.ContextualBanditPolicy import ContextualBanditPolicy

def rargmax(x):
    return np.argmax(x)

class UCB1(ContextualBanditPolicy):


    def __init__(self):
        self.counts = {}
        self.values = {}
        return




    def getActionToPerform(self, visitor,possibleActions):
        psvalues = {}
        pscounts = {}

        for action in possibleActions:
            if action.getID() not in self.counts:
                self.counts[action.getID()] = 1.0
                self.values[action.getID()] = 1.0
            psvalues[action.getID()] = self.values[action.getID()]
            pscounts[action.getID()] = self.counts[action.getID()]

        total_counts = sum(pscounts[count] for count in pscounts)

        ucbvalues = [ self.values[a.getID()] + math.sqrt((2 * math.log(total_counts)) / pscounts[a.getID()]) for a in possibleActions]

        action = possibleActions[rargmax(ucbvalues)]

        return action


    def updatePolicy(self, content, chosen_arm, reward):
        self.counts[chosen_arm.getID()] = self.counts[chosen_arm.getID()] + 1
        n = self.counts[chosen_arm.getID()]

        value = self.values[chosen_arm.getID()]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm.getID()] = new_value
        return


