

class Mission:
    """ """
    def __init__(self):
        self.waypoint_list = []

    def add_waypoint(self, input_waypoint_entry):
        self.waypoint_list.append(input_waypoint_entry)

    def remove_waypoint(self):
        self.waypoint_list.remove(len(self.waypoint_list))

    def clear_mission(self):
        self.waypoint_list.clear()


class Waypoint:
    """ A waypoint must consist of: lat, long, alt. Optional variables include camera heading and tilt """

    def __init__(self,
                 input_latitude,
                 input_longitude,
                 input_waypoint_icon,
                 input_draggable_icon,
                 # input_drag_start_pos = None,
                 input_altitude=30,
                 input_cam_heading=0,
                 input_cam_tilt=0):

        self.latitude = input_latitude
        self.longitude = input_longitude
        self.altitude = input_altitude
        self.cam_heading = input_cam_heading
        self.cam_tilt = input_cam_tilt
        self.waypoint_icon = input_waypoint_icon
        self.draggable_icon = input_draggable_icon
        # self.input_drage_start_pos = input_drag_start_pos


