
import numpy as np

type_order = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water',
             'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']

multiplier_index = [
                    [1, 1, 1 ,1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5], 
                    [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],
                    [1,1,1,0.5,0.5,0.5,1,0.5,0,1,1,2,1,1,1,1,1,2],
                    [1,1,0,2,1,2,0.5,1,2,2,1,0.5,2,1,1,1,1,1], 
                    [1,0.5,2,1,0.5,1,2,1,0.5,2,1,1,1,1,2,1,1,1],
                    [1,0.5,0.5,0.5,1,1,1,0.5,0.5,0.5,1,2,1,2,1,1,2,0.5],
                    [0,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,1],
                    [1,1,1,1,1,2,1,1,0.5,0.5,0.5,1,0.5,1,2,1,1,2],
                    [1,1,1,1,1,0.5,2,1,2,0.5,0.5,2,1,1,2,0.5,1,1],
                    [1,1,1,1,2,2,1,1,1,2,0.5,0.5,1,1,1,0.5,1,1],
                    [1,1,0.5,0.5,2,2,0.5,1,0.5,0.5,2,0.5,1,1,1,0.5,1,1],
                    [1,1,2,1,0,1,1,1,1,1,2,0.5,0.5,1,1,0.5,1,1],
                    [1,2,1,2,1,1,1,1,0.5,1,1,1,1,0.5,1,1,0,1],
                    [1,1,2,1,2,1,1,1,0.5,0.5,0.5,2,1,1,0.5,2,1,1,],
                    [1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,2,1,0],
                    [1,0.5,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,0.5],
                    [1,2,1,0.5,1,1,1,1,0.5,0.5,1,1,1,1,1,2,2,1]     
                ]
def damage_multiplier(attack_type, defend_types):
    total_multiplier = 1
    attack_index = type_order.index(attack_type)
    for defend_type in defend_types:
        defend_index = type_order.index(defend_type)
        total_multiplier *= multiplier_index[attack_index][defend_index]
    return total_multiplier
    


def damage_calculation(level, move_power, self_attack, target_defense):
    ad = self_attack / target_defense
    dmg = 2. + ( 0.4 * level * move_power * ad) / 50.
    return round(dmg)

def perform_move(attacking_pokemon, defending_pokemon, move):
    # check if move is valid
    # include randomness because accuracy may not be 100'
    if move not in attacking_pokemon.moves:
        print("Move not valid")
        return 0
    move_hit = np.random.uniform(0,100)
    if move_hit > attacking_pokemon.moves[move]['Accuracy']:
        print("Move missed!")
        return 0
    
    # Get miltiplier here
    dmg_multiplier = damage_multiplier(attacking_pokemon.moves[move]['Type'], defending_pokemon.type)   
    move_damage = damage_calculation(attacking_pokemon.level, attacking_pokemon.moves[move]['Power'], attacking_pokemon.effective_stats['attack'], defending_pokemon.effective_stats['defense'])
    effective_move_damage = move_damage * dmg_multiplier
    defending_pokemon.current_hp -= effective_move_damage
    return 1
    
    
    