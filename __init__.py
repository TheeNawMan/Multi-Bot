#!/usr/bin/env python3

import re
import socket
import json
import utils.cmd as cmd


## Pull JSON config file
with open('./config/config.json', 'r') as json_data_file:
    datastore = json.load(json_data_file)

## Setup variable to connect to server
HOST = datastore["other"]["host"]
PORT = int(datastore["other"]["port"])
CHAN = datastore["twitch"]["channel"]
NICK = datastore["twitch"]["nick"]
PASS = datastore["twitch"]["token"]
if datastore["other"]["debug"] == "on":
    print("HOST: " + HOST + "\nCHAN: " + CHAN + "\nNICK: " + NICK + "\nPASS: " + PASS)
else:
    print(None)

## Basic function required for the server.
def send_pong(msg):
    con.send(bytes('PONG %s\r\n' % msg, 'UTF-8'))


def send_message(chan, msg):
    con.send(bytes('PRIVMSG %s :%s\r\n' % (chan, msg), 'UTF-8'))


def send_nick(nick):
    con.send(bytes('NICK %s\r\n' % nick, 'UTF-8'))


def send_pass(password):
    con.send(bytes('PASS %s\r\n' % password, 'UTF-8'))


def join_channel(chan):
    con.send(bytes('JOIN %s\r\n' % chan, 'UTF-8'))


def part_channel(chan):
    con.send(bytes('PART %s\r\n' % chan, 'UTF-8'))

# Start Helper Functions 
def get_sender(msg):
    result = ""
    for char in msg:
        if char == "!":
            break
        if char != ":":
            result += char
    return result


def get_message(msg):
    result = ""
    i = 3
    length = len(msg)
    while i < length:
        result += msg[i] + " "
        i += 1
    result = result.lstrip(':')
    return result


def parse_message(msg):
    if len(msg) >= 1:
        msg = msg.split(' ')
        options = {'!test': command_test,
                   '!asdf': command_asdf,
                   '!cmd': cmd.command_asdf2}
        if msg[0] in options:
            options[msg[0]]()

## Commands
def command_test():
    send_message(CHAN, 'testing some stuff')


def command_asdf():
    send_message(CHAN, 'asdfster')

## Build connections for BOT

con = socket.socket()
con.connect((HOST, PORT))

send_pass(PASS)
send_nick(NICK)
join_channel(CHAN)

data = ""

while True:
    try:
        data = data+con.recv(1024).decode('UTF-8')
        data_split = re.split(r"[~\r\n]+", data)
        data = data_split.pop()

        for line in data_split:
            line = str.rstrip(line)
            line = str.split(line)

            if len(line) >= 1:
                if line[0] == 'PING':
                    send_pong(line[1])

                if line[1] == 'PRIVMSG':
                    sender = get_sender(line[0])
                    message = get_message(line)
                    parse_message(message)

                    print(sender + ": " + message)

    except socket.error:
        print("Socket died")

    except socket.timeout:
        print("Socket timeout")