import urllib.request
import json
import random

key = 


def getData(key, userID, interface, method, ids='ids', version="1"):
    url = "https://api.steampowered.com/" + interface + '/' + method + '/v' + version + '/?format=json&key=' + key + '&steam' + ids + '=' + userID
    # url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v1/?format=json&key=DF893D1F606289EEBE946ED629C32819&steamids=76561197960435530,76561198147924133"
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read().decode('utf-8'))
    # data = data['response']['games']
    # data = data['response']['players']
    # print (data)
    # return data['response']['players']
    return data

if __name__ == '__main__':
    # userIDs = ["76561197960435539",
    #           "76561198262236331",
    #           "76561198003030375",
    #             "76561198003030373"]
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
                if ownedGames['response']['game_count'] >= 5:
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
    # dataset.append(data['response']['players']['player'])




# response = urllib.request.urlopen('https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?format=json&key=DF893D1F606289EEBE946ED629C32819&steamid=76561198147924133')
# html = response.read()
# print (html)

# import urllib.request
# response = urllib.request.urlopen('http://python.org/')
# html = response.read()
# print (html)



##keep data if communityvisibilitystate == 3 && personastate == 1


