

import json

from bs4 import BeautifulSoup


PATH = ' '



def soup():
    soup = BeautifulSoup(PATH, 'html.parser')
    return soup