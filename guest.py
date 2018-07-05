from invite import *
from review import *
class Guest:
    _all = []

    def __init__(self, name):
        self._name = name
        Guest._all.append(self)
        # remember to keep track of all trip instances

# returns a list of all guest instances
    @classmethod
    def all(cls):
        # import pdb; pdb.set_trace()
        return cls._all

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

# returns the guest invited to the most dinner parties
    @classmethod
    def most_popular(cls):
        invited_guest_list = []
        for invite in Invite.all():
            invited_guest_list.append(invite.guest)
        invited_guest_hist = dict.fromkeys(invited_guest_list, 0)
        for item in invited_guest_list:
            invited_guest_hist[item] += 1
        max_invites = max(invited_guest_hist.values())
        return [guest for guest in invited_guest_hist.keys() if invited_guest_hist[guest] == max_invites][0]

    # returns the guest with lowest average rating for recipe reviews
    @classmethod
    def toughest_critic(cls):
        dict = {}
        dict = dict.fromkeys(Guest._all, [])
        for review in Review.all():
            dict[review._guest].append(review.rating)
        return min(dict.items(), key = lambda item: sum(item[1])/len(item[1]))[0]

    @classmethod
    def most_active_critic(cls):
        guest_rating_list = []
        for item in Review.all():
            guest_rating_list.append(item._guest)
        guest_rating_hist = dict.fromkeys(guest_rating_list, 0)
        for item in guest_rating_list:
            guest_rating_hist[item] += 1
        for item, value in guest_rating_hist.items():
            if guest_rating_hist[item] == max(guest_rating_hist.values()):
                return item

# returns a list of all of the guest's invites
    def invites(self):
        return [invite for invite in Invite.all() if invite.guest == self]

# returns a list of all of the guest's reviews
    def reviews(self):
        return [review for review in Review.all() if review.guest == self]

    def avg_rating(self):
        review_list = self.reviews()
        guest_rating = [review.rating for review in review_list]
        average_rating = sum(guest_rating) / (len(guest_rating)+1)
        return average_rating

# returns the number of dinner party invites a guest has recieved
    def number_of_invites(self):
        return len(self.invites())

# takes in a boolean value (True or False) and updates a guest's rsvp status. It should return the rsvp_status status
    def rsvp(self, invite, rsvp_status):
        invite.accepted = rsvp_status
        return invite.accepted

# adds a guest's review with a rating and comment to a recipe. Returns the given recipe's reviews
    def review_recipe(self, recipe, rating, comment):
        recipe_review_list = []
        Review(self, recipe, rating, comment)
        recipe_review_list = [review for review in Review.all() if review.recipe == recipe]
        return recipe_review_list

# returns the given guest's favorite recipe
    def favorite_recipe(self):
        #get list of all recipes
        self_review_list = [review for review in Review.all() if review.reviewer == self]
        rating_list = [review.rating for review in self_review_list]
        fave_recipe = [review.recipe for review in self_review_list if review.rating == max(rating_list)]
        return fave_recipe[0]









# Class Methods:
# Guest.all() returns a list of all guest instances
# Guest.most_popular() returns the guest invited to the most dinner parties
# Guest.toughest_critic() returns the guest with lowest average rating for recipe reviews
# Guest.most_active_critic() returns the guest with most recipe reviews
# Instance Methods:
# guest.invites() returns a list of all of the guest's invites
# guest.reviews() returns a list of all of the guest's reviews
# guest.number_of_invites() returns the number of dinner party invites a guest has recieved
# guest.rsvp(invite, rsvp_status) takes in a boolean value (True or False) and updates a guest's rsvp status. It should return the rsvp_status status
# guest.review_recipe(recipe, rating, comment) adds a guest's review with a rating and comment to a recipe. Returns the given recipe's reviews
# guest.favorite_recipe() returns the given guest's favorite recipe
