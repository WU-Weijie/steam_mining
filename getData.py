# https://api.steampowered.com/<interface>/<method>/v<version>/
import http.client
import json

key = "your steam-web-api key"

def getData(key, userID, interface, method, version = ""):
    conn = http.client.HTTPSConnection('api.steampowered.com')
    conn.request('GET', '/' + interface + '/' + method + '/v' + version + '/?format=json&key=' + key + '&steamids=' + userID)
    resp = conn.getresponse()
    data = json.loads(resp.read().decode('utf-8'))

    return data
