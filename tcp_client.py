<<<<<<< HEAD
import socket, pyodbc
=======
import socket, pyodbc, functions, time, sys
import multiprocessing
>>>>>>> cdb968da2ffbc30649795f9c3dea40bb956148a4

class client(object):

    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.recv_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.move_db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ= \\asset\database\BaseStatus.accdb;').cursor()
        self.info = (ip, port)
        self.msg_recv = ""
        self.receving = True
    
    def connect(self):
        '''Connect to a server. Returns True if succeeded, otherwise False. '''
        try:
            self.s.connect(self.info)
            #self.recv_s.connect(self.info)
            self.recv_thd = multiprocessing.Process(target=self.b_recv)
            self.recv_thd.start()
            return True
        except:
            return False
    
    def send(self, msg):
        self.s.send(msg.encode())
    
    def reeive(self):
        return self.s.recv(1024).decode()
    
    def b_recv(self):
        while self.receving:
            self.msg_recv = self.s.recv(1024).decode()
    
    def get_msg(self):
        temp = self.msg_recv[:]
        self.msg_recv = ""
        return temp
    
    def press_start(self):
        self.send("start")
        while not self.get_msg() == "start":
            time.sleep(0.1)
        

def main():
    c = client("127.0.0.1", 25792)
    c.connect()
    input("Press Start")
    c.press_start()
    print("Entered")
    c.recv_thd.terminate()
    c.s.close()

main()
print("exit")