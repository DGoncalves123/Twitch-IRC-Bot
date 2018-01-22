import socket
import sys
import ssl
 
 
class IRC:
 
    irc = socket.socket()
  
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    def send(self, chan, msg):
        self.irc.send(bytes("PRIVMSG #" + chan + " :" + msg + "\n",'UTF-8'))
 
    def connect(self, server, channel, botnick, password):
        #defines the socket
        self.irc.connect((server, 6667))
        #self.irc.setblocking(False)
        self.irc.send(bytes("PASS " + password + "\n" , 'UTF-8'))
        self.irc.send(bytes("NICK " + botnick + "\n", 'UTF-8'))
        self.irc.send(bytes("JOIN #" + channel + "\n", 'UTF-8')) 
        self.irc.send(bytes("CAP REQ :twitch.tv/tags\n", 'UTF-8'))
        self.irc.send(bytes("CAP REQ :twitch.tv/commands\n", 'UTF-8'))
        self.irc.send(bytes("CAP REQ :twitch.tv/membership\n", 'UTF-8'))
        self.irc.send(bytes("CAP END\n", 'UTF-8'))
        self.send(channel,'Started PogChamp')
 
    def get_text(self):
        text=self.irc.recv(4096)  #receive the text
        text=text.decode('UTF-8')
        if text.find('PING') != -1:                      
            self.irc.send(bytes('PONG ' + text.split() [1] + '\r\n','UTF-8'))  
        return text