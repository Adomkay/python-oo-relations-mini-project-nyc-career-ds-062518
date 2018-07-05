class Invite:

    _all = []

    def __init__(self, dinner_party, guest):
        self._dinner_party = dinner_party
        self._guest = guest
        Invite._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def guest(self):
        return self._guest

    @guest.setter
    def guest(self, guest):
        self._guest = guest

    @property
    def dinner_party(self):
        return self._dinner_party

    @dinner_party.setter
    def dinner_party(self, dinnerparty):
        self._dinner_party = dinner_party

    @property
    def rsvp(self):
        return self._rsvp

    @rsvp.setter
    def rsvp(self, rsvp):
        self._rsvp = rsvp

# returns a boolean value (true or false) for whether the the guest accepted the invite or not
    def accepted(self):
        return self.accepted

# returns the given invite's guest instance

# returns the given invite's dinner party instance




# Class Methods:
# Invite.all() returns a list of all invite instances
# Instance Methods:
# invite.accepted returns a boolean value (true or false) for whether the the guest accepted the invite or not
# invite.guest returns the given invite's guest instance
# invite.dinner_party returns the given invite's dinner party instance
