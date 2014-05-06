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

import io
from exploChallenge.eval.EvaluationPolicy import EvaluationPolicy

class MyEvaluationPolicy(EvaluationPolicy):

    clicks = 0;
    evaluations = 0;
    lines = 0;
    logger = io.StringIO();
    logFrequency = 0;
    linesToSkip = 0;

    def __init__(self, a, b = None, c = None):
        if type(a) == type(1):
            self.__init1__(a)
        else:
            self.__init2__(a, b, c)


    def __init1__(self, linesToSkip):
        self.linesToSkip = linesToSkip
        self.clicks = 0
        self.evaluations = 0
        self.lines = 0
        self.logFrequency = -1


    def __init2__(self, outputStream, logFrequency, linesToSkip):
        self.clicks = 0;
        self.evaluations = 0;
        self.linesToSkip = linesToSkip;
        self.lines = 0;
        self.logFrequency = logFrequency;
        self.logger = outputStream
        self.logger.write("lines evaluations clicks score \n")



    #@Override
    def log(self):
        self.logger.write(str(self.lines) + " " + str(self.evaluations) + " " + str(self.clicks) + " " + str(self.getResult()) + "\n")
        self.logger.flush()

    #@Override
    def getResult(self):
        try:
            return float(self.clicks) / float(self.evaluations)
        except:
            return 0.0


    #@Override
    def evaluate(self, logLine, chosenAction):
        if self.linesToSkip > 0:
            self.linesToSkip -= 1
            return

        if logLine.getAction() == chosenAction:
            self.evaluations += 1
            if logLine.getReward():
                self.clicks += 1

        self.lines += 1
        if self.logFrequency != -1 and self.lines % self.logFrequency == 0:
            self.log()

