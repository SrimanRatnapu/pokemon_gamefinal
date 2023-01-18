import sys
sys.path.append('../pokemon_classes')

import numpy as np
from pokemon_classes.pokemons import *
from combat import perform_move
import pypokedex
import pokepy


class NaiveTrainer(object):
    
    def __init__(self, name):
        self.name = name
        self.pokemons = {}
        self.pokemon_status = {}
        self.battling_pokemon = None
        
        
    def add_pokemon(self, name, level=100):
        if len(self.pokemons) == 6:
            return
        p = getattr(sys.modules[__name__], name)(level)
        
        moves = p.valid_moves
        move_keys = list(moves.keys())
        move_counter = (np.arange(0,len(moves)))
        np.random.shuffle(move_counter)
        rnd_move_choices = move_counter[:4]
        
        for rnd in rnd_move_choices:
            p.add_move(move_keys[rnd])
        self.pokemons[name] = p
        self.pokemon_status[name] = 1
        
        
    def choose_pokemon(self):
#         poke_status_vals = list(self.pokemon_status.values())
#         if set(poke_status_vals) == {0}:
#             print("Trainer %s is out of pokemon and has lost the match" % self.name
#             return
        
        chosen = False
        chosen_name = None
        npokemon = len(self.pokemons)
        poke_names = list(self.pokemons.keys())
        while not chosen:
            if npokemon == 1:
                rnd_choice = 0
            else:
                rnd_choice = np.random.randint(0,npokemon)
            chosen_name  = poke_names[rnd_choice]
            if self.pokemon_status[chosen_name]: chosen = True
        self.battling_pokemon = self.pokemons[chosen_name]
        print("Trainer %s has chosen %s" % (self.name, self.battling_pokemon.name))
        
        
    def choose_move(self):
        move_rnd = np.random.randint(0, 4)
        move_lst = list(self.battling_pokemon.moves.keys())
        move_name = move_lst[move_rnd]
        return move_name
        
        
    def pokemon_attack(self, defending_trainer):
        move_rnd = np.random.randint(0, 4)
        move_lst = list(self.battling_pokemon.moves.keys())
        move_name = move_lst[move_rnd]
        print(move_name)
        
        attacking_pokemon = self.battling_pokemon
        defending_pokemon = defending_trainer.battling_pokemon
        perform_move(attacking_pokemon, defending_pokemon, move_name)
        if defending_pokemon.current_hp <= 0:
            print(defending_pokemon.name, "has fainted!")
            defending_trainer.pokemon_status[defending_pokemon.name] = 0
            defending_trainer.battling_pokemon = None
            defending_trainer.choose_pokemon()
 
            
        