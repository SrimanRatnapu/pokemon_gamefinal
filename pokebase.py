import numpy as np         


valid_moves = {'Electric': ['Thunder', 'Thunderbolt', 'Wild Charge'],
               'Normal': ['Tail Whip', 'Quick Attack'],
               'Steel': ['Iron Tail', 'Iron Head', 'Flash Cannon']            
              }

electric_move_stats = {'Thunderbolt': {'Power': 90, 'Accuracy': 100},
                      'Thunder': {'Power': 110, 'Accuracy': 70},
                       'Wild Charge': {'Power': 90, 'Accuracy': 100}
                      }

normal_move_stats   = {'Tail Whip': {'Power': 0, 'Accuracy': 100},
                       'Quick Attack': {'Power': 40, 'Accuracy': 100}
                      }

steel_move_stats = {'Iron Tail': {'Power': 100, 'Accuracy': 75}
                   }


def identify_move_stats(name, move_type):
    if name not in valid_moves[move_type]:
        print('Error, %s not a valid move' % name)
        return None
        
    if move_type == 'Electric':
        return electric_move_stats[name]
    elif move_type == 'Normal':
        return normal_move_stats[name]
    elif move_type == 'Steel':
        return steel_move_stats[name]



class pokemon:
    
    def __init__(self, level):
        self.level = level
        self.valid_moves = {}
        
    def _stat_calculation(self):
        
        # lambda function
        stat_calc = lambda x,y: int(x/100.*y)
        
        health = self.maximum_stats['health']
        effective_health = max(stat_calc(self.level, health), 5)
        self.effective_stats['health'] = effective_health
        
        attack = self.maximum_stats['attack']
        effective_attack = max(stat_calc(self.level, attack), 5)
        self.effective_stats['attack'] = effective_attack
        
        defense = self.maximum_stats['defense']
        effective_defense = max(stat_calc(self.level, defense), 5)
        self.effective_stats['defense'] = effective_defense
        
        
        
    def add_move(self, name=None):
        if len(self.moves.keys()) == 4:
            print('Error, can only have 4 moves maximum')
            return
        
        if name in self.valid_moves:
            self.moves[name] = self.valid_moves[name]
        else:
            print('Error, move name %s not a valid move' % name)
        
        
        
        
        
