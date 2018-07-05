class Course:
    _all = []

    def __init__(self, dinner_party, recipe):
        self._dinner_party = dinner_party
        self._recipe = recipe
        Course._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def dinner_party(self):
        return self._dinner_party

    @dinner_party.setter
    def dinner_party(self, dinnerparty):
        self._dinner_party = dinner_party

    @property
    def recipe(self):
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        self._recipe = recipe

# returns the dinner party instance for the given course


# returns the recpipe instance for the given cours
# Class Methods:
# Course.all() returns a list of all course instances
# Instance Methods:
# course.dinner_party returns the dinner party instance for the given course
# course.recipe returns the recpipe instance for the given course
