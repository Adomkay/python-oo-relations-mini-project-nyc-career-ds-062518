from invite import Invite
from course import Course
from review import Review

class DinnerParty:
    _all = []

    def __init__(self, name):
        self._name = name
        DinnerParty._all.append(self)
        # remember to keep track of all trip instances

# returns a list of all dinner party instances
    @classmethod
    def all(cls):
        return cls._all

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

# returns a list of all of invites handed out for the party
    def invites(self):
        return [invite for invite in Invite.all() if invite.dinner_party == self]

# returns a list of the party's guests
    def guests(self):
        return [invite.guest for invite in Invite.all() if invite.dinner_party == self]

# returns the number of guests who accepted their invite for the dinner party
    def number_of_attendees(self):
        dinner_guest_list = [invite for invite in Invite.all() if invite.dinner_party == self and invite.accepted == True]
        return len(dinner_guest_list)

# returns a list of the party's courses
    def courses(self):
        return [course for course in Course.all() if course.dinner_party == self]

# returns a list of all the recipes for the courses featured at the given dinner party
    def recipes(self):
        return [course.recipe for course in self.courses()]

# returns the number of recipes for the given dinner party
    def recipe_count(self):
        recipe_list = self.recipes()
        return len(recipe_list)

# returns a list of reviews for the recipes of a given dinner party
    def reviews(self):
        recipe_list = self.recipes()
        review_list = []
        for item in recipe_list:
            review_list += [review for review in Review.all() if review.recipe == item]
        return review_list

# returns the highest rated recipe for the given dinner party
    def highest_rated_recipe(self):
        ratings_list = self.reviews()
        rating_dict = {}
        for item in ratings_list:
            rating_dict[item.recipe] = item.rating
        for recipe, rating in rating_dict.items():
            if rating_dict[recipe] == max(rating_dict.values()):
                return recipe





# Class Methods:
# DinnerParty.all() returns a list of all dinner party instances
# Instance Methods:
# dinner_party.invites() returns a list of all of invites handed out for the party
# dinner_party.guests() returns a list of the party's guests
# dinner_party.number_of_attendees() returns the number of guests who accepted their invite for the dinner party
# dinner_party.courses() returns a list of the party's courses
# dinner_party.recipes() returns a list of all the recipes for the courses featured at the given dinner party
# dinner_party.recipe_count() returns the number of recipes for the given dinner party
# dinner_party.reviews() returns a list of reviews for the recipes of a given dinner party
# dinner_party.highest_rated_recipe() returns the highest rated recipe for the given dinner party
