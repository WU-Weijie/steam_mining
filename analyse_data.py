import json, heapq

# mapping list
country2continent = {'EH': 'AF', 'PN': 'OC', 'TF': 'AT', 'JE': 'EU', 'TP': 'AS', 'YU': 'EU', 'BL': 'NA', 'AX': 'EU', 'HM': 'AT', 'GS': 'AT', 'AN': 'AF', 'DZ': 'AF', 'AO': 'AF', 'SH': 'AF', 'BJ': 'AF', 'BW': 'AF', 'BF': 'AF', 'BI': 'AF', 'CM': 'AF', 'CV': 'AF', 'CF': 'AF', 'TD': 'AF', 'KM': 'AF', 'CG': 'AF', 'CD': 'AF', 'DJ': 'AF', 'EG': 'AF', 'GQ': 'AF', 'ER': 'AF', 'ET': 'AF', 'GA': 'AF', 'GM': 'AF', 'GH': 'AF', 'GN': 'AF', 'GW': 'AF', 'CI': 'AF', 'KE': 'AF', 'LS': 'AF', 'LR': 'AF', 'LY': 'AF', 'MG': 'AF', 'MW': 'AF', 'ML': 'AF', 'MR': 'AF', 'MU': 'AF', 'YT': 'AF', 'MA': 'AF', 'MZ': 'AF', 'NA': 'AF', 'NE': 'AF', 'NG': 'AF', 'ST': 'AF', 'RE': 'AF', 'RW': 'AF', 'SN': 'AF', 'SC': 'AF', 'SL': 'AF', 'SO': 'AF', 'ZA': 'AF', 'SS': 'AF', 'SD': 'AF', 'SZ': 'AF', 'TZ': 'AF', 'TG': 'AF', 'TN': 'AF', 'UG': 'AF', 'ZM': 'AF', 'ZW': 'AF', 'AQ': 'AT', 'AF': 'AS', 'AM': 'AS', 'AZ': 'AS', 'BH': 'AS', 'BD': 'AS', 'BT': 'AS', 'BN': 'AS', 'KH': 'AS', 'CN': 'AS', 'CX': 'AS', 'CC': 'AS', 'IO': 'AS', 'GE': 'AS', 'HK': 'AS', 'IN': 'AS', 'ID': 'AS', 'IR': 'AS', 'IQ': 'AS', 'IL': 'AS', 'JP': 'AS', 'JO': 'AS', 'KZ': 'AS', 'KW': 'AS', 'KG': 'AS', 'LA': 'AS', 'LB': 'AS', 'MO': 'AS', 'MY': 'AS', 'MV': 'AS', 'MN': 'AS', 'MM': 'AS', 'NP': 'AS', 'KP': 'AS', 'OM': 'AS', 'PK': 'AS', 'PS': 'AS', 'PH': 'AS', 'QA': 'AS', 'SA': 'AS', 'SG': 'AS', 'KR': 'AS', 'LK': 'AS', 'SY': 'AS', 'TW': 'AS', 'TJ': 'AS', 'TH': 'AS', 'TR': 'AS', 'TM': 'AS', 'AE': 'AS', 'UZ': 'AS', 'VN': 'AS', 'YE': 'AS', 'AS': 'OC', 'AU': 'OC', 'NZ': 'OC', 'CK': 'OC', 'TL': 'OC', 'FM': 'OC', 'FJ': 'OC', 'PF': 'OC', 'GU': 'OC', 'KI': 'OC', 'MP': 'OC', 'MH': 'OC', 'UM': 'OC', 'NR': 'OC', 'NC': 'OC', 'NU': 'OC', 'NF': 'OC', 'PW': 'OC', 'PG': 'OC', 'WS': 'OC', 'SB': 'OC', 'TK': 'OC', 'TO': 'OC', 'TV': 'OC', 'VU': 'OC', 'WF': 'OC', 'AL': 'EU', 'AD': 'EU', 'AT': 'EU', 'BY': 'EU', 'BE': 'EU', 'BA': 'EU', 'BG': 'EU', 'HR': 'EU', 'CY': 'EU', 'CZ': 'EU', 'DK': 'EU', 'EE': 'EU', 'FO': 'EU', 'FI': 'EU', 'FR': 'EU', 'DE': 'EU', 'GI': 'EU', 'GR': 'EU', 'HU': 'EU', 'IS': 'EU', 'IE': 'EU', 'IM': 'EU', 'IT': 'EU', 'XK': 'EU', 'LV': 'EU', 'LI': 'EU', 'LT': 'EU', 'LU': 'EU', 'MK': 'EU', 'MT': 'EU', 'MD': 'EU', 'MC': 'EU', 'ME': 'EU', 'NL': 'EU', 'NO': 'EU', 'PL': 'EU', 'PT': 'EU', 'RO': 'EU', 'RU': 'EU', 'SM': 'EU', 'RS': 'EU', 'SK': 'EU', 'SI': 'EU', 'ES': 'EU', 'SE': 'EU', 'CH': 'EU', 'UA': 'EU', 'GB': 'EU', 'VA': 'EU', 'FX': 'EU', 'SJ': 'EU', 'AI': 'NA', 'AG': 'NA', 'AW': 'NA', 'BS': 'NA', 'BB': 'NA', 'BZ': 'NA', 'BM': 'NA', 'BQ': 'NA', 'VG': 'NA', 'CA': 'NA', 'KY': 'NA', 'CR': 'NA', 'CU': 'NA', 'CW': 'NA', 'DM': 'NA', 'DO': 'NA', 'SV': 'NA', 'GL': 'NA', 'GD': 'NA', 'GP': 'NA', 'GT': 'NA', 'HT': 'NA', 'HN': 'NA', 'JM': 'NA', 'MQ': 'NA', 'MX': 'NA', 'PM': 'NA', 'MS': 'NA', 'KN': 'NA', 'NI': 'NA', 'PA': 'NA', 'PR': 'NA', 'SX': 'NA', 'LC': 'NA', 'VC': 'NA', 'TT': 'NA', 'TC': 'NA', 'US': 'NA', 'VI': 'NA', 'AR': 'SA', 'BO': 'SA', 'BR': 'SA', 'CL': 'SA', 'CO': 'SA', 'EC': 'SA', 'FK': 'SA', 'GF': 'SA', 'GY': 'SA', 'PY': 'SA', 'PE': 'SA', 'SR': 'SA', 'UY': 'SA', 'VE': 'SA'}

# load data
with open('dataset/user_games_4.json', 'r') as f:
    data = json.load(f)
data = data['user_games']

# continent counter
continent = dict().fromkeys(['AF', 'AT', 'AS', 'OC', 'EU', 'NA', 'SA'], 0)

# continent look up table
continentLT = {'AF': 0, 'AT': 1, 'AS': 2, 'EU': 3, 'OC': 4, 'NA':5, 'SA': 6}
gamesContinent = []   # store game count
gamesContinentPlaytime = []  # store playtime
countGames = []
i = 0
while i < 7:
    i += 1
    gamesContinent.append({})
    gamesContinentPlaytime.append({})
    countGames.append(0)



pt = 0
gg = 0
games = {}
# process data: add continent -> user
for i in data:
    continent[country2continent[i[0]['loccountrycode']]] += 1

    # add continent attribute to user_info
    i[0].update({'continent': country2continent[i[0]['loccountrycode']]})

    # print(i[0])
    # reserve 10 most played games
    i[1]['games'] = heapq.nlargest(10, i[1]['games'], key=lambda k:k['playtime_forever'])
    totalPlaytime = 0
    for game in i[1]['games']:
        # add total playtime and continent count
        totalPlaytime += game['playtime_forever']
        countGames[continentLT[i[0]['continent']]] += 1

        if games.get(game['appid']) == None:
            games.update({game['appid']: {'count': 0, 'AF': 0, 'AT': 0, 'AS': 0, 'OC': 0, 'EU': 0, 'NA': 0, 'SA': 0}})
        # games[game['appid']]['count'] += game['playtime_forever'] # by play time
        # games[game['appid']][i[0]['continent']] += game['playtime_forever']# by play time
        games[game['appid']]['count'] += 1
        games[game['appid']][i[0]['continent']] += 1

        # add to top games list in each continent
        if gamesContinent[continentLT[i[0]['continent']]].get(game['appid']) == None:
            gamesContinent[continentLT[i[0]['continent']]].update({game['appid']: 0})
            gamesContinentPlaytime[continentLT[i[0]['continent']]].update({game['appid']: 0})
        gamesContinentPlaytime[continentLT[i[0]['continent']]][game['appid']] += game['playtime_forever']/60 #by playtime hour
        gamesContinent[continentLT[i[0]['continent']]][game['appid']] += 1


    i[1].update({'playtime_total': totalPlaytime})

# print top 15 games in each continent
print('-----------------------------------------------------------------------')
print('---------------------top 15 games in each continent----------------------')
for cont in continentLT:
    # ranged by possession
    gamesContinent[continentLT[cont]] = dict(sorted(gamesContinent[continentLT[cont]].items(), key=lambda item:item[1], reverse=True))
    # ranged by total playtime
    gamesContinentPlaytime[continentLT[cont]] = dict(sorted(gamesContinentPlaytime[continentLT[cont]].items(), key=lambda item:item[1], reverse=True))
    print('-----------' + cont + '-----------')
    j = 0
    # for g in gamesContinentPlaytime[continentLT[cont]]:  # sorted by playtime
    for g in gamesContinent[continentLT[cont]]: # sorted by owner count
        if j < 20:
            j += 1
        else:
            break

        # sorted by playtime
        # print -> gameid, users count, possession-percentage, total playtime, playtime/person(owned game), playtime/person(all)
        print( str(g) + ", "  #gameid
              + str(gamesContinent[continentLT[cont]][g]) + ", "  #users count
              + str(round(gamesContinent[continentLT[cont]][g] /continent[cont] * 100, 2)) + "%, "  #possession-percentage
              + str(round(gamesContinentPlaytime[continentLT[cont]][g], 2)) + ", "  #total playtime
              + str(round(gamesContinentPlaytime[continentLT[cont]][g] / gamesContinent[continentLT[cont]][g], 2)) + ", "  #playtime/person(owned game)
              + str(round(gamesContinentPlaytime[continentLT[cont]][g] / continent[cont], 2)))  #playtime/person(all)

        # sorted by owner count
        # print(g, str(round(gamesContinent[continentLT[cont]][g] /continent[cont] * 100, 2)) + "%, " + str(gamesContinent[continentLT[cont]][g]))
    print('-----------' + cont + '-----------')
    print()
print('---------------------top 15 games in each continent---------------------')
print('-----------------------------------------------------------------------')





# sort games by playtime /desc
games = dict(sorted(games.items(), key=lambda item:item[1]['count'], reverse=True))

# print continent summaries
print('-----------------------------------------------------------------------')
print('--------------------------continent summaries--------------------------')
sum = 0
for k in continent.keys():
    sum += continent[k]
for k in continent.keys():
    print (k +': ' + str(round(continent[k] / sum * 100, 2)) + "%, " + str(continent[k]))
print('--------------------------continent summaries--------------------------')
print('-----------------------------------------------------------------------')


print()
print()
print()



print('-----------------------------------------------------------------------')
print('------------------------------top 15 games-----------------------------')
# print top 20 games
i = 15
for id in games:
    game = games[id]
    print('--------------------------')
    print('appid: ' + str(id))
    for c in game.keys():
        if c != 'count':
            if game['count'] == 0:
                break
            else:
                print(c + ': ' + str(round(game[c] / game['count'] * 100, 2)) + "%, " + str(round(game[c]/continent[c], 2))) #game owned per person
                # print(c + ': ' + str(round(game[c] / game['count'] * 100, 2)) + "%, " + str(game[c]))
        else:
            print('users count: ' + str(game[c]))
    print('--------------------------')
    print()
    if i <= 0:
        break
    i -= 1

print('------------------------------top 15 games-----------------------------')
print('-----------------------------------------------------------------------')


print(continent)