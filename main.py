from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sys
import llvmlite.ir as ir
import llvmlite.binding as llvm
from logger import Console_Logger
from verse_lexer import lexicon
from verse_parser import Parser
from verse_interpreter import Interpreter
from symboltable import SymbolTable
from nodes import Node, VariableDeclaration, VariableReference

# Helper functions from the linter/error checking code
def get_ast(source_code):
    lexer = lexicon(source_code)
    parser = Parser(lexer)
    ast = parser.parse()
    return ast

def analyze(ast):
    symbol_table = SymbolTable()
    errors = []

    def visit(node):
        if isinstance(node, VariableDeclaration):
            if not symbol_table.declare(node.name, node.type):
                errors.append(f"Variable '{node.name}' redeclared.")
        elif isinstance(node, VariableReference):
            if not symbol_table.lookup(node.name):
                errors.append(f"Variable '{node.name}' not declared.")
        for child in node.children:
            visit(child)

    visit(ast)
    return errors

def generate_ir(ast):
    module = ir.Module(name="verse_module")
    function = ir.Function(module, ir.FunctionType(ir.VoidType(), []), name="main")
    block = function.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)

    def visit(node):
        if isinstance(node, VariableDeclaration):
            var = builder.alloca(ir.IntType(32), name=node.name)
            builder.store(ir.Constant(ir.IntType(32), node.value), var)
        elif isinstance(node, VariableReference):
            var = builder.load(builder.alloca(ir.IntType(32), name=node.name))
            builder.ret(var)
        for child in node.children:
            visit(child)

    visit(ast)
    builder.ret_void()
    return module

def compile_ir(module):
    llvm_ir = str(module)
    llvm_module = llvm.parse_assembly(llvm_ir)
    llvm_module.verify()

    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    with llvm.create_mcjit_compiler(llvm_module, target_machine) as ee:
        ee.finalize_object()
        ee.run_static_constructors()
        ee.run_function(llvm_module.get_function('main'), [])

# Main Kivy Application
class VerseInterpreterApp(App):
    def build(self):
        
        self.title = '* Verse Interpreter w/GUI * v1.0'
        self.icon = 'viip.png'
        self.root = BoxLayout(orientation='vertical')
        self.logger = Console_Logger()

        # Create the label with the provided text
        intro_text = """
        * Verse Interpreter w/GUI * v1.0
        A Verse programming sandbox independent of UEFN!
        Frontend & GUI by Cruz Wootten aka Lil Wikipedia
        Backend by Kariyampalli Christy & Turobin-Ort Marcel
        The interpreter was released under MIT license
        """
        self.intro_label = Label(text=intro_text, halign='center', valign='middle')
        self.intro_label.bind(size=self.intro_label.setter('text_size'))  # Ensures the text wraps within the label
        self.root.add_widget(self.intro_label)

        self.input = TextInput(hint_text='Enter text here', multiline=True)
        self.root.add_widget(self.input)

        self.output = Label(text='Output will be shown here', halign='left', valign='top')
        self.output.bind(size=self.output.setter('text_size'))  # Ensures the text wraps within the label
        self.root.add_widget(self.output)

        self.button = Button(text='Interpret')
        self.button.bind(on_press=self.on_button_press)
        self.root.add_widget(self.button)

        return self.root

    def on_button_press(self, instance):
        try:
            input_text = self.input.text
            
            ast = get_ast(input_text)
            errors = analyze(ast)
            if errors:
                self.output.text = '\n'.join(f"Error: {error}" for error in errors)
                return

            llvm_ir = generate_ir(ast)
            self.output.text = str(llvm_ir)  # Optionally print the LLVM IR
            compile_ir(llvm_ir)
            
        except Exception as e:
            self.output.text = f"Error: {str(e)}"

def verse_userinput(text):
    sys.setrecursionlimit(1000000)
    userverse = text

    lexer = lexicon(uservice)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    result = interpreter.interpret()
    return repr(result)

if __name__ == '__main__':
    VerseInterpreterApp().run()
