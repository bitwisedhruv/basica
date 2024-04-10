"""
  _____ __  __ _____   ____  _____ _______ _____ 
 |_   _|  \/  |  __ \ / __ \|  __ \__   __/ ____|
   | | | \  / | |__) | |  | | |__) | | | | (___  
   | | | |\/| |  ___/| |  | |  _  /  | |  \___ \ 
  _| |_| |  | | |    | |__| | | \ \  | |  ____) |
 |_____|_|  |_|_|     \____/|_|  \_\ |_| |_____/ 

"""

from symbol_table import SymbolTable
from context import Context
from lexer import Lexer
from basica_parser import Parser
from values import Number, BuiltInFunction

# from basica_interpreter import Interpreter


"""
  _____  _    _ _   _ 
 |  __ \| |  | | \ | |
 | |__) | |  | |  \| |
 |  _  /| |  | | . ` |
 | | \ \| |__| | |\  |
 |_|  \_\\____/|_| \_|

"""

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number.null)
global_symbol_table.set("true", Number.true)
global_symbol_table.set("false", Number.false)
global_symbol_table.set("print", BuiltInFunction.print)
global_symbol_table.set("printRet", BuiltInFunction.print_ret)
global_symbol_table.set("input", BuiltInFunction.input)
global_symbol_table.set("inputInt", BuiltInFunction.input_int)
global_symbol_table.set("clear", BuiltInFunction.clear)
global_symbol_table.set("cls", BuiltInFunction.clear)
global_symbol_table.set("isNum", BuiltInFunction.is_number)
global_symbol_table.set("isStr", BuiltInFunction.is_string)
global_symbol_table.set("isList", BuiltInFunction.is_list)
global_symbol_table.set("isFunc", BuiltInFunction.is_func)
global_symbol_table.set("append", BuiltInFunction.append)
global_symbol_table.set("pop", BuiltInFunction.pop)
global_symbol_table.set("extend", BuiltInFunction.extend)
global_symbol_table.set("len", BuiltInFunction.len)
global_symbol_table.set("run", BuiltInFunction.run)


def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error

    # Run program
    from basica_interpreter import Interpreter

    interpreter = Interpreter()
    context = Context("<program>")
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error
