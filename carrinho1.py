import socket
from threading import Thread
import random
import os

id = 1
global pos_x = -50.0
global pos_y = -2.5
global size_x = 5.5
global size_y = 1.5

fila = []


def send_pos():
    UDP_IP = "127.0.0.255"
    UDP_PORT = 5005
    MESSAGE = "1/" + pos_x + '/' + pos_y + '/' + size_x + '/' + size_y
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def invertexy():
    x = size_x
    y = size_y
    global size_x = y
    global size_y = x

def send(message):
    UDP_IP = "127.0.0.255"
    UDP_PORT = 5005
    MESSAGE = message

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    
def receive():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        checaMensagem(data)
        print "received message:", data
        
def checaMensagem(data):
    #Verifica o conteudo da mensagem recebida
    message = data.split("/")
    if data[1] == "Cheguei":
        fila.append(message[0])
    if data[1] == "Acabei"
        fila.remove(message[0])

def walk_x():
    #deslocar em posição x
    if pos_x == -50:
        for i in range(-50, -2.5, 1)
            pos_x = i
            if i == -5:
                send("chegando")
            send_pos()
    else if pos_x == 50:
        for i in range(50, 2.5, -1)
            pos_x = i
            if i == -5:
                send("chegando")
            send_pos()
    else:
        print("posição inválida")
        spawn_1()   

def walk_y():
    #deslocar em posição y
    if pos_y == -50 :
        for i in range(-50, -2.5, 1)
            pos_y = i
            if i == -5:
                send("chegando")
            send_pos()
    else if pos_y == 50:
        for i in range(50, 2.5, -1)
            pos_y = i
            if i == -5:
                send("chegando")
            send_pos()
    else:
        print("posição inválida")
        spawn_1()   


def spawn_1():
    #Função que faz o carro apararecer no mapa
    global pos_x = -50.0
    global pos_y = -2.5
    global size_x = 5.5
    global size_y = 1.5
    send("Apareci")
    
def opt1()
    #segue reto
    for i in range(-5, 50, 1)
        pos_x = i
        send_pos()
    send("1/Acabei")
    

def opt2()
    #vira a direita
    for i in range(-5, 2.5, 1)
        pos_x = i
        send_pos()
    invertexy()
    for i in range(2.5, 50, 1)
        pos_y = i
        send_pos()
    send("1/Acabei")

def opt3()
    #vira a esquerda
    for i in range(-5, -2.5, 1)
        pos_x = i
        send_pos()
    invertexy()
    for i in range(2.5, -50, -1)
        pos_y = i
        send_pos()
    send("1/Acabei")

def checaCondicao():
    #Verifica se ha outro carro no cruzamento
    #Verifica se e o primeiro da lista
    #Atravessa
    if fila.size == 0:
        return True
    elif fila[0] == "1":
        return True
    else
        return False

options = [1,2,3]

try:
    spawn_1()
    walk_x()
    opt = random.choice(options)
    send("1\Cheguei")

#    while(checaCondicao):    
        if opt == 1:
            opt1()
                    
        elif opt == 2:
            opt2()
            
        elif opt == 3:
            opt3()    
            

    threads = []

    for i in range(10):
        t = threading.Thread(target=receive)
        t.start()
        threads.append(t)
        
    for thread in threads:
        thread.join()