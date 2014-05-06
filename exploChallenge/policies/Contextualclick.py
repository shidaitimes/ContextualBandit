__author__ = 'dai.shi'

import random as rn
import operator
import math
import numpy as np

from exploChallenge.policies.ContextualBanditPolicy import ContextualBanditPolicy
'''
def rargmax(x):
    m = np.amax(x)
    indices = np.nonzero(x == m)[0]
    return rn.choice(indices)
    '''
def rargmax(x):
    return np.argmax(x)


class Contextualclick(ContextualBanditPolicy):


    def __init__(self):
        self.clicksPerFeature = {}
        self.selectionsPerFeature = {}
        return




    def getActionToPerform(self, visitor,possibleActions):

        for action in possibleActions:
            if action.getID() not in self.clicksPerFeature:
                self.clicksPerFeature[action.getID()] = np.ones(136)
                self.selectionsPerFeature[action.getID()] = np.ones(136)

        #probs = [sum(visitor.getFeatures()*self.clicksPerFeature[action.getID()])/sum(visitor.getFeatures()*self.selectionsPerFeature[action.getID()]) for action in possibleActions]
        probs = [sum(visitor.getFeatures()*(self.clicksPerFeature[action.getID()]/self.selectionsPerFeature[action.getID()])) for action in possibleActions]


        action = possibleActions[rargmax(probs)]
        return action


    def updatePolicy(self, content, chosen_arm, reward):
        self.selectionsPerFeature[chosen_arm.getID()] += content.getFeatures()
        if reward is True:
            self.clicksPerFeature[chosen_arm.getID()] += content.getFeatures()
        return



