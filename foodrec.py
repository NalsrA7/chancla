##########################################################
### START OF THE GREATEST FOOD RECOMMENDATION BOT EVER ###
##########################################################

import random

Foodie = {'breakfast':['cereal','eggs and toast','PB&J','avocado on toast'],
            'lunch':['grilled cheese','nasi goreng','lodeh lodeh','mcdonalds fillet-o-fish'],
            'dinner':['steak','ziti pasta','rice and eggs','pizza'],
            'dessert':['ice cream','choco pudding','lava cake','vanilla panna cotta']}
food_rec = ''

print('Welcome to the food recommender bot')



while True:

    time_of_meal = input('Would you like to eat breakfast, lunch, dinner, or dessert (please input exactly as shown):\n')

    if time_of_meal in Foodie:
        print(f'You chose {time_of_meal}!')
        food_rec = random.choice(Foodie[time_of_meal])
        print(f'Hooray! you should eat {food_rec}!')
        break
    else:
        print('Sorry! you can only input either breakfast, lunch, dinner, or dessert. Please try again')