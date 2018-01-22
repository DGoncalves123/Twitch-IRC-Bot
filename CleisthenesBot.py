from IRC import *
from Twitch import *
import os

d = {}
with open('cfg1.txt') as cid:
	for line in cid:
	   (key, val) = line.split()
	   d[key] = val
irc = IRC()
irc.connect(d['HOST'], d['CHAN'], d['NICK'], d['PASS'])
while 1:
	text = irc.get_text()
	name,msg = Twitch.parseMsg(text)
	print(name,msg)
