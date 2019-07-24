import socket, pyodbc, functions

class client(object):

    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.move_db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\13918\Documents\Summer\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;').cursor()
        self.info = (ip, port)
    
    def connect(self):
        '''Connect to a server. Returns True if succeeded, otherwise False. '''
        try:
            self.s.connect(self.info)
            return True
        except:
            return False

s = client("127.0.0.1", 1000)
s.connect()
print(s.s.recv())