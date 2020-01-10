

import json

from bs4 import BeautifulSoup


def soup():
    soup = BeautifulSoup(open('games.html'), 'html.parser')
    return soup


def create_schedule(soup):

    schedule, game_id = {}, 0

    games = soup.find_all('table', {'class' : 'imspo_mt__mit'})

    for game in games:

        print(game.text)
        break

        date = game.find('div', {
            'class': 'imspo_mt__pm-inf imspo_mt__date imso-medium-font'
            }).text
        time = game.find('div', {
            'class': 'imspo_mt__ndl-p imspo_mt__pm-inf imso-medium-font'
            }).text

        away = game.find_all('div', {'class' : 'ellipsisize'})[0].text
        home = game.find_all('div', {'class' : 'ellipsisize'})[1].text
        
        schedule[game_id] = {
            "date": date,
            "time": time,
            "away": away,
            "home": home
        }

        game_id += 1

    with open('schedule.json', 'w') as outfile:  
        json.dump(schedule, outfile, indent=4)




if __name__ == "__main__":
    create_schedule(soup())