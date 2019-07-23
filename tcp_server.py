import socket, pyodbc, functions

class server(object):
    
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info = (ip, port)
        self.move_db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\13918\Documents\Summer\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;').cursor()
        self.s.bind(self.info)
    
    def connect(self):
        '''Wait until a connection is established and returns the client's ip address. '''
        s.listen(1)
        return s.accept()[0]

    def act(self, pkmn, move):
        #self.move_db.execute("select * from Status where EnName = '" + move + "'")
        pass