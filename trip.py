class Trip(object):
    def __init__(self, route, start_time, duration, beginning, end):
        self._route = route
        self._start_time = start_time
        self._duration = duration
        self._beginning = beginning
        self._end = end

    @property
    def route(self):
        return self._route

    @property
    def start_time(self):
        return self._start_time

    @property
    def duration(self):
        return self._duration

    @property
    def beginning(self):
        return self._beginning

    @property
    def end(self):
        return self._end

    def __unicode__(self):

        return u'{start_time} via {route}: {duration}'.format(
            start_time=self.start_time.strftime('%m-%d %I:%M %p'),
            route=self.route,
            duration='{hr}:{min:0=2}'.format(
                hr=self.duration.seconds // 60 // 60,
                min=self.duration.seconds // 60 % 60
            ),
            beg=self.beginning,
        )

    def __repr__(self):
        return self.__unicode__()