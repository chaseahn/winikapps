
import json
import csv
import requests



TEAM = "Nuggets"


def schedule():
    with open('schedule.json', 'r') as f:
        schedule = json.load(f)
        return schedule


def create_team_schedule(TEAM):

    games = schedule()
    events, g_id = {}, 0

    for key in games.keys():

        group = ["Hawks","Knicks","Bulls", "Pelicans", "Nuggets", "Grizzlies"]

        if TEAM == games[key]['home'] and games[key]['away'] is in group:
            events[g_id] = games[key]
            g_id += 1
        else:
            pass

    csv_columns = events[0].keys()


    try:
        with open('./csv/{}-Schedule-19-20.csv'.format(TEAM), 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for key in events.keys():
                try:
                    writer.writerow(events[key])
                except TypeError as e:
                    print e
                    print data
                    break

    except IOError as e:
        print e


create_team_schedule(TEAM)