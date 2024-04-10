"""
  _____        _____   _____ ______   _____  ______  _____ _    _ _   _______ 
 |  __ \ /\   |  __ \ / ____|  ____| |  __ \|  ____|/ ____| |  | | | |__   __|
 | |__) /  \  | |__) | (___ | |__    | |__) | |__  | (___ | |  | | |    | |   
 |  ___/ /\ \ |  _  / \___ \|  __|   |  _  /|  __|  \___ \| |  | | |    | |   
 | |  / ____ \| | \ \ ____) | |____  | | \ \| |____ ____) | |__| | |____| |   
 |_| /_/    \_\_|  \_\_____/|______| |_|  \_\______|_____/ \____/|______|_|   

"""


class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None
        self.last_registered_advance_count = 0
        self.advance_count = 0
        self.to_reverse_count = 0

    def register_advancement(self):
        self.last_registered_advance_count = 1
        self.advance_count += 1

    def register(self, res):
        self.last_registered_advance_count = res.advance_count
        self.advance_count += res.advance_count
        if res.error:
            self.error = res.error
        return res.node

    def try_register(self, res):
        if res.error:
            self.to_reverse_count = res.advance_count
            return None
        return self.register(res)

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        if not self.error or self.last_registered_advance_count == 0:
            self.error = error
        return self
