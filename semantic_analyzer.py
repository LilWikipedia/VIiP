# semantic_analyzer.py

from symboltable import SymbolTable
from nodes import *

def analyze(ast):
    symbol_table = SymbolTable()
    errors = []
    
    def visit(node):
        if isinstance(node, VariableDeclaration):
            if symbol_table.declare(node.name, node.type):
                errors.append(f"Variable '{node.name}' redeclared.")
        elif isinstance(node, VariableReference):
            if not symbol_table.lookup(node.name):
                errors.append(f"Variable '{node.name}' not declared.")
        for child in node.children:
            visit(child)
    
    visit(ast)
    return errors
