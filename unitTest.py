"""
    This is the unit test system.
    It contains the unit test for every PYR_PG module
    (c) 2025 Spyro24
"""
import pygame as p
import pyr_pg
import runtime_store as rs

class testing:
    def __init__(self, pygameWindow, logSystem, font):
        self.runtimeStore = {}
        self.runtimeStore[rs.FontSystem] = font
        self.runtimeStore[rs.LogSystem] = logSystem
        self.runtimeStore[rs.Window] = pygameWindow
        self.font = font
        self.log = logSystem
        
    def runTests(self) -> bool:
        self.testDialogSystem()
        self.testFont()
    
    def testFont(self) -> bool:
        self.log(1, "[unitTest] Font unit test...")
        try:
            testElement = self.font
            testElement.draw("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890", 10, (0,0))
        except BaseException as err:
            self.log(1, "[unitTest] Font unit test [FAIL]", err)
            return False
        self.log(1, "[unitTest] Font unit test [PASS]")
        return True
    
    def testDialogSystem(self) -> bool:
        self.log(1, "[unitTest] DialogSystem unit test...") 
        try:
            testElement = pyr_pg.DialogHandler.DialogScript(self.runtimeStore)
            testElement.execDialogScript("./res/unitTests/unitTest.dls")
        except BaseException as err:
            self.log(1, "[unitTest] DialogSystem unit test [FAIL]", err)
            return False
        self.log(1, "[unitTest] DialogSystem unit test [PASS]")
        return True

if __name__ == "__main__":
    testWindow = p.display.set_mode((1080, 720))
    logSystem  = pyr_pg.log_system.log()
    fontSystem = pyr_pg.font.font(testWindow, "./res/fonts/standard")
    testSystem = testing(testWindow, logSystem.insert, fontSystem)
    testSystem.runTests()
    logSystem.WriteLog(name="unitTestLog.txt")
    p.display.flip()