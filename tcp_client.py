import socket, pyodbc, functions, time, sys

class client(object):

    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.move_db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ= \\asset\database\BaseStatus.accdb;').cursor()
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
        return self.receive().split(", ")
