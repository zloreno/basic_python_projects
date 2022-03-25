from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = '/prod/v1/today.json'


printer = PrettyPrinter()


def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    return data['links']


def get_scorebord(links):
    scorebord = links['currentScoreboard']
    scoreboard = get(BASE_URL + scorebord).json()
    games = scoreboard['games']
    for game in games:
        home_team = game['hTeam']
        visiting_team = game['vTeam']
        clock = game['clock']
        period = game['period']
        print('--------------------------------------------------------')
        print(f'{home_team["triCode"]} vs {visiting_team["triCode"]}')
        print(
            f'{home_team["score"] or "-" } - {visiting_team["score"] or "-"}')
        print(f'{clock} : Q {period["current"]} ')


def get_stats(links):
    starts_link = links['leagueTeamStatsLeaders']
    stats = get(BASE_URL + starts_link).json()
    teams = stats['league']['standard']['regularSeason']['teams']

    teams = [team for team in teams if team['name'] != "Team"]
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    i = 1
    for team in teams:
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']
        print(f'{i}. {name} - {nickname}: {ppg["avg"]}')
        i += 1


links = get_links()
get_scorebord(links)
get_stats(links)
