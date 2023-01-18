import sys
sys.path.append('../pokemon_classes')

from pokemon_classes.pokemons import *
from trainer import NaiveTrainer
from combat import perform_move


class Battle():
    
    
    def __init__(self, trainerA, trainerB):
        
        self.trainerA = trainerA
        self.trainerB = trainerB
        self.gameOver = 0 # If 1, then game is over
        
    def _game_check(self, trainer):
        # trainer.pokemon_status
        poke_status_vals = list(trainer.pokemon_status.values())
        if set(poke_status_vals) == {0}:
            print("Trainer %s is out of pokemon and has lost the match" % trainer.name)
            self.gameOver = 1
            
            
    def _speed_check(self, pA, pB):
        sA = pA.maximum_stats['speed']
        sB = pB.maximum_stats['speed']
        if sA >= sB:
            return "A"
        else:
            return "B"
    

    def run_battle(self):
        self.trainerA.choose_pokemon()
        self.trainerB.choose_pokemon()
        current_move = None
        while not self.gameOver:
            # logic for battle
            if current_move is None:
                current_move = self._speed_check(self.trainerA.battling_pokemon, self.trainerB.battling_pokemon)
             
            attacking_trainer = None
            defending_trainer = None
            if current_move == "A":
                attacking_trainer = self.trainerA
                defending_trainer = self.trainerB
            else:
                attacking_trainer = self.trainerB
                defending_trainer = self.trainerA
            
            poke_move = attacking_trainer.choose_move()
            print("%s's %s will perform %s" % (attacking_trainer.name, attacking_trainer.battling_pokemon.name, poke_move))
            perform_move(attacking_trainer.battling_pokemon, defending_trainer.battling_pokemon, poke_move)
            if defending_trainer.battling_pokemon.current_hp <= 0:
                print(defending_trainer.battling_pokemon.name, "has fainted!")
                defending_trainer.pokemon_status[defending_trainer.battling_pokemon.name] = 0
                defending_trainer.battling_pokemon = None
                
                self._game_check(defending_trainer)
                if self.gameOver:
                    return
                defending_trainer.choose_pokemon()
                current_move = None
            else:
                if current_move == "A":
                    current_move = "B"
                else:
                    current_move = "A"
               
        return
        
    