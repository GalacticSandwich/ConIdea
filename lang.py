
from random import choice

lang_groups = [
    'a family',
    'a group',
    'a clan',
    'a handful of clans',
    'a group of clans',
    'clans',
    'a tribe',
    'a handful of tribes',
    'a group of tribes',
    'tribes',
    'a tribal federation',
    'a small village',
    'a kingdom',
    'a group of kingdoms',
    'kingdoms',
    'a city-state',
    'a group of city-states',
    'city-states',
    'a classical republic',
    'a democracy',
    'a democratic republic'
]

lang_locations = [
    'in a flat plain',
    'in a grassland',
    'in a tropical rainforest',
    'in a tropical dry forest',
    'in a swampy marsh',
    'in a coastal plain',
    'in a snowy tundra',
    'in a taiga',
    'in a sandy desert'
    'in a chaparral',
    'in a river-valley',
    'in a fertile crescent',
    'along a coast',
    'along a river',
    'along a mountain chain',
    'around a small lake',
    'around a large lake',
    'on a peninsula',
    'on a desert island',
    'on a group of scattered islands'
]

# generate a random description of a language
def get_language():
    # response string builder
    builder = ''

    # describe the people that speak it, and where they live
    builder = builder + f'This language is spoken by the people of '
    builder = builder + f'{ choice( lang_groups ) } { choice( lang_locations ) }\n'

    return builder
