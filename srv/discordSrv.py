#!/usr/bin/env python3

import re
import socket
from srv.jsonLoader import HOST, CHAN, NICK, PASS, PORT, jsonCfg
from srv.cmd import *

def discordStart():
    if jsonCfg["other"]["debug"] == "on":
        print("HOST: " + HOST + "\nCHAN: " + CHAN + "\nNICK: " + NICK + "\nPASS: " + PASS)
    else:
        print(None)