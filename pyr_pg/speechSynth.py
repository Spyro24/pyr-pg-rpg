import pygame as p

class tokenizerSystem:
    def __init__(self, tokenTable):
        self.begins = tokenTable[0]
        self.mids = tokenTable[1]
        self.ends = tokenTable[2]
        self.onetokens = tokenTable[3]
        
    def returnTokens(self, string: str) -> list[tuple]:
        string = string.lower()
        rawTokens = string.split(" ")
        tokens = []
        for token in rawTokens:
            if self.onetokens.count(token):
                tokens.append((token, 3))
                rawTokens[rawTokens.index(token)] = None
            else:
                tokens.append(None)
        for token in rawTokens:
            if rawTokens[rawTokens.index(token)] != None:
                index = rawTokens[rawTokens.index(token)]
                curToken = token
        return tokens
    

class speechSynth:
    def __init__(self, sampleFolder, tokenizer: tokenizerSystem):
        self.__tokenizer = tokenizer
        

if __name__ == "__main__": #Unit test
    tokenizer = tokenizerSystem([["wi"],["ll","ko"],["men"],["ist", "ein", "an"]])
    print(tokenizer.returnTokens(input("Input a string > ")))
    