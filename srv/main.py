#!/usr/bin/env python3

import re
import socket
from srv.cfgLoad import HOST, CHAN, NICK, PASS, PORT, datastore
from srv.cmd import command_testw, command_math, command_echo
from srv.msgHandler import sendMsg


if datastore["other"]["debug"] == "on":
    print("HOST: " + HOST + "\nCHAN: " + CHAN + "\nNICK: " + NICK + "\nPASS: " + PASS)
    #print("HOST: " + lHOST + "\nCHAN: " + lCHAN + "\nNICK: " + lNICK + "\nPASS: " + lPASS)
else:
    print(None)

## Basic function required for the server.


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
        options = {'!test': sendMsg(str(command_echo)),
                   '!asdf': command_asdf,
                   '!cmd': command_testw(),
                   '!math': command_math()}
        if msg[0] in options:
            options[msg[0]]()

## Commands
def command_test():
    send_message(CHAN, 'testing some stuff')


def command_asdf():
    send_message(CHAN, command_testw())

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