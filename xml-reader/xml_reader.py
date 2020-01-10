
import os
import csv

from bs4 import BeautifulSoup

PATH = "/Users/ahn.ch/Desktop/ep1.xml"
CSV_NAME = './csv/Episode4EDL.csv'

class XML():

    def __init__(self):
        self.path = PATH

    def parse(self):

        with open(self.path, "r") as f:

            contents = f.read()

            soup = BeautifulSoup(contents, 'lxml')

            clips = soup.find_all('clipitem')

            for clip in clips:
                
                names = clip.find_all('name')
                duration = clip.find('duration')


                print clip.find('duration')
                break

    

if __name__ == "__main__":
    x = XML()
    x.parse()

