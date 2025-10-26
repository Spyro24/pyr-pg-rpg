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
        self.dependencies = pyr_pg.dependecies.dependcies()
        self.dependencies.add(font, "/system/font")
        self.dependencies.add(logSystem, "/system/log")
        self.dependencies.add(pygameWindow, "/window")
        self.dependencies.add(pyr_pg.sound.sound("./res/audio/"), "/system/sound") 
        self.runtimeStore = {}
        self.runtimeStore[rs.FontSystem] = font
        self.runtimeStore[rs.LogSystem] = logSystem
        self.runtimeStore[rs.Window] = pygameWindow
        self.font = font
        self.log = logSystem
        self.testCounter = 0
        
    def runTests(self) -> bool:
        self.testDialogSystem()
        self.testFont()
        self.testPerlinNoise()
    
    def testFont(self) -> bool:
        self.log("[unitTest] Font unit test...")
        try:
            testElement = self.font
            testElement.draw("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890", 14, (0,0))
        except BaseException as err:
            self.log("[unitTest] Font unit test [FAIL]", err)
            return False
        self.log("[unitTest] Font unit test [PASS]")
        return True
    
    def testDialogSystem(self) -> bool:
        self.self_onTestStartMessage("DialogSystem")
        try:
            testElement = pyr_pg.DialogHandler.DialogScript(self.dependencies)
            testElement.execDialogScript("./res/unitTests/unitTest.dls")
        except BaseException as err:
            self.log("[unitTest] DialogSystem unit test [FAIL]", f"Failed with: {err}")
            return False
        self.log("[unitTest] DialogSystem unit test [PASS]")
        return True
    
    def testPerlinNoise(self):
        self.self_onTestStartMessage("PerlinNoise")
        noiseTest = pyr_pg.math_.PerlinNoise2D(seed=24375)
        testValues = {(0,0):0.5, (5.5,5.5):0.25, (100.1,100.1):0.5076380537599988}
        try:
            for key in testValues.keys():
                if not  noiseTest.noise(key[0], key[1]) == testValues[key]:
                    raise ValueError("noise Value mismatch")
        except ValueError:
            self.log("[unitTest] PerlinNoise unit test [FAIL]", err)
            return False
        self.log("[unitTest] PerlinNoise unit test [PASS]")
    
    def self_onTestStartMessage(self, testName: str):
        self.testCounter += 1
        self.log(f"[unitTest] {testName} unit test [....] (Test No. {self.testCounter})")

if __name__ == "__main__":
    window = p.display.set_mode((1080, 720))
    logSystem  = pyr_pg.log_system.log()
    fontSystem = pyr_pg.font.font(window, "./res/fonts/standard")
    testSystem = testing(window, logSystem.insert, fontSystem)
    testSystem.runTests()
    logSystem.WriteLog(name="unitTestLog.txt")
    p.display.flip()
    