#! python3

races = {
    0:  { "race" : "Dwarf",
        "subrace" : "Hill",
        "abilityModifier" : {'wis': 1, 'con': 2 },
        "size" : "M",
        "speed": 25,
        "darkVision": 60,
        },
    1:  { "race" : "Dwarf",
        "subrace" : "Mountain",
        "abilityModifier" : {'str': 2, 'con': 2 },
        "size" : "M",
        "speed": 25,
        "darkVision": 60,
        },
    2:  { "race" : "Elf",
        "subrace" : "High",
        "abilityModifier" : {'int': 1, 'dex': 2 },
        "size" : "M",
        "speed" : 30,
        "darkVision": 60,
        },
    3:  { "race" : "Elf",
        "subrace" : "Wood",
        "abilityModifier" : {'wis': 1, 'dex': 2 },
        "size" : "M",
        "speed" : 30,
        "darkVision": 60,
        },
    4:  { "race" : "Elf",
        "subrace" : "Dark",
        "abilityModifier" : {'dex': 2, 'cha': 1 },
        "size" : "M",
        "speed" : 30,
        "darkVision": 120,
        },
    5:  { "race" : "Halfling",
        "subrace" : "Lightfoot",
        "abilityModifier" : {'dex': 2, 'cha': 1 },
        "size" : "S",
        "speed" : 25,
        },
    6:  { "race" : "Halfling",
        "subrace" : "Stout",
        "abilityModifier" : {'dex': 2, 'con': 1 },
        "size" : "S",
        "speed" : 25,
        },
    7:  { "race" : "Human",
        "abilityModifier" : {'str': 1, 'int': 1, 'wis': 1, 'dex': 1, 'con': 1, 'cha': 1 },
        "size" : "M",
        "speed" : 30,
        },
    8:  { "race" : "Dragonborn",
        "abilityModifier" : {'str': 2, 'cha': 1 },
        "size" : "M",
        "speed" : 30,
        },
    9:  { "race" : "Gnome",
        "subrace" : "Forest",
        "abilityModifier" : {'int': 2, 'dex': 1 },
        "size" : "M",
        "speed" : 25,
        "darkVision:": 60,
        },
    10: { "race" : "Gnome",
        "subrace" : "Rock",
        "abilityModifier" : {'int': 2, 'con': 1 },
        "size" : "M",
        "speed" : 25,
        "darkVision:": 60,
        },
    11: { "race" : "Half-Elf",
         "abilityModifier" : {'str': 0, 'int': 0, 'wis': 0, 'dex': 0, 'con': 0, 'cha': 2 },
        "size" : "M",
        "speed" : 30,
        "darkVision:": 60,
        },
    12: {
        "race" : "Half-Orc",
        "abilityModifier" : {'str': 2, 'con': 1 },
        "size" : "M",
        "speed" : 30,
        "darkVision:": 60,
        },
    13: { "race" : "Tiefling",
        "abilityModifier" : {'int': 1, 'cha': 2 } ,
        "size" : "M",
        "speed" : 30,
        "darkVision:": 60,
        },
}

def full_race_name(raceID):
    if raceID < 0 or raceID >= len(races):
        return None

    if 'subrace' in races[raceID]:
        raceName = races[raceID]['subrace'] + " " + races[raceID]['race']
    else:
        raceName = races[raceID]['race']

    return raceName

def race_list():
    race_list = []

    for i in range(len(races)):
        race_list.append(full_race_name(i))

    return race_list
