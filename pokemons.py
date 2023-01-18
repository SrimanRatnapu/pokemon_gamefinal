from pokebase import pokemon
import pypokedex
import pokepy


def get_valid_moves(name):
    valid_moves = {}
    client = pokepy.V2Client()
    pokemon = pypokedex.get(name=name)
    for move in pokemon.moves['yellow']:
        move_name = move.name
        pymove = client.get_move(move_name)[0]
        power  = pymove.power
        accuracy = pymove.accuracy
        move_type = pymove.type.name
        
        if accuracy is None: accuracy = 100
        if power is None: power = 0.0
            
        valid_moves[move_name] = {'Power': power, 'Accuracy': accuracy, 'Type': move_type}
    return valid_moves


class Pikachu(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.name = 'Pikachu'
        self.moves = {}
        self.type = ['electric']
        self.maximum_stats   = {'health': 35, 'attack': 55, 'defense': 40, 'speed' : 90}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        self.valid_moves = get_valid_moves('Pikachu')
        
        
        
class Bulbasaur(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.name = 'Bulbasaur'
        self.moves = {}
        self.type = ['grass', 'poison']
        self.maximum_stats   = {'health': 45, 'attack': 49, 'defense': 49, 'speed': 45}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        self.valid_moves = get_valid_moves('Bulbasaur')

        
class Ivysaur(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.name = 'Ivysaur'
        self.moves = {}
        self.type = ['grass', 'poison']
        self.maximum_stats   = {'health': 60, 'attack': 62, 'defense': 63, 'speed': 45}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        self.valid_moves = get_valid_moves('Ivysaur')
    
class Venusaur(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.name = 'Venasaur'
        self.moves = {}
        self.type = ['grass', 'poison']
        self.maximum_stats   = {'health': 80, 'attack': 82, 'defense': 83, 'speed': 80}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        self.valid_moves = get_valid_moves('Venusaur')

        
class Charmander(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.name = 'Charmander'
        self.moves = {}
        self.type = ['fire']
        self.maximum_stats   = {'health': 39, 'attack': 52, 'defense': 43, 'speed' : 65}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        self.valid_moves = get_valid_moves('Charmander')
        
class Charmeleon(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.name = 'Charmeleon'
        self.moves = {}
        self.type = ['fire']
        self.maximum_stats   = {'health': 58, 'attack': 64, 'defense': 58, 'speed' : 80}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        self.valid_moves = get_valid_moves('Charmeleon')
        
class Charizard(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.name = 'Charizard'
        self.moves = {}
        self.type = ['fire', 'flying']
        self.maximum_stats   = {'health': 78, 'attack': 84, 'defense': 78, 'speed' : 100}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        self.valid_moves = get_valid_moves('Charizard')
        

class Squirtle(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.name = 'Squirtle'
        self.moves = {}
        self.type = ['water']
        self.maximum_stats   = {'health': 44, 'attack': 48, 'defense': 65, 'speed' : 43}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        self.valid_moves = get_valid_moves('Squirtle')
        
class Wartortle(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.name = 'Wartortle'
        self.moves = {}
        self.type = ['water']
        self.maximum_stats   = {'health': 59, 'attack': 63, 'defense': 80, 'speed' : 58}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        self.valid_moves = get_valid_moves('Wartortle')
        
class Blastoise(pokemon):
    
    def __init__(self, level):
        super().__init__(level)
        self.name = 'Blastoise'
        self.moves = {}
        self.type = ['water']
        self.maximum_stats   = {'health': 79, 'attack': 83, 'defense': 100, 'speed' : 78}
        self.effective_stats = {'health': None, 'attack': None, 'defense': None}
        self._stat_calculation()
        self.current_hp = self.effective_stats['health']
        self.alive = True
        self.valid_moves = get_valid_moves('Blastoise')

        