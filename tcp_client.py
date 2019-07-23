import socket

class client(object):

    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info = (ip, port)
    
    def connect(self):
        '''Connect to a server. Returns True if succeeded, otherwise False. '''
        try:
            s.connect(self.info)
            return True
        except:
            return False