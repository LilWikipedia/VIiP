from verse_linter import get_ast
from semantic_analyzer import analyze
from llvm_generator import generate_ir, compile_ir

def main(source_code):
    ast = get_ast(source_code)
    errors = analyze(ast)
    if errors:
        for error in errors:
            print(f"Error: {error}")
        return

    llvm_ir = generate_ir(ast)
    print(llvm_ir)  # Optionally print the LLVM IR
    compile_ir(llvm_ir)

if __name__ == "__main__":
    source_code = """
    int x = 10;
    int y = x + 20;
    """
    main(source_code)
