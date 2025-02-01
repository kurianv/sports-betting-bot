import requests
import datetime as dt
import tools

API_KEY = '775066093bd2fa6d1186873299127d79'
sport = 'basketball_nba'
market = 'us2'
betType = 'h2h'
oddsformat = 'american'
until = str(dt.date.today()) + "T11:59:59Z"


#request
sports_data = requests.get(f'https://api.the-odds-api.com/v4/sports/{sport}/odds/?apiKey={API_KEY}&regions={market}&markets={betType}')

#game details
def game_odds():
  for i in range(len(sports_data.json())):
    sport_name = sports_data.json()[i]['sport_key']
    underIndex  = sport_name.find("_") +1
    home = sports_data.json()[i]['home_team']
    away = sports_data.json()[i]['away_team']
    print(f'{(i+1)} {home} v. {away}: {(sport_name[underIndex:]).upper()}')
    for j in range(len(sports_data.json()[i]['bookmakers'])):
      print(f"Bookmaker: {sports_data.json()[i]['bookmakers'][j]['title']} with odds:")
      for k in range(len(sports_data.json()[i]['bookmakers'][j]['markets'][0]['outcomes'])):
        print(f"{sports_data.json()[i]['bookmakers'][j]['markets'][0]['outcomes'][k]['name']}: {(sports_data.json()[i]['bookmakers'][j]['markets'][0]['outcomes'][k]['price'])}")
      print("\n")


def feasibleBets():
  results = []
  odds = {}
  emailBody = ""
  for i in range(len(sports_data.json())):
    for j in range(len(sports_data.json()[i]['bookmakers'])):
      for k in range(len(sports_data.json()[i]['bookmakers'][j]['markets'][0]['outcomes'])):
        name = sports_data.json()[i]['bookmakers'][j]['markets'][0]['outcomes'][k]['name']
        if name not in odds.keys():
          odds[name] = {}
        price = sports_data.json()[i]['bookmakers'][j]['markets'][0]['outcomes'][k]['price']
        sportsbook = sports_data.json()[i]['bookmakers'][j]['title']
        odds[name][sportsbook] = price

        '''
        odds format: odds[name of the team] = {
            sportbook1: price1,
            sportbook2: price2,
            sportbook3: price3,
            ...
        }
        '''

  list1 = []
  #data collection: all possible odds are calcualed to find a feasible outcome
  for c in range(len(sports_data.json())):
    home = sports_data.json()[c]['home_team']
    away = sports_data.json()[c]['away_team']
    if home not in odds.keys() or away not in odds.keys():
      continue
    else:
      home_sportbook = list(odds[home].keys())
      away_sportbook = list(odds[away].keys())

    for i in range(len(home_sportbook)):
      home_price = odds[home][home_sportbook[i]]
      for j in range(len(away_sportbook)):
        if home_sportbook[i] == away_sportbook[j]:
          continue
        else:
          away_price = odds[away][away_sportbook[j]]
          val = tools.arbi(home_price, away_price)
          if val < 1:
            list1.append((home, away, home_sportbook[i], away_sportbook[j], val)) #list format: [home, away, home_sportbook, away_sportbook, arbitrage value]


    #selection of the data to output a feasible option
    if len(list1) == 0:
      results.append(f"For the {home} v. {away} game, WE DON'T RECOMMEND TO BET. NO sportbook offers odds to earn profit.")
    else:
      max_val = max(list1, key=lambda x: x[4])
      home_price = odds[home][max_val[2]]
      away_price = odds[away][max_val[3]]
      val = max_val[4]
      #team1_price = betValue(toDecimals(list1[max_index][home]['price']), list1[max_index][2])
      results.append(f"For the {home} v. {away} game, WE RECOMMEND TO BET. \nFor {home} WE RECOMMEND to use {max_val[2]} for ${(tools.betValue(home_price, val)):.2f} \nFor {away} WE RECOMMEND to use {max_val[3]} for ${(tools.betValue(away_price, val)):.2f}")
    list1.clear()

  for i in range(len(results)):
    emailBody += results[i] + "\n\n"
  emailBody += "\nProgrammed by Kurian Vadakara. \nSharperBets"
  return emailBody


print(feasibleBets())
game_odds()






