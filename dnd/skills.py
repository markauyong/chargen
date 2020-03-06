#! python3

skills = {
    0:  { "skill" : "Acrobatics", "ability" : "dex"},
    1:  { "skill" : "Animal Handling", "ability" : "wis"},
    2:  { "skill" : "Arcana", "ability" : "int"},
    3:  { "skill" : "Athletics", "ability" : "str"},
    4:  { "skill" : "Deception", "ability" : "cha"},
    5:  { "skill" : "History", "ability" : "int"},
    6:  { "skill" : "Insight", "ability" : "wis"},
    7:  { "skill" : "Intimidation", "ability" : "cha"},
    8:  { "skill" : "Investigation", "ability" : "int"},
    9:  { "skill" : "Medicine", "ability" : "wis"},
    10: { "skill" : "Nature", "ability" : "int"},
    11: { "skill" : "Perception", "ability" : "wis"},
    12: { "skill" : "Performance", "ability" : "cha"},
    13: { "skill" : "Persuasion", "ability" : "cha"},
    14: { "skill" : "Religion", "ability" : "int"},
    15: { "skill" : "Sleight of Hand", "ability" : "dex"},
    16: { "skill" : "Stealth", "ability" : "dex"},
    17: { "skill" : "Survival", "ability" : "wis"},
}


def skill_list():
    skill_list = []

    for i in range(len(skills)):
        alignment_list.append(skills[i]["skill"])

    return skill_list
