import socket

class server(object):
    
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info = (ip, port)
        s.bind(self.info)
    
    def connect(self):
        '''Wait until a connection is established and returns the client's ip address. '''
        s.listen(1)
        return s.accept()[0]
    
    