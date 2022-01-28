import operator
import speech_rec as s
import text_to_speech as t
def main():
    t.speak("Sure, tell me what you want to calculate, example: 3 plus 3")
    calc = s.listen()
    def getfn(op):
        return {
            '+' : operator.add,
            '-' : operator.sub,
            'x' : operator.mul,
            'divided' :operator.__truediv__,
            'Mod' : operator.mod,
            'mod' : operator.mod,
            '^' : operator.xor,
            }[op]

    def getsoln(op1, oper, op2):
        op1,op2 = int(op1), int(op2)
        return getfn(oper)(op1, op2)
    t.speak("The answer is")
    t.speak(getsoln(*(calc.split())))