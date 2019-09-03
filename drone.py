from PyQt5 import QtCore

"""
The drone class provides the GUI with a means of maintaining state information, as well as generating command messages
that can be delivered to the systems.
"""


class Drone:
    """ The drone class carries state information of the drone and provides command and control inputs """

    def __init__(self):
        self.drone_id = None

        self.pos_lat = None
        self.pos_long = None
        self.alt_m = None
        self.speed_mps = None
        self.heading_deg = None
        self.tilt_deg = None
        self.roll_deg = None
        self.camera_tilt = None
        self.battery_percentage = None
        self.flight_time = None

    def req_telem(self):
        message_string = 'telem'
        message_bytes = QtCore.QByteArray()
        return message_bytes.append(message_string.encode())

    def command_land(self):
        message_string = 'land'
        message_bytes = QtCore.QByteArray()
        return message_bytes.append(message_string.encode())

    def command_takeoff(self):
        message_string = 'takeoff'
        message_bytes = QtCore.QByteArray()
        return message_bytes.append(message_string.encode())





