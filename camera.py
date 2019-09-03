

class Camera:
    """ Camera class for monitoring launchpad """
    def __init__(self):
        self.ip_address = ""


    def update_ip_address(self, input_ip_address):
        self.ip_address = input_ip_address

