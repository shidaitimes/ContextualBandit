__author__ = 'ftruzzi'

# Linear Bayes solution based on "Linear Bayes Policy for Learning in Contextual-Bandits"
# but not using the pursuit method of calculation

import numpy as np
from collections import defaultdict
from exploChallenge.policies.ContextualBanditPolicy import ContextualBanditPolicy


class LinearBayesFtu(ContextualBanditPolicy):
    def __init__(self):
        self.clicksPerFeature = {}
        self.selectionsPerFeature = {}
        self.clicksPerArticle = {}
        self.selectionPerArticle = {}
        self.featureClickRate = {}
        for feature in xrange(136):
            self.featureClickRate[feature] = 0

    def getActionToPerform(self, visitor, possibleActions):

        for article in possibleActions:
            if article.getID() not in self.clicksPerFeature:
                self.clicksPerFeature[article.getID()] = defaultdict(int)
                self.selectionsPerFeature[article.getID()] = defaultdict(int)
                self.clicksPerArticle[article.getID()] = 1
                self.selectionPerArticle[article.getID()] = 1

        # corrigir quando nao estiver com sono

        sumOfclicks = np.asarray([sum(self.clicksPerFeature[a.getID()].values() + [1]) for a in possibleActions])
        sumOfSelections = np.asarray([sum(self.selectionsPerFeature[a.getID()].values() + [1]) for a in possibleActions])
        Pai = sumOfclicks/sumOfSelections

        Pa = np.asarray([self.clicksPerArticle[a.getID()] / self.selectionPerArticle[a.getID()] for a in possibleActions])
        Pi = np.asarray([self.clicksPerFeature[a.getID()] / self.selectionsPerFeature[a.getID()] for a in possibleActions])

        action = possibleActions[np.argmax((sumOfclicks / sumOfSelections) * Pa / Pi)]


        #action = possibleActions[np.argmax([((1.0 * x) / y) for x, y in zip(sumOfclicks, sumOfSelections)])]

        return action

    def updatePolicy(self, c, a, reward):
        self.selectionPerArticle[a.getID()] += 1
        if reward is True:
            self.clicksPerArticle += 1
        for f, p in enumerate(c.getFeatures()):
            if p is 1:
                self.featureClickRate[f] += 1
                if reward is True:
                    self.clicksPerFeature[a.getID()][f] += 1.0
                self.selectionsPerFeature[a.getID()][f] += 1.0
