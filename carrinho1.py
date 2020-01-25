import socket
from threading import Thread
import os

global pos_x = 0
global pos_y = 0

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
    if pos_x > 0:
        i = pos_x
        for i in range(-1)
            pos_x = i
    else if pos_x < 0
        i = pos_x
        for i in range(-1)
            pos_x = i

    

def spawn():
    #Função que faz o carro apararecer no mapa
    global pos_x = -5
    global pos_y = -0.5
    

threads = []

for i in range(10):
    t = threading.Thread(target=receive)
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()