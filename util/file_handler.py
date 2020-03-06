#! python3

import sys
sys.path.append('../')

import pickle
import dnd.character

def save_to_file(filename, object):
    with open(filename, 'wb') as outfile:
        pickle.dump(object, outfile, pickle.HIGHEST_PROTOCOL)

def load_from_file(filename):
    loaded_object = None

    with open(filename, 'rb') as infile:
        loaded_object = pickle.load(infile)

    return loaded_object
