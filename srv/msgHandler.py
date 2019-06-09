import sys
from srv.main import con
from srv.cfgLoad import CHAN

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

def sendMsg(*args):
    print(args)
    return args

def runCmd(*args):
    send_message(CHAN, args)




