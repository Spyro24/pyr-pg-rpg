import time

class log():
    def __init__(self):
        self.content = []
        
    def insert(self, *strings):
        PrintOut   = False
        Counter    = 0
        MaxCounter = len(strings)
        if strings[0] == 1:
            PrintOut = True
            Counter  = 1
        while Counter < MaxCounter:
            self.content.append(strings[Counter])
            if PrintOut:
                print(strings[Counter])
            Counter += 1
            
    def WriteLog(self, path="./", name=str(time.time()) + ".txt"):
        LogFile = open(path + name, "w")
        for line in self.content:
            LogFile.write(str(line) + "\n")
        
if __name__ == "__main__":
    test = log()
    test.insert(1,2,3,4,5,6,7,8)