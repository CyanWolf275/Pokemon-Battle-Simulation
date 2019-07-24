import socket, pyodbc, functions, time, sys
from random import random
import multiprocessing

class server(object):
    
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info = (ip, port)
        #self.move_db = pyodbc.connect( r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' r'DBQ=C:\Users\jeffr\OneDrive\Desktop\VS2020\BattleSimulation\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;').cursor()
        self.s.bind(self.info)
        self.conn = None
        #self.recv_conn = None
        self.msg_recv = ""
        self.receiving = True
    
    def connect(self):
        '''Wait until a connection is established and returns the client's ip address. '''
        self.s.listen(1)
        self.conn, ip = self.s.accept()
        #self.recv_conn, ip = self.s.accept()
        self.recv_thd = multiprocessing.Process(target=self.b_recv)
        self.recv_thd.start()
        return ip

    def act(self, pkmn, mv):
        '''msg: name, atk_cat, atk, pwr, op_code/miss
        data: hp, status
        '''
        exec(mv.my_code)
        msg = ""
        if random() >= mv.acc:
            msg = "miss"
        else:
            msg = mv.name + ", " + mv.cat + ", " + str(mv.atk(pkmn)) + ", " + mv.pwr + mv.op_code
        self.conn.send(msg)
        data = conn.recv().split(", ")
        return {"hp": data[0], "status": data[1]}

    def send(self, msg):
        self.conn.send(msg.encode())
    
    def receive(self):
        return self.conn.recv(1024).decode()
    
    def b_recv(self):
        while self.receive:
            self.msg_recv = self.recv_conn.recv(1024).decode()
    
    def get_msg(self):
        temp = self.msg_recv[:]
        self.msg_recv = ""
        return temp
    
    def press_start(self):
        self.send("start")
        while not self.get_msg() == "start":
            time.sleep(0.1)

def main():
    s = server("127.0.0.1", 25792)
    print(s.connect())
    input("Press Start")
    s.press_start()
    print("Entered")
    s.recv_thd.terminate()
    #s.recv_conn.close()
    s.conn.close()
    s.s.close()

    def act(self, pkmn, move):
        #self.move_db.execute("select * from Status where EnName = '" + move + "'")
        pass
