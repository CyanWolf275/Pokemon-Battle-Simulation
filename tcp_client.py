import socket, Pokemon, Move

class client(object):

    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info = (ip, port)
    
    def connect(self):
        '''Connect to a server. Returns True if succeeded, otherwise False. '''
        self.s.connect(self.info)

    
    def send(self, msg):
        self.s.send(msg.encode())
    
    def receive(self):
        return self.s.recv(1024).decode()
    
    def press_start(self):
        self.send("start")
        return self.receive()
    
    def battle(self, pkmn, move):
        print(", ".join([str(pkmn), str(move)]))
        return
        recv_lst = self.receive().split(", ")
        op_lst = recv_lst[0].split("/")
        my_lst = recv_lst[1].split("/")
        o_lst = [op_lst[0], int(op_lst[1]), int(op_lst[2]), int(op_lst[3]), int(op_lst[4]), int(op_lst[5]), int(op_lst[6]), int(op_lst[7]), int(op_lst[8]), float(op_lst[9]), float(op_lst[10]), int(op_lst[11]), int(op_lst[12]), int(op_lst[13]), int(op_lst[14]), int(op_lst[15]), op_lst[16], op_lst[17]]
        m_lst = [my_lst[0], int(my_lst[1]), int(my_lst[2]), int(my_lst[3]), int(my_lst[4]), int(my_lst[5]), int(my_lst[6]), int(my_lst[7]), int(my_lst[8]), float(my_lst[9]), float(my_lst[10]), int(my_lst[11]), int(my_lst[12]), int(my_lst[13]), int(my_lst[14]), int(my_lst[15]), my_lst[16], my_lst[17]]
        result = {"first": bool(recv_lst[2]), "my_pkmn": m_lst, "op_pkmn": o_lst}
        return result

b = Pokemon.Pokemon("Bulbasaur")
c = Pokemon.Pokemon("Charmander")
cl = client("", 1000)
cl.battle(b, b.move_lst[0])
cl.battle(c, c.move_lst[0])