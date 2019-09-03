
from PIL import Image

class Map:
    def __init__(self):
        self.image_location = ""

        self.top_left_lat = None
        self.top_left_long = None
        self.bottom_right_long = None
        self.bottom_right_lat = None

        self.image_width = None
        self.image_height = None

    def calc_image_dimensions(self, input_image_location):

        temp_im = Image.open(input_image_location)
        self.image_width, self.image_height = temp_im.size

    def update_image_corner_coords(self,
                                   input_top_left_lat,
                                   input_top_left_long,
                                   input_bottom_right_lat,
                                   input_bottom_right_long):

        print(input_top_left_lat, input_bottom_right_lat)

        self.top_left_lat = float(input_top_left_lat)
        print(self.top_left_lat)
        self.top_left_long = float(input_top_left_long)
        self.bottom_right_lat = float(input_bottom_right_lat)
        print(self.bottom_right_lat)
        self.bottom_right_long = float(input_bottom_right_long)

    def update_image_location(self, input_image_location):
        self.image_location = input_image_location
        self.calc_image_dimensions(self.image_location)

    def mouse_location_to_lat_long(self, input_mouse_x, input_mouse_y):
        pass


