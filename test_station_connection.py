
import connection
import time

from PyQt5 import QtCore
from PyQt5.QtNetwork import QUdpSocket, QHostAddress



def main():

    # conn = connection.Connection('localhost', 100)
    udp_socket = QUdpSocket()
    time.sleep(3)

    s = 'test/n'

    b = QtCore.QByteArray()
    b.append(s.encode())

    udp_socket.connectToHost(QHostAddress.LocalHost, 100)

    while True:
        udp_socket.writeData(b)
        time.sleep(1)

main()