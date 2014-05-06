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
#package exploChallenge.eval;

from exploChallenge.eval.IllegalChoiceOfArticleException import IllegalChoiceOfArticleException

class Evaluator:

    generator = None
    evalPolicy = None
    policy = None
    linesToSkip = 0


    def __init__(self, generator, evalPolicy, policy, linesToSkip = 0):
        self.generator = generator
        self.evalPolicy = evalPolicy
        self.policy = policy
        self.linesToSkip = linesToSkip;


    def runEvaluation(self):
        while self.generator.hasNext():
            logLine = self.generator.generateLogLine()
            if self.linesToSkip > 0:
                self.linesToSkip -= 1
                continue

            #print [i.getID() for i in self.generator.getPossibleActions()]
            #print self.generator.getPossibleActions()

            a = self.policy.getActionToPerform(logLine.getContext(), self.generator.getPossibleActions())
            #print a
            if a not in self.generator.getPossibleActions():
                raise IllegalChoiceOfArticleException
            self.evalPolicy.evaluate(logLine, a)
            if a == logLine.getAction():
                self.policy.updatePolicy(logLine.getContext(), logLine.getAction(), logLine.getReward())

        return self.evalPolicy.getResult()



