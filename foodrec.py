##########################################################
### START OF THE GREATEST FOOD RECOMMENDATION BOT EVER ###
##########################################################

### Work In Progress ###

import random

Foodie = {'breakfast':
            {'hot':['eggs on toast','egg burrito','pancakes'],
            'cold':['cereal','PB&J','avocado on toast']},
        'lunch':
            {'hot':['grilled cheese','nasi goreng','lodeh lodeh','mcdonalds fillet-o-fish'],
            'cold':['chicken salad','fruit salad']},
        'dinner':
            {'hot':['beef steak','baked ziti pasta','rice and eggs','cheese pizza'],
            'cold':['pesto pasta','caesar salad','cereal']},
        'dessert':
            {'hot':['jaleebi','gulab jamun','pancakes','lava mug cake'],
            'cold':['ice cream','choco pudding','vanilla panna cotta']}}
#food_rec = ''

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