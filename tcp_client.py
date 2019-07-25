import socket

class client(object):

    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info = (ip, port)
    
    def connect(self):
        '''Connect to a server. Returns True if succeeded, otherwise False. '''
        try:
            self.s.connect(self.info)
            return True
        except:
            return False
    
    def send(self, msg):
        self.s.send(msg.encode())
    
    def receive(self):
        return self.s.recv(1024).decode()
    
    def press_start(self):
        self.send("start")
        return self.receive()
    
    def battle(self, pkmn, move):
        self.send(", ".join([str(pkmn), str(move)]))
        recv_lst = self.receive().split(", ")
        op_lst = recv_lst[0].split("/")
        my_lst = recv_lst[1].split("/")
        result = {"first": bool(recv_lst[2])}