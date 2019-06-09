import sys
import requests
from srv.jsonLoader import jsonCfg,tCHAN

def testConnect():
    client_id = jsonCfg["twitch"]["clientID"]
    url = jsonCfg["other"]["twitchapi"]+ 'users?login=' + tCHAN[1:]
    headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
    r = requests.get(url, headers=headers).json()
    name = r['users'][0]['display_name']
    if name.lower() == tCHAN[1:].lower():
        return 'I have authenticated with the API server and am ready to take API commands.'
    else:
        return '"I am whoever I say I am. <- Eminem'
