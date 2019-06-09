import json

with open('./config/config.json', 'r') as json_data_file:
    jsonCfg = json.load(json_data_file)

tHOST = jsonCfg["other"]["twitchhost"]
tPORT = int(jsonCfg["other"]["twitchport"])
tCHAN = jsonCfg["twitch"]["channel"]
tNICK = jsonCfg["twitch"]["nick"]
tPASS = jsonCfg["twitch"]["token"]
