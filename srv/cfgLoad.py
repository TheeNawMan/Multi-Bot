import json

with open('./config/config.json', 'r') as json_data_file:
    datastore = json.load(json_data_file)

HOST = datastore["other"]["host"]
PORT = int(datastore["other"]["port"])
CHAN = datastore["twitch"]["channel"]
NICK = datastore["twitch"]["nick"]
PASS = datastore["twitch"]["token"]

