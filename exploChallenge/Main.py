#-------------------------------------------------------------------------------
# Copyright (c) 2012 Jose Antonio Martin H..
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v3.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/gpl.html
#
# Contributors:
#     Jose Antonio Martin H. - Translation to Python from Java
#     Jeremie Mary - very minor adaptation for the challenge
#-------------------------------------------------------------------------------
#package exploChallenge;

#import java.io.FileNotFoundException;
import sys
import time



from myPolicy.MyPolicy import MyPolicy
from exploChallenge.eval.EvaluationPolicy import EvaluationPolicy
from exploChallenge.eval.Evaluator import Evaluator
from exploChallenge.eval.MyEvaluationPolicy import MyEvaluationPolicy
from exploChallenge.logs.FromFileLogLineGenerator import FromFileLogLineGenerator
from exploChallenge.logs.yahoo.YahooArticle import YahooArticle
from exploChallenge.logs.yahoo.YahooLogLineReader import YahooLogLineReader
from exploChallenge.logs.yahoo.YahooVisitor import YahooVisitor
from exploChallenge.policies.ContextualBanditPolicy import ContextualBanditPolicy
from exploChallenge.policies.RandomPolicy import RandomPolicy
from exploChallenge.policies.eGreedy import eGreedy
from exploChallenge.policies.Softmax import Softmax
from exploChallenge.policies.UCB1 import UCB1
from exploChallenge.policies.EXP3 import EXP3
from exploChallenge.eval.EvaluatorEXP3 import EvaluatorEXP3
from exploChallenge.policies.Mostclick import Mostclick
from exploChallenge.policies.Clickrate import Clickrate
from exploChallenge.policies.NaiveIII import Naive3
from exploChallenge.policies.Contextualclick import Contextualclick
from exploChallenge.policies.LinearBayes import LinearBayes
from exploChallenge.policies.LinearBayesFtu import LinearBayesFtu









class Main:

    """
     * @param argv: a Python list containing the command line args
     * a usual, argv[0] is the full path name of this program.
     * @throws FileNotFoundException -> IOError?
    """
    def main(self, argv = sys.argv):

        currentTimeMillis = lambda:  int(round(time.time() * 1000))
        t = currentTimeMillis()
        reader = None

        try:
            #reader = YahooLogLineReader("/home/guests/guest05/YahooEvals/data/ydata-fp-td-clicks-v2_0.201110", 2, 6, 136)
            reader = YahooLogLineReader("../ydata-fp-td-clicks-v2_0.201110", 2, 6, 136)
            logStep = 200000
        except:
            reader = YahooLogLineReader("../yahooTest.txt", 136)
            logStep = 1


        generator = FromFileLogLineGenerator(reader)
        #policy = MyPolicy()
        #policy = RandomPolicy()
        #policy = eGreedy()
        #policy = Softmax()
        #policy = UCB1()
        #policy = EXP3()
        #policy = Mostclick()
        #policy = Clickrate()
        #policy = Naive3()
        #policy = Contextualclick()
        policy = LinearBayes()
        #policy = LinearBayesFtu()

        evalPolicy = MyEvaluationPolicy(sys.stdout, logStep, 0)

        ev = Evaluator(generator, evalPolicy, policy)
        #ev = EvaluatorEXP3(generator, evalPolicy, policy)


        value = ev.runEvaluation()

        if logStep == 1:
            print("final result => " + str(value))
            print(str(currentTimeMillis() - t) + " ms" + "\n")




if __name__ == '__main__':

    app = Main()
    app.main(sys.argv)
