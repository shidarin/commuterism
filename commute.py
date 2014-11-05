class Commute(object):
    def __init__(self, home, work, start_time):
        self._home = home
        self._work = work
        self._start_time = start_time

        self.monday_to = []
        self.monday_from = []

        self.tuesday_to = []
        self.tuesday_from = []

        self.wednesday_to = []
        self.wednesday_from = []

        self.thursday_to = []
        self.thursday_from = []

        self.friday_to = []
        self.friday_from = []

        self.saturday_to = []
        self.saturday_from = []

        self.sunday_to = []
        self.sunday_from = []

    @property
    def home(self):
        return self._home

    @property
    def start_time(self):
        return self._start_time

    @property
    def work(self):
        return self._work