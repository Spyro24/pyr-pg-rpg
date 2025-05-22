"""
    simpleRuntimeStore for pyr_pg to use the pyr_pg lib
    (C) 2025 Spyro24
"""

class simpleRS:
    def __init__(self):
        self.rs = dict()
        self.lookUp = {"window": (10,13),
                        }
        
    def getById(self, id_: tuple):
        idTree = id_
        try:
            returnObj = self.rs
            for id_ in idTree:
                returnObj = returnObj[id_]
            return returnObj
        except KeyError:
            raise ValueError(f"Given ID '{idTree}' is not found in the Current RuntimeStore")
    
    def setById(self, id_: tuple):
        pass
    
    def getByName(self, name: str):
        lookUp = None
        lookName = name
        try:
            lookUp = self.lookUp[lookName]
        except KeyError:
            raise NameError(f"Given Name '{lookName}' is not found in the Current RuntimeStore")
        return self.getById(lookUp)