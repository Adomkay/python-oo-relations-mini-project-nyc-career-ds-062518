class Review:

    _all = []

    def __init__(self, guest, recipe, rating, comment = None):
        self._guest = guest
        self._recipe = recipe
        self._rating = rating
        self._comment = comment
        Review._all.append(self)

    @classmethod
    def all(cls):
        return Review._all

    @property
    def reviewer(self):
        return self._guest

    @reviewer.setter
    def reviewer(self, reviewer):
        self._guest = guest

    @property
    def recipe(self):
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        self._recipe = recipe

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, comment):
        self._comment = comment

# returns the given review's rating





# Class Methods:
# Review.all() returns a list of all invite instances
# Instance Methods:
# review.rating returns the given review's rating
# review.recipe returns the given review's recipe
# review.reviewer returns the given review's reviewer (guest instance)
# review.comment returns the given review's comment, if there is one
