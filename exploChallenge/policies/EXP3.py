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

class EXP3(ContextualBanditPolicy):


    def __init__(self):
        self.gamma = 0.5
        self.weights = {}


    def getActionToPerform(self, visitor,possibleActions):
        psweights ={}
        probs = {}
        for action in possibleActions:
            if action.getID() not in self.weights:
                self.weights[action.getID()] = 1
            psweights[action.getID()] = 0

        for psweight in psweights:
            psweights[psweight] = self.weights[psweight]


        total_weight = sum(psweights[w] for w in psweights)

        for v in psweights:
            probs[v]= (1 - self.gamma) * (self.weights[v] / total_weight)
            probs[v] = probs[v] + (self.gamma) * (1.0 / float(len(psweights)))

        id = categorical_draw(probs)
        for action in possibleActions:
            if action.getID() == id:
                return action


    def updatePolicy(self, content, chosen_arm, reward,possibleActions):
        psweights ={}
        probs = {}
        for action in possibleActions:
            if action.getID() not in self.weights:
                self.weights[action.getID()] = 1
            psweights[action.getID()] = 0

        for psweight in psweights:
            psweights[psweight] = self.weights[psweight]


        total_weight = sum(psweights[w] for w in psweights)

        for v in psweights:
            probs[v]= (1 - self.gamma) * (self.weights[v] / total_weight)
            probs[v] = probs[v] + (self.gamma) * (1.0 / float(len(psweights)))

        x = reward / probs[chosen_arm.getID()]

        growth_factor = math.exp((self.gamma / len(probs)) * x)
        self.weights[chosen_arm.getID()] = self.weights[chosen_arm.getID()] * growth_factor

