import socket

class server(object):
    
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))