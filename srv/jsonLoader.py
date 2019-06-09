import json

with open('./config/config.json', 'r') as json_data_file:
    jsonCfg = json.load(json_data_file)

HOST = jsonCfg["other"]["host"]
PORT = int(jsonCfg["other"]["port"])
CHAN = jsonCfg["twitch"]["channel"]
NICK = jsonCfg["twitch"]["nick"]
PASS = jsonCfg["twitch"]["token"]
