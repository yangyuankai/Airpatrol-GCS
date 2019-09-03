from html.parser import HTMLParser
import requests

class Analyzer:
    """  """
    def __init__(self):
        self.summary_active_flights = None
        self.summary_plan_limit = None
        self.summary_total_air_time = None
        self.summary_total_log_time = None
        self.summary_total_photos = None
        self.summary_total_videos = None

        self.summary_total_km = None
        self.summary_longest_flight_time_m_s = None
        self.summary_max_flight_time_m_s = None

        self.summary_hottest_battery_temperature_c = None
        self.summary_min_battery_temperature_c = None
        self.summary_max_battery_temperature_c = None

        self.summary_farthest_home_distance_m = None
        self.summary_max_home_distance_m = None

        self.summary_greatest_distance_flown = None
        self.summary_max_distance_allowed = None

        self.summary_highest_altitude_m = None
        self.summary_max_altitude_m = None

        self.fastest_speed_mps = None
        self.max_speed_mps = None

        self.battery_id = None


    def get_html(self, input_url):
        r = requests.get(input_url)
        return r.text

    def download(self):
        html_summary = self.get_html("https://app.airdata.com/flight/last")
        print(html_summary)

    def process(self):
        pass

    def update(self):
        data_summary_html = self.download()

    def upload(self):
        pass


# Test Code
a = Analyzer()
a.download()
