class Twitch:


	def parseMsg(text):
		tokens = text.split(' ')
		if 'PRIVMSG' in tokens:
			start = tokens.index('PRIVMSG')
			name = tokens[start+1]
			name = name.strip('#')
			msg = tokens[start+2]
			msg = msg.strip(':')
			return name,msg
		else:
			return 'FULL',text