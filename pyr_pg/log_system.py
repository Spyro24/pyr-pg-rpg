import time

class log():
    def __init__(self):
        self.content = []
        self.printOut = False
        
    def insert(self, *strings):
        MaxCounter = len(strings)
        for string in strings:
            self.content.append(string)
            if self.printOut:
                print(string)
            
    def WriteLog(self, path="./", name=str(time.time()) + ".txt"):
        LogFile = open(path + name, "w")
        for line in self.content:
            LogFile.write(str(line) + "\n")
        
if __name__ == "__main__":
    test = log()
    test.insert(1,2,3,4,5,6,7,8)