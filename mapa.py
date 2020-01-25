import socket
from threading import Thread
import os
import matplotlib.pyplot as plt
from matplotlib import interactive
interactive(True)


""" def receive():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print "received message:", data """


""" def plot_map(): """
plt.plot(4.5, 0, color='grey')
plt.plot(5.5, 0, color='grey')
plt.plot(0, 4.5, color='grey')     
plt.plot(0, 5.5, color='grey')
    

#plot_map()

""" threads = []

for i in range(10):
    t = threading.Thread(target=receive)
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join() """