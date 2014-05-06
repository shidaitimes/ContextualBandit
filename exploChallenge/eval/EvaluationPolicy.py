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


class EvaluationPolicy:

    def evaluate(self, logLine, chosenAction):
        raise NotImplementedError

    def getResult(self):
        raise NotImplementedError

    def log(self):
        raise NotImplementedError

