"""
   _____ ____  _   _ _______ ________   _________ 
  / ____/ __ \| \ | |__   __|  ____\ \ / /__   __|
 | |   | |  | |  \| |  | |  | |__   \ V /   | |   
 | |   | |  | | . ` |  | |  |  __|   > <    | |   
 | |___| |__| | |\  |  | |  | |____ / . \   | |   
  \_____\____/|_| \_|  |_|  |______/_/ \_\  |_|   

"""


class Context:
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = None
