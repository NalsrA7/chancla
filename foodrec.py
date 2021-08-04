##########################################################
### START OF THE GREATEST FOOD RECOMMENDATION BOT EVER ###
##########################################################

### Work In Progress ###

import random

foodie = {'breakfast':
            {'hot':
                {'heavy':['pancakes','avocado on toast','eggs on toast','french toast'],
                'light':['egg wrap','poached eggs','egg quiche']},
            'cold':
                {'heavy':['nutella crepes','avocado on toast','smoothie bowl with fruits'],
                'light':['cereal','PB&J','smoothie bowl']}},
        'lunch':
            {'hot':
                {'heavy':['nasi goreng','lodeh lodeh','Big Mac'],
                'light':['mcdonalds fillet-o-fish','chicken burrito','grilled cheese sandwich']},
            'cold':
                {'heavy':['chicken salad','big sushi roll','pesto pasta'],
                'light':['fruit salad','tuna sandwich','smoked salmon on a bagel']}},
        'dinner':
            {'hot':
                {'heavy':['beef steak','baked ziti pasta','cheese pizza','two indomie packets'],
                'light':['rice and eggs','salmon and asparagus','one indomie packet']},
            'cold':
                {'heavy':['japanese soba','caesar salad'],
                'light':['feta cheese pasta','cereal']}},
        'dessert':
            {'hot':
                {'heavy':['pancakes','lava mug cake'],
                'light':['gulab jamun','jalebi']},
            'cold':
                {'heavy':['choco pudding','chocolate cake'],
                'light':['ice cream','vanilla panna cotta']}}}

#food_rec = ''

print('Welcome to the food recommender bot')


while True:

    time_of_meal = input('Which time of meal would you like a recommendation for? [breakfast/lunch/dinner/dessert]:\n')
    
    if time_of_meal in foodie:
        print(f'You chose {time_of_meal}!')
        break
    else:
        print('Sorry! you can only input either breakfast, lunch, dinner, or dessert. Please try again')


while True:

    temp_of_meal = input('Now please input wether you would like hot or cold food! [hot/cold]')
    
    if temp_of_meal in foodie[time_of_meal]:
        print(f'You chose {temp_of_meal}!')
        break
    else:
        print('Sorry! you can only input either hot or cold. Please try again')

while True:

    size_of_meal = input('Finally, please input wether you would like heavy or light food! [heavy/light]')

    if size_of_meal in foodie[time_of_meal][temp_of_meal]:
        print(f'You chose {size_of_meal}!')
        food_rec = random.choice(foodie[time_of_meal][temp_of_meal][size_of_meal])
        print(f'Hooray! You should eat {food_rec}!')
        break
    else:
        print('Sorry! you can only input either heavy or light. Please try again')
