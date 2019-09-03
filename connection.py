import socket
import struct
import queue
import multiprocessing

from PyQt5.QtNetwork import QUdpSocket, QHostAddress

class Connection:
    """
    A Connection object is an IP connection that reads and processes messages from a UDP client.
    This is developed with the vision-based guidance system in mind, though it is not limited to it. It may
    may also provide a connection to a gamepad or other peripheral system.
    """

    #TODO this Connection class is there as a placeholder.
    # TODO This should migrate to multi-processing/multi-threading, and remove risk of blocking functions


    def __init__(self, input_ipAdress, input_port):

        self.host_ip = QHostAddress(input_ipAdress)
        self.port = input_port
        self.udp_socket = QUdpSocket()

        # udp_socket.bind(QHostAddress('192.168.43.126'),port)
        print(self.udp_socket.bind(QHostAddress('localhost'), self.port))

    def write_message(self, input_message):
        # udp_socket.writeDatagram(b, QHostAddress('192.168.43.1'), port)
        # self.udp_socket.writeDatagram(input_message, self.host_ip, self.port)
        self.udp_socket.writeData(input_message)

    def read_message(self):
        return self.udp_socket.readDatagram(100)


