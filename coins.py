import socket
import json
from server_data import ip, port

def coins():
    with open("bloostamp") as file:
        file = file.read().split(":")
        addr, key = file[0], file[1]

    s = socket.socket()
    try:
        s.connect((ip, port))
    except:
        return "Could not connect to server."
    
    s.send(json.dumps({"cmd":"my_coins", "addr":addr, "pwd":key}))
    data = s.recv(1024)
    s.close()
    if data:
        data = json.loads(data)
        if data[u'success']:
            return "You have "+str(data['payload']['amount'])+" coins"
    if not data:
        return "Error"