class debug_log():
    def __init__(self, debug):
        self.debug_state = debug
        self.debug_log = []
    
    def print(self, msg):
        self.debug_log.append(msg)
        