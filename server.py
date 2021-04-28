import socket
from _thread import *
import mod.LvMOD
import pickle

hostname = socket.gethostname()
ipv4 = socket.gethostbyname(hostname)

server = ipv4
port = 5555

print("{}".format(server))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

print("Waiting for a connection....")
#print(Player_1)
#p1/p2 list for position
#players = [Player(), Player()]
#players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50, (0,0,255))]

def threaded_client(connection, player):
    connection.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            connection.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    connection.close()

currentPlayer = 0

while True:
    connection, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (connection, currentPlayer))
    currentPlayer += 1