import time
import random
import json

# Initializing food dictionary
with open('foodie_dict.json','r') as json_file:
    foodie = json.load(json_file)

print('Welcome to the food recommender bot')
time.sleep(1.5)

while True:

    time_of_meal = input('Which time of meal would you like a recommendation for? [breakfast/lunch/dinner/dessert]:\n').lower()
    
    if time_of_meal in foodie:
        print(f'You chose {time_of_meal}!')
        break
    else:
        print('Sorry! you can only input either breakfast, lunch, dinner, or dessert. Please try again')


while True:

    temp_of_meal = input('Now please input wether you would like hot or cold food! [hot/cold]:\n').lower()
    
    if temp_of_meal in foodie[time_of_meal]:
        print(f'You chose {temp_of_meal}!')
        break
    else:
        print('Sorry! you can only input either hot or cold. Please try again')

while True:

    size_of_meal = input('Finally, please input wether you would like heavy or light food! [heavy/light]:\n').lower()

    if size_of_meal in foodie[time_of_meal][temp_of_meal]:
        print(f'You chose {size_of_meal}!')
        break
    else:
        print('Sorry! you can only input either heavy or light. Please try again')

food_rec = random.choice(foodie[time_of_meal][temp_of_meal][size_of_meal])
print(f'Hooray! You should eat {food_rec}!')


### THE FOLLOWING CODE IS FOR TAKING IN INPUT FOR THE FOOD DICTIONARY ###

yes_choices = ['y','Y','yes','Yes','YES']
no_choices = ['n','N','no','No','NO']
food_opt = ['food_options','food options']
list_food = []

time.sleep(3)
print('Whould you like to recommend a food to be added to the list?')

while True:
    
    choice_rec = input('[type Y for yes and N for no]')


    if choice_rec in yes_choices:
        
        print('Thank you for choosing to expand our list of food')
        time.sleep(2)

        while True:

            print('to see the current options of food, type [food_options]')
            time_of_meal = input('Which time of meal would you like to recommend? [breakfast/lunch/dinner/dessert]:\n').lower()
    
            if time_of_meal in foodie:
                print(f'You chose {time_of_meal}!')
                break
            
            elif time_of_meal in food_opt:
                for x in foodie.values():
                    for y in x.values():
                        for z in y.values():
                            print(z)
            
            else:
                print('Sorry! you can only input either breakfast, lunch, dinner, or dessert. Please try again')

        while True:

            temp_of_meal = input('Would you like to recommend hot or cold food! [hot/cold]:\n').lower()
    
            if temp_of_meal in foodie[time_of_meal]:
                print(f'You chose {temp_of_meal}!')
                break
            else:
                print('Sorry! you can only input either hot or cold. Please try again')

        while True:

            size_of_meal = input('Will you recommend heavy or light food! [heavy/light]:\n').lower()

            if size_of_meal in foodie[time_of_meal][temp_of_meal]:
                print(f'You chose {size_of_meal}!')
                break
            else:
                print('Sorry! you can only input either heavy or light. Please try again')


        new_food = input('Finally, please type what food would you like to recommend.\n')
        
        foodie[time_of_meal][temp_of_meal][size_of_meal].append(str(new_food))
        
        with open('foodie_dict.json','w') as json_file:
            json.dump(foodie,json_file,indent=4)
        
        time.sleep(2)
        print(f'Thank you! {new_food} has been added to the list of foods :)')
        break


    elif choice_rec in no_choices:
        break


    else:
        print('Sorry! You can only type Y for YES and N for NO.')

time.sleep(2)
print('Thank you for using our food recommendation!')