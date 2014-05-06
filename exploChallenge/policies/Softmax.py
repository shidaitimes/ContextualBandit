__author__ = 'dai.shi'

import random
import operator
import math

from exploChallenge.policies.ContextualBanditPolicy import ContextualBanditPolicy

def categorical_draw(x):
    z = random.random()
    cum_prob = 0.0
    for p in x:
        prob = x[p]
        cum_prob += prob
        if cum_prob > z:
            return p
    return x.iterkeys().next()

class Softmax(ContextualBanditPolicy):


    def __init__(self):
        self.temperature = 0.1
        self.counts = {}
        self.values = {}


    def getActionToPerform(self, visitor,possibleActions):
        psvalues = {}
        probs = {}

        for action in possibleActions:
            if action.getID() not in self.counts:
                self.counts[action.getID()] = 0
                self.values[action.getID()] = 0
            psvalues[action.getID()] = self.values[action.getID()]


        z = sum([math.exp(psvalues[v] / self.temperature) for v in psvalues])

        for v in psvalues:
            probs[v]= math.exp(psvalues[v] / self.temperature) / z


        id = categorical_draw(probs)
        for action in possibleActions:
            if action.getID() == id:
                return action


    def updatePolicy(self, content, chosen_arm, reward):
        self.counts[chosen_arm.getID()] = self.counts[chosen_arm.getID()] + 1
        n = self.counts[chosen_arm.getID()]

        value = self.values[chosen_arm.getID()]
        if reward is True:
            new_value = ((n - 1) / float(n)) * value + (1 / float(n))
            self.values[chosen_arm.getID()] = new_value
        return



