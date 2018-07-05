from course import Course
from dinnerparty import DinnerParty
from guest import Guest
from invite import Invite
from recipe import Recipe
from review import Review


# an invite belongs to a dinnerparty
# an invite belongs to a _guest
#
# a dinnerparty has many invites
# a dinnerparty has many guests
# a dinnerparty has many courses
# a dinnerparty has many recipies through courses
# a dinnerparty has many reviews through guests
#
# a guest has many invites
# a guest has many dinnerparties
# a guest has many courses through dinnerparty
# a guest has many recipies through courses
# a guest has many reviews
#
# a course has many dinnerparties
# a course has many guests through dinnerparties
# a course has many invites through guests
# a course belongs to a recipe
#
# a recipe has many reviews
# a recipe has many guests through _dinnerparty
# a recipe has many courses through dinnerparties
# a recipe has many invites through guests through dinnerparties
# a recipe has many dinnerpaties
