"""
    first fightsystem for pyr_pg
    (c) 2025 Spyro24
"""

class fightSystem:
    def __init__(self, runtimestore):
        pass
    
    def start_fight(self, enemies: list):
        pass
    
    def _eval_enemie_pos(self, enemie_amount: int):
        eval_pos = (((1,2)),
                    ((1,1),(1,3)),
                    ((1,1),(1,2),(1,3)),
                    ((1,1),(0,2),(2,2),(1,3)),
                    ((0,1),(2,1),(1,2),(0,3),(2,3)),
                    ((0,0),(2,0),(0,2),(2,2),(0,4),(2,4)),
                    ((1,0),(0,1),(2,1),(1,2),(0,3),(2,3),(1,4)),
                    ((0,0),(0,2),(1,1),(0,2),(2,2),(1,3),(0,4),(2,4)))
        if 0 < enemie_amount <= 8:
            return eval_pos[enemie_amount + 1]
        elif enemie_amount > 8:
            return eval_pos[7]
        else:
            return ((-1,-1))
        
class enemie:
    def __init__(self, config: tuple(int, int)):
        self.health = config[0]
        self.resistence = config[1]
        
    def is_alive(self):
        if self.health <= 0:
            return True
        return False
        