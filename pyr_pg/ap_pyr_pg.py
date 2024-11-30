import pygame as p

class argparse():
    def __init__(self, global_config):
        self.args = global_config["ap_config"]
        self.params = self.args.keys()
    
    def set(self, args_list):
        pass
    
    def get(self, arg):
        pass
    
    def get_names(self):
        names = []
        
    def argparse_config(self):
        names = {"ArgTest":["int 1:100:10"], "ArgBool":"bool"}
        return names

if __name__ == "__main__":
    TestConfig = {"ap_config":{}}
    TestModule = argparse(TestConfig)