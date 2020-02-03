import socket
from threading import Thread
import os

global pos_x = -50
global pos_y = -2.5
global size_x = 5.5
global size_y = 1.5


def send_pos():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE = "Carrinho1/" + pos_x + '/' + pos_y + '/' + size_x + '/' + size_y
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def invertexy():
    x = size_x
    y = size_y
    size_x = y
    size_y = x

def send(message):
    UDP_IP = "127.0.0.1"
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
        print "received message:", data
        
def walk_x():
    #deslocar em posição x
    if pos_x == -5 :
        for i in range(-5, 0, 0.5)
            pos_x = i
            send_pos()
    else if pos_x == 5:
        for i in range(5, 0, -0.5)
            pos_x = i
            send_pos()
    else:
        print("posição inválida")
        spawn_1()   

def walk_y():
    #deslocar em posição y
    if pos_y == -5 :
        for i in range(-5, 0, 0.5)
            pos_y = i
            send_pos()
    else if pos_y == 5:
        for i in range(5, 0, -0.5)
            pos_y = i
            send_pos()
    else:
        print("posição inválida")
        spawn_1()   

def spawn_1():
    #Função que faz o carro apararecer no mapa
    global pos_x = -5
    global pos_y = -0.5
    
def opt1()

def opt2()

def opt3()


threads = []

for i in range(10):
    t = threading.Thread(target=receive)
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()