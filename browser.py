from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from trip import Trip

class Browser(object):
    def __init__(self, commute):
        self._commute = commute

        self._profile = self.disable_images()
        self._driver = webdriver.Firefox(self._profile)

        self._to_url = self._determine_url(self.commute.home, self.commute.work)
        self._from_url = self._determine_url(self.commute.work, self.commute.home)

    @property
    def commute(self):
        return self._commute

    @property
    def driver(self):
        return self._driver

    @property
    def to_url(self):
        return self._to_url

    @property
    def from_url(self):
        return self._from_url

    # =========================================================================

    def _determine_url(self, start, destination):
        return 'https://www.google.com/maps/dir/{start}/{dest}/'.format(
            start=start.url,
            dest=destination.url
        )

    # =========================================================================

    @staticmethod
    def disable_images():
        """Disables css, images and flash inside browser"""
        ## get the Firefox profile object
        firefox_profile = FirefoxProfile()

        #return firefox_profile

        ## Disable CSS
        firefox_profile.set_preference('permissions.default.stylesheet', 2)
        ## Disable images
        firefox_profile.set_preference('permissions.default.image', 2)
        ## Disable Flash
        firefox_profile.set_preference(
            'dom.ipc.plugins.enabled.libflashplayer.so',
            'false'
        )

        return firefox_profile

    def get_trips(self):

        now = datetime.now()

        vias = self.driver.find_elements_by_xpath(
            "//span[contains(text(),'via')]"
        )

        # Get rid of empty elements
        vias = [element for element in vias if element.text]

        times = []
        for element in vias:
            jstid = int(element.get_attribute('jstid'))
            jstid += 13
            time = self.driver.find_element_by_xpath(
                '//span[@jstid="{id}"]'.format(id=jstid)
            ).text
            times.append(time)

        trips = []

        for i, via in enumerate(vias):
            route_name = via.text.replace('via ', '')
            time = times[i].replace(' min', '').split('h ')
            time = timedelta(
                hours=int(time[0]) if len(time) == 2 else 0,
                minutes=int(time[1]) if len(time) == 2 else int(time[0])
            )
            trip = Trip(
                route=route_name,
                start_time=now,
                duration=time,
                beginning=self.commute.home,
                end=self.commute.work,
            )
            trips.append(trip)

        print trips