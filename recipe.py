from review import Review
from course import Course

class Recipe:
    _all = []

    def __init__(self, name):
        self._name = name
        Recipe._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

# returns a list of reviews for the given recipe
    def reviews(self):
        return [review for review in Review.all() if review.recipe == self]

    def avg_rating(self):
        review_list = self.reviews()
        recipe_rating = [review.rating for review in review_list]
        average_rating = sum(recipe_rating) / (len(recipe_rating)+1)
        return average_rating

    @classmethod
    def top_three(cls):
        recipe_dict = {}
        for item in Review.all():
            recipe_dict[item.recipe] = item.recipe.avg_rating()
        sorted_recipe_dict = dict(sorted(recipe_dict.items(), key = lambda item: item[1], reverse = True))
        final_list = []
        for i in range(0,3):
            final_list.append(list(sorted_recipe_dict.keys())[i])
        return final_list

    @classmethod
    def bottom_three(cls):
        recipe_dict = {}
        for item in Review.all():
            recipe_dict[item.recipe] = item.recipe.avg_rating()
        sorted_recipe_dict = dict(sorted(recipe_dict.items(), key = lambda item: item[1]))
        final_list = []
        for i in range(0,3):
            final_list.append(list(sorted_recipe_dict.keys())[i])
        return final_list

    def top_five_reviews(self):
        review_list = self.reviews()
        return sorted(review_list, key = lambda review: review.rating, reverse = True)[:5]



# Class Methods:
# Recipe.all() returns a list of all invite instances
# Recipe.top_three() returns a list with the three recipe instances with the highest average rating
# Recipe.bottom_three() returns a list with the three recipe instances with the lowest average rating
# Instance Methods:
# recipe.reviews() returns a list of reviews for the given recipe
# recipe.top_five_reviews() returns a list with the five review instances with the highest rating for the given recipe
