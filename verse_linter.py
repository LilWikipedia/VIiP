
from verse_lexer import lexicon
from verse_parser import Parser

def get_ast(source_code):
    lexer = lexicon(source_code)
    #tokens = lexer.tokenize()
    parser = Parser(lexer)
    return parser.parse()
