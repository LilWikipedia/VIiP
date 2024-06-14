# llvm_generator.py

import llvmlite.ir as ir
import llvmlite.binding as llvm

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

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
            var = builder.load(node.name)
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
