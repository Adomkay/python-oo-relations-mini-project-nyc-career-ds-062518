from environment import *

guest_1 = Guest("Dwight Schrute")

guest_2 = Guest("Michael Scott")

guest_3 = Guest("Pam Beasley")

dinner_party_1 = DinnerParty("Office Christmas Party")

dinner_party_2 = DinnerParty("Your parent's friend's")

dinner_party_3 = DinnerParty("Friend's House Warming")

invite_1 = Invite(dinner_party_1, guest_1)

invite_2 = Invite(dinner_party_1, guest_2)

invite_3 = Invite(dinner_party_1, guest_3)

invite_4 = Invite(dinner_party_2, guest_1)

invite_5 = Invite(dinner_party_3, guest_1)

recipe_1 = Recipe("Disaster")

recipe_2 = Recipe("Punch")

recipe_3 = Recipe("Cookies")

recipe_4 = Recipe("Punch")

recipe_5 = Recipe("Cookies")

recipe_6 = Recipe("Punch")

course_1 = Course(dinner_party_1, recipe_1)

course_2 = Course(dinner_party_1, recipe_2)

course_3 = Course(dinner_party_1, recipe_3)

course_4 = Course(dinner_party_1, recipe_4)

course_5 = Course(dinner_party_2, recipe_5)

course_6 = Course(dinner_party_2, recipe_6)

course_7 = Course(dinner_party_2, recipe_2)

review_1 = Review(guest_1, recipe_1, 3, "the Disaster wasn't as bad as I would've liked")

review_2 = Review(guest_2, recipe_1, 5, "It was total chaos, exceeded expectations")

review_3 = Review(guest_3, recipe_1, 4, "Just disastrous, nothing more")

review_4 = Review(guest_1, recipe_2, 2, "way too much pineapple juice!")

review_5 = Review(guest_2, recipe_2, 2, "not enough pineapple juice!")

review_6 = Review(guest_3, recipe_2, 3, "right amount of pineapple juice, but wasn't anything to write home about")

review_7 = Review(guest_1, recipe_3, 2, "I don't like cookies, that's all.")

review_8 = Review(guest_2, recipe_1, 4, "Pretty disastrous, nothing more")

review_9 = Review(guest_3, recipe_1, 4, "Meh, I've seen more bedlam")

review_10 = Review(guest_1, recipe_4, 1, "It was more of a slap in the face")
