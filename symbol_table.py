"""
   _______     ____  __ ____   ____  _        _______       ____  _      ______ 
  / ____\ \   / /  \/  |  _ \ / __ \| |      |__   __|/\   |  _ \| |    |  ____|
 | (___  \ \_/ /| \  / | |_) | |  | | |         | |  /  \  | |_) | |    | |__   
  \___ \  \   / | |\/| |  _ <| |  | | |         | | / /\ \ |  _ <| |    |  __|  
  ____) |  | |  | |  | | |_) | |__| | |____     | |/ ____ \| |_) | |____| |____ 
 |_____/   |_|  |_|  |_|____/ \____/|______|    |_/_/    \_\____/|______|______|

"""


class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def get(self, name):
        value = self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]
