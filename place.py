MULTILINE = """{address_1}{address_sep}{address_2}
{city}, {state} {zip}"""
SINGLELINE = "{address_1}{address_sep}{address_2}, {city}, {state} {zip}"


class Place(object):
    def __init__(self, address_1, address_2, city, state, zip):
        self._address_1 = address_1
        self._address_2 = address_2
        self._city = city
        self._state = state
        self._zip = zip

    @property
    def address_1(self):
        return self._address_1

    @property
    def address_2(self):
        return self._address_2

    @property
    def address_list(self):
        address_list = [
            self.address_1,
            self.city,
            self.state,
            self.zip
        ]
        if self.address_2:
            address_list.insert(1, self.address_2)

        return address_list

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def url(self):
        return '+'.join(self.address_list)

    @property
    def zip(self):
        return self._zip

    @property
    def multiline(self):
        return self.format_address(MULTILINE)

    @property
    def singleline(self):
        return self.format_address(SINGLELINE)

    def format_address(self, address):
        return address.format(
            address_1=self.address_1,
            address_sep=', ' if self.address_2 else '',
            address_2=self.address_2,
            city=self.city,
            state=self.state,
            zip=self.zip
        )

    def __unicode__(self):
        return self.singleline

    def __repr__(self):
        return self.__unicode__()