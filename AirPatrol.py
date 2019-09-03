import connection

import camera
import drone
import map
import mission
####
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor
from PyQt5.QtCore import QMimeData, Qt
####
from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia
from AirPatrol_design import Ui_MainWindow

import sys
# import vlc

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        # Set up the user interface from Designer.
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Modifications to interface

        """ add vlc interfaces for ip cameras"""

        # Create all required objects
        self.drone = drone.Drone()
        self.map = map.Map()
        self.mission = mission.Mission()

        # TODO add mission_planner_map_image initialisations here
        self.ui.mission_planner_map_image.setContentsMargins(0, 0, 0, 0)


        # TODO load default values here
        self.load_default_values()

        self.map_image.mousePressEvent = self.get_mouse_click_pos

        self.camera_1 = camera.Camera()
        self.camera_1.update_ip_address("192.168.1.1")
        self.camera_2 = camera.Camera()
        self.camera_2.update_ip_address("192.168.1.1")
        self.camera_3 = camera.Camera()
        self.camera_3.update_ip_address("192.168.1.1")
        self.camera_4 = camera.Camera()
        self.camera_4.update_ip_address("192.168.1.1")

        # set up video feeds
        self.media_player_1 = QtMultimedia.QMediaPlayer(self)
        self.media_player_1.setVideoOutput(self.ui.launchpad_monitoring_videofeed_1)
        # fileName = "/path/of/your/local_file"
        # url = QtCore.QUrl.fromLocalFile(fileName)
        url_1 = QtCore.QUrl("http://devimages.apple.com/iphone/samples/bipbop/gear4/prog_index.m3u8")
        self.media_player_1.setMedia(QtMultimedia.QMediaContent(url_1))
        self.media_player_1.play()

        self.media_player_2 = QtMultimedia.QMediaPlayer(self)
        self.media_player_2.setVideoOutput(self.ui.launchpad_monitoring_videofeed_2)
        # fileName = "/path/of/your/local_file"
        # url = QtCore.QUrl.fromLocalFile(fileName)
        url_2 = QtCore.QUrl("http://devimages.apple.com/iphone/samples/bipbop/gear4/prog_index.m3u8")
        self.media_player_2.setMedia(QtMultimedia.QMediaContent(url_2))
        self.media_player_2.play()

        self.media_player_3 = QtMultimedia.QMediaPlayer(self)
        self.media_player_3.setVideoOutput(self.ui.launchpad_monitoring_videofeed_3)
        # fileName = "/path/of/your/local_file"
        # url = QtCore.QUrl.fromLocalFile(fileName)
        url_3 = QtCore.QUrl("http://devimages.apple.com/iphone/samples/bipbop/gear4/prog_index.m3u8")
        self.media_player_3.setMedia(QtMultimedia.QMediaContent(url_3))
        self.media_player_3.play()

        self.media_player_4 = QtMultimedia.QMediaPlayer(self)
        self.media_player_4.setVideoOutput(self.ui.launchpad_monitoring_videofeed_4)
        # fileName = "/path/of/your/local_file"
        # url = QtCore.QUrl.fromLocalFile(fileName)
        url_4 = QtCore.QUrl("http://devimages.apple.com/iphone/samples/bipbop/gear4/prog_index.m3u8")
        self.media_player_4.setMedia(QtMultimedia.QMediaContent(url_4))
        self.media_player_4.play()

        # CONNECT BUTTONS

        #configuration buttons
        self.ui.remove_waypoint_btn.clicked.connect(self.mission.remove_waypoint)

        self.ui.config_camera_update_btn.clicked.connect(self.config_update_camera_parameters)
        self.ui.map_select_file_btn.clicked.connect(self.select_map_file)
        self.ui.config_map_update_btn.clicked.connect(self.config_update_map_parameters)
        self.ui.config_launchpad_update_btn.clicked.connect(self.config_update_launchpad_parameters)
        self.ui.config_uas_update_btn.clicked.connect(self.config_update_uas_parameters)


        # TODO TEST CODE




        # self.load_default_values()

        # TODO introduce queue processing here
        self.station_connection = connection.Connection('localhost', 100)



    def load_default_values(self):
        ''' upon loading up the GCS software, the GCS should also load default values. These default values should
        inform things such as missions, map, drone id, etc.'''
        #TODO: add text file/config file for reading parameters - not hardcoded within the function

        #load map values
        self.map.update_image_location("Maps/map_cranfield.png")
        self.map.update_image_corner_coords("52.5",
                                            "1.1",
                                            "52.1",
                                            "1.5")



        pixmap = QtGui.QPixmap(self.map.image_location)


        # TODO move to initialisation - should be out of the load default values function
        # widget = QtWidgets.QWidget()
        self.map_image = QtWidgets.QLabel(self.ui.widget)
        self.map_image.setPixmap(pixmap)

        # layout_box = QHBoxLayout(widget)

        self.ui.mission_planner_map_image.addWidget(self.map_image)

        # map_image = QtWidgets.QLabel(widget)
        # map_image.setPixmap(pixmap)
        # self.ui.mission_planner_map_image.addWidget(map_image)


    def config_update_uas_parameters(self):
        pass

    def config_update_launchpad_parameters(self):
        pass

    def config_update_map_parameters(self):
        """ Update map parameters """
        self.map.update_image_location(self.ui.mapImageLocationLineEdit.text())
        self.map.update_image_corner_coords(self.ui.map_corner_1_lat.text(),
                                            self.ui.map_corner_1_long.text(),
                                            self.ui.map_corner_4_lat.text(),
                                            self.ui.map_corner_4_long.text())

        print("Updated Map Parameters: ",
              self.map.image_location,
              self.map.image_height,
              self.map.image_width,
              self.map.top_left_lat,
              self.map.top_left_long,
              self.map.bottom_right_lat,
              self.map.bottom_right_long)

        """ Now implement changes """
        self.ui.mission_planner_map_image.setPixmap(QtGui.QPixmap(self.map.image_location))


    def get_mouse_click_pos(self, event):
        #TODO add spherical projection in. This is assuming a flat plane as is inaccurate for long distances.
        x = event.pos().x()
        y = event.pos().y()

        print("position: ", x, y)

        print(self.map.top_left_long)

        longperpix = (self.map.bottom_right_long-self.map.top_left_long)/self.map.image_width
        latperpix = (self.map.bottom_right_lat-self.map.top_left_lat)/self.map.image_height

        print("image width, height:", self.map.image_width, self.map.image_height)
        print(latperpix, longperpix)

        # mouse_pos_lat = float(self.ui.map_corner_1_lat.text()) + latperpix*y
        # mouse_pos_long = float(self.ui.map_corner_1_long.text()) + longperpix*x

        mouse_pos_lat = self.map.top_left_lat + latperpix*y
        mouse_pos_long = self.map.top_left_long + longperpix*x

        self.ui.mission_plan_map_mouse_over_lat_LineEdit.setText(str(mouse_pos_lat))
        self.ui.mission_plan_map_mouse_over_long_LineEdit.setText(str(mouse_pos_long))

        numRows = self.ui.waypoint_table.rowCount()
        self.ui.waypoint_table.insertRow(numRows)
        self.ui.waypoint_table.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(mouse_pos_lat)))
        self.ui.waypoint_table.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(mouse_pos_long)))
        entry = QtWidgets.QDoubleSpinBox()
        entry.setValue(30.0)
        self.ui.waypoint_table.setCellWidget(numRows, 2, entry)

        # TODO add waypoint icon to map
        self.draw_waypoint_icon(x, y, mouse_pos_lat, mouse_pos_long)


        # TODO add

        # return x, y, mouse_pos_lat, mouse_pos_long

    def draw_waypoint_icon(self, input_x, input_y, lat, long):
        # convert image file into pixmap

        # widget = QtWidgets.QWidget()
        print('Doing something')

        waypoint_pixmap = QtGui.QPixmap('waypoint.png')
        waypoint_pixmap = waypoint_pixmap.scaled(waypoint_pixmap.width() * 0.06, waypoint_pixmap.height() * 0.06, QtCore.Qt.KeepAspectRatio)

        waypoint_icon = QtWidgets.QLabel(self.ui.widget)
        waypoint_icon.setPixmap(waypoint_pixmap)

        self.mission.waypoint_list.append(mission.Waypoint(lat,
                                                           long,
                                                           waypoint_icon,
                                                           DraggableLabel(waypoint_icon, waypoint_pixmap)))
        # self.waypoint_icon.setPixmap(waypoint_pixmap)
        # self.waypoint_icon.setFixedSize(waypoint_pixmap.size())
        # self.waypoint_icon.setFixedSize(waypoint_pixmap.size())
        print('Doing something')

        # self.ui.mission_planner_map_image.addWidget(self.waypoint_icon)

        # p = self.geometry().bottomRight() - self.waypoint_icon.geometry().bottomRight() - QtCore.QPoint(100, 100)
        # self.waypoint_icon.move(p)
        # self.waypoint_icon.move(100,100)
        # self.waypoint_icon.show()
        self.mission.waypoint_list[len(self.mission.waypoint_list)-1].waypoint_icon.show()
        self.mission.waypoint_list[len(self.mission.waypoint_list)-1].waypoint_icon.move(input_x + 1, input_y + 62)





    def select_map_file(self):
        self.ui.mapImageLocationLineEdit.setText(QtWidgets.QFileDialog.getOpenFileName()[0])


    def config_update_camera_parameters(self):
        """ Update camera parameters"""

        self.camera_1.update_ip_address(self.ui.camera1IPAddressLineEdit.text())
        self.camera_2.update_ip_address(self.ui.camera2IPAddressLineEdit.text())
        self.camera_3.update_ip_address(self.ui.camera3IPAddressLineEdit.text())
        self.camera_4.update_ip_address(self.ui.camera4IPAddressLineEdit.text())

        print("Updated Camera IP addresses: ", self.camera_1.ip_address, self.camera_2.ip_address, self.camera_3.ip_address, self.camera_4.ip_address)

    def update_drone_vis(self):
        # Update the Flight Data page
        self.ui.dronePositionLineEdit.setText(str(self.drone.pos_lat) + ', ' + str(self.drone.pos_long))
        self.ui.droneHeadingLineEdit.setText(str(self.drone.heading_deg) + ' deg')
        # self.ui.droneSpeedLineEdit.setText(str(self.drone.speed_mps + ' m/s')
        # self.ui.droneAltitudeLineEdit.setText(str(self.drone.alt_m) + ' m')
        self.ui.droneStatusLineEdit.setText(str(self.drone.status))
        self.ui.droneBatteryLineEdit.setText(str(self.drone.battery_percentage + ' %'))

        # TODO update aircraft position on map

        # TODO

    def process_connection(self):
        '''
        This function is executed every 200ms to process information and update the GUI parameters in the background
        while the GCS software is running (see Timer statements below).
        '''
        while self.station_connection.udp_socket.hasPendingDatagrams():
            message = self.station_connection.read_message()[0].decode("utf-8")
            print("Message: ", message)
            # print('Reading Message: ', message.decode("utf-8"))

            # delimit message using commas
            message = message.split(',')

            if message[0] == 'telem':
                # actions in case message is of 'telem' type
                self.drone.pos_lat = message[1] # drone_current_latitude
                self.drone.pos_long = message[2] # drone_current_longitude
                self.drone.battery_percentage = message[3] # drone_battery_percentage
                self.drone.status = message[4]
                self.drone.heading_deg = message[5]

                # TODO add altitude

                self.update_drone_vis()

        # following connection, make sure to request telemetry information from app. Response will be processed during next cycle
        self.station_connection.write_message(self.drone.req_telem())



class DraggableLabel(QLabel):
    def __init__(self, parent, image):
        super(QLabel, self).__init__(parent)
        self.setPixmap(QPixmap(image))
        self.show()
        self.drag_start_position = None

    def mousePressEvent(self, event):
        print("WORKED : Function called")
        if event.button() == Qt.LeftButton:
            print("WORKED : LEFT BUTTON IS CLICKED")
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

class my_label(QLabel):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self,event):
        if event.mimeData().hasImage():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()
    def dropEvent(self,event):
        if event.mimeData().hasImage():
            self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))








            

# Create connection and corresponding Queue

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

timer = QtCore.QTimer()
timer.timeout.connect(application.process_connection)
timer.start(1000)

sys.exit(app.exec())