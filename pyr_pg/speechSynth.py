import pygame as p

class tokenizerSystem:
    def __init__(self, tokenTable):
        self.begins = tokenTable[0]
        self.mids = tokenTable[1]
        self.ends = tokenTable[2]
        self.onetokens = tokenTable[3]
        
    def returnTokens(self, string: str) -> list[tuple]:
        
    

class speechSynth:
    def __init__(self, sampleFolder, tokenizer: tokenizerSystem):
        self.__tokenizer = tokenizer
        

if __name__ == "__main__": #Unit test
    tokenizer = tokenizerSystem([[],["ll"],[],["ist", "ein"]])