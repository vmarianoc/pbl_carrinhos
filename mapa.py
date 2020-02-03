import socket
from threading import Thread
import os
import matplotlib.pyplot as plt
from matplotlib import interactive
from vpython import *



#Criando um mapa
#Via H
box(pos=vector(0, 0, 0),
    size=vector(110, 10, 0), 
    color = color.gray(2))

#Via V
box(pos=vector(0, 0, 0),
    size=vector(10, 110, 0), 
    color = color.gray(2))

#Faixas H
box(pos=vector(0, 0, 0),
    size=vector(1, 110, 0), 
    color = color.yellow)

#Faixas V
box(pos=vector(0, 0, 0),
    size=vector(110, 1, 0), 
    color = color.yellow)

#Jardins
box(pos=vector(30, 30, 0),
    size=vector(50, 50, 0), 
    color = color.green)
box(pos=vector(-30, 30, 0),
    size=vector(50, 50, 0), 
    color = color.green)
box(pos=vector(30, -30, 0),
    size=vector(50, 50, 0), 
    color = color.green)
box(pos=vector(-30, -30, 0),
    size=vector(50, 50, 0), 
    color = color.green)


def carro1(pos_x, pos_y, size_x, size_y):
#Carrinho 1
#inicial -50, -2.5
#size 5.5, 1.5
box(pos=vector(pos_x,pos_y,0),
        size=vector(size_x,size_y,1.6),
        color=color.red)

def carro2(pos_x, pos_y):
#Carrinho 2
#inicial 50, 2.5
box(pos=vector(pos_x,pos_y,0),
        size=vector(5.5,1.5,1.6),
        color=color.red)

def carro3(pos_x, pos_y):
#Carrinho 3
#inicial 2.5,-50
box(pos=vector(pos_x,pos_y,0),
        size=vector(1.5,5.5,1.6),
        color=color.red)

def carro4(pos_x, pos_y):
#Carrinho 4
#inicial -2.5, 50
box(pos=vector(pos_x,pos_y,0),
        size=vector(1.5,5.5,1.6),
        color=color.red)





def exibe(data):
    message = data.split("/")
    
    carro = message[0]
    pos_x = message[1] 
    pos_y = message[2]


 


def receive():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        exibe(data)
        print("received message:", data) 


threads = []

for i in range(10):
    t = threading.Thread(target=receive)
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join() 