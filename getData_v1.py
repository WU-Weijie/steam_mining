import urllib.request
import json
import random

key = 


def getData(key, userID, interface, method, ids='ids', version="1"):
    url = "https://api.steampowered.com/" + interface + '/' + method + '/v' + version + '/?format=json&key=' + key + '&steam' + ids + '=' + userID
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read().decode('utf-8'))
    return data

if __name__ == '__main__':
    userIDHeader = "765611980"
    dataset = []
    i = 0
    u = 0
    
    #get user data
    while i < 10000:
        # header + 8 random digits
        userID = userIDHeader + str(random.randint(0,99999999)).zfill(8)
        i += 1
        # get user data
        userData = getData(key, userID, "ISteamUser", "GetPlayerSummaries")
        # check the visibility of the profiles and the location infomation
        if (userData['response']['players']['player'][0] != None
            and userData['response']['players']['player'][0].get('communityvisibilitystate') == 3
            and userData['response']['players']['player'][0].get('profilestate') == 1
            and userData['response']['players']['player'][0].get('loccountrycode') != None):
            # get ownedgames and total played time
                ownedGames = getData(key, userID, "IPlayerService", "GetOwnedGames", "id")
                if ownedGames['response']['game_count'] >= 1:
                    userData = userData['response']['players']['player']
                    userData[0].pop('communityvisibilitystate')
                    userData[0].pop('profilestate')
                    userData[0].pop('profileurl')
                    userData[0].pop('avatar')
                    userData[0].pop('avatarmedium')
                    userData[0].pop('avatarfull')
                    userData[0].pop('personastate')
                    userData[0].pop('personastateflags')

                    userData.append(ownedGames['response'])
                    dataset.append(userData)

                    u += 1
        # print(dataset)
        print(str(u) + "/" + str(i))
    print(len(dataset))
    # print(dataset)
    toWrite = {'user_games': dataset}
    with open('user_games_2.json', 'w') as f:
        json.dump(toWrite, f)


