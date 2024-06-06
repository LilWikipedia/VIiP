import sys
from nnodes import *
from verse_lexer import lexicon
from verse_parser import Parser
from verse_interpreter import Interpreter
import start_text

sys.setrecursionlimit(1000000)

text = 'z:int; z=7; y:=(31|5); x:=(7|22); (z,x,y)'


start_text
lexer = lexicon(text)
parser = Parser(lexer)
interpreter = Interpreter(parser)
result = interpreter.interpret()
print(repr(result))