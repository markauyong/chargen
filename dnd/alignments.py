#! python3

alignments = {
    0:  { "alignment" : "Lawful Good"},
    1:  { "alignment" : "Neutral Good"},
    2:  { "alignment" : "Chaotic Good"},
    3:  { "alignment" : "Lawful Neutral"},
    4:  { "alignment" : "Neutral"},
    5:  { "alignment" : "Chaotic Neutral"},
    6:  { "alignment" : "Lawful Evil"},
    7:  { "alignment" : "Neutral Evil"},
    8:  { "alignment" : "Chaotic Evil"},
}


def alignment_list():
    alignment_list = []

    for i in range(len(alignments)):
        alignment_list.append(alignments[i]["alignment"])

    return alignment_list
