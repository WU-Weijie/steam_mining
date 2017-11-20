# https://api.steampowered.com/<interface>/<method>/v<version>/
import urllib.request
import json

key = "your steam-web-api key"

#ids = "ids" / "id" depending on the method, pls check steam web api before calling the function. 
def getData(key, userID, interface, method, ids='ids', version="1"):
    url = "https://api.steampowered.com/" + interface + '/' + method + '/v' + version + '/?format=json&key=' + key + '&steam' + ids + '=' + userID
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read().decode('utf-8'))
    return data

# get user data
# getData(key, userID, "ISteamUser", "GetPlayerSummaries")

# get ownedgames and total played time
# getData(key, userID, "IPlayerService", "GetOwnedGames", "id")
