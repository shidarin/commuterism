from browser import Browser
from commute import Commute
from config import Config
from place import Place
from trip import Trip

config = Config('./config.ini')
config.debug()

commute = Commute(config.home, config.work, config.start_time)

browser = Browser(commute)
browser.driver.get(browser.to_url)
browser.driver.implicitly_wait(10)
browser.get_trips()