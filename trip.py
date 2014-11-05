class Trip(object):
    def __init__(self, start_time, duration, beginning, end):
        self._start_time = start_time
        self._duration = duration
        self._beginning = beginning
        self._end = end

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
        return u'{start_time}: {duration} from {beg}'.format(
            start_time=self.start_time,
            duration=self.duration,
            beg=self.beginning,
        )
