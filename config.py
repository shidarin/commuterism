# =============================================================================
# IMPORTS
# =============================================================================

import ConfigParser
from datetime import time

from place import Place

# =============================================================================
# GLOBALS
# =============================================================================

__all__ = [
    'Config',
]

# =============================================================================
# CLASSES
# =============================================================================


class Config(object):
    """Parses ini file for configuration options"""
    def __init__(self, config_file):
        self._config = ConfigParser.ConfigParser()
        self._config.read(config_file)

        self._home = self._read_address('Home')
        self._work = self._read_address('Work')

        self._early_morning = self._read_time('early_morning')
        self._late_morning = self._read_time('late_morning')
        self._start_time = self._read_time('at_work_by')

        self._early_evening = self._read_time('early_evening')
        self._late_evening = self._read_time('late_evening')

    # Properties ==============================================================

    @property
    def home(self):
        return self._home

    @property
    def work(self):
        return self._work

    @property
    def early_morning(self):
        return self._early_morning

    @property
    def late_morning(self):
        return self._late_morning

    @property
    def early_evening(self):
        return self._early_evening

    @property
    def late_evening(self):
        return self._late_evening

    @property
    def start_time(self):
        return self._start_time

    # Private Methods =========================================================

    def _read_address(self, section):
        keys = [
            'address_1',
            'address_2',
            'city',
            'state',
            'zip'
        ]
        config_results = {key: self._config.get(section, key) for key in keys}

        return Place(**config_results)

    # =========================================================================

    def _read_time(self, key):
        section = 'Times'
        entry = self._config.get(section, key)
        return time(*[int(number) for number in entry.split(':')])

    # Public Methods ==========================================================

    def debug(self):
        """Prints all attributes"""
        print 'Home:', self.home
        print 'Work:', self.work
        print 'Early Morning:', self.early_morning
        print 'Late Morning:', self.late_morning
        print 'At Work By:', self.start_time
        print 'Early Evening:', self.early_evening
        print 'Late Evening:', self.late_evening
