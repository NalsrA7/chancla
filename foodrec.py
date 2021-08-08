##########################################################
### START OF THE GREATEST FOOD RECOMMENDATION BOT EVER ###
##########################################################

### Work In Progress ###

import random
import time
import json
import discord
from discord.ext import commands
import asyncio
import config

client = commands.Bot(command_prefix = ['im.',"I.","c.","C."], 
                      help_command=commands.MinimalHelpCommand(no_category = "Available Commands"), 
                      activity=discord.Activity(type = discord.ActivityType.playing, name = 'c.help | weeeeeee'), 
                      case_insensitive=True)

# Initializing food dictionary
with open('foodie_dict.json','r') as json_file:
    foodie = json.load(json_file)

# Classes created to display buttons on discord and take in input    
# following class is for taking in time of meal preference 
class TimeOfMeal(discord.ui.View):
   
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Breakfast")
    async def breakfast(self, button, interaction):
        global time_of_meal 
        time_of_meal = "breakfast"
        await interaction.response.edit_message(content=f"You picked {time_of_meal}!\nNow please input wether you would like hot or cold food!", view=TempOfMeal())
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Lunch")
    async def lunch(self, button, interaction):
        global time_of_meal 
        time_of_meal = "lunch"
        await interaction.response.edit_message(content=f"You picked {time_of_meal}!\nNow please input wether you would like hot or cold food!", view=TempOfMeal())

    @discord.ui.button(style=discord.ButtonStyle.primary, label="Dinner")
    async def dinner(self, button, interaction):
        global time_of_meal 
        time_of_meal = "dinner"
        await interaction.response.edit_message(content=f"You picked {time_of_meal}!\nNow please input wether you would like hot or cold food!", view=TempOfMeal())
        
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Dessert")
    async def dessert(self, button, interaction):
        global time_of_meal 
        time_of_meal = "dessert"
        await interaction.response.edit_message(content=f"You picked {time_of_meal}!\nNow please input wether you would like hot or cold food!", view=TempOfMeal())
    
# following class is for taking in temperature of meal preference 
class TempOfMeal(discord.ui.View):
    
    @discord.ui.button(style=discord.ButtonStyle.danger, label="Hot", emoji="🔥")
    async def hot(self, button, interaction):
        global temp_of_meal 
        temp_of_meal = "hot"
        await interaction.response.edit_message(content=f"You picked {temp_of_meal}!\nFinally, please input wether you would like heavy or light food!", view=SizeOfMeal())
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Cold", emoji="❄")
    async def cold(self, button, interaction):
        global temp_of_meal
        temp_of_meal = "cold"
        await interaction.response.edit_message(content=f"You picked {temp_of_meal}!\nFinally, please input wether you would like heavy or light food!", view=SizeOfMeal())

# following class is for taking in size of meal preference AND returning result recommendation
class SizeOfMeal(discord.ui.View):
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Heavy")
    async def heavy(self, button, interaction):
        
        global size_of_meal
        size_of_meal = "heavy"
        embed = discord.Embed(title="Please wait...", #defining embed used in final output of recommendation
                description=f'Our expert AI is picking just the right food for you!\n"hmm... a {size_of_meal} {temp_of_meal} meal for {time_of_meal}... 🤔"', 
                color=discord.Color.greyple())
        embed.set_image(url="https://c.tenor.com/_Zm078I_YAYAAAAC/when.gif")
        
        food_rec = random.choice(foodie[time_of_meal][temp_of_meal][size_of_meal])
        await interaction.response.edit_message(content=None,embed=embed,view=None)
        await asyncio.sleep(7)
        await message.reply(f'Hooray! Our expert AI recommends that you eat {food_rec}!')
        await asyncio.sleep(4)
        await message.reply("Do you want to recommend a food to be added to our database?", view=Confirmation())
        
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Light")
    async def light(self, button, interaction):
        
        global size_of_meal
        size_of_meal = "light"
        embed = discord.Embed(title="Please wait...", #defining embed used in final output of recommendation
                description=f'Our expert AI is picking just the right food for you!\n"hmm... a {size_of_meal} {temp_of_meal} meal for {time_of_meal}... 🤔"', 
                color=discord.Color.greyple())
        embed.set_image(url="https://c.tenor.com/_Zm078I_YAYAAAAC/when.gif")
        
        food_rec = random.choice(foodie[time_of_meal][temp_of_meal][size_of_meal])
        await interaction.response.edit_message(content=None,embed=embed,view=None)
        await asyncio.sleep(7)
        await message.reply(f'Hooray! Our expert AI recommends that you eat {food_rec}!')
        await asyncio.sleep(4)
        await message.reply("Do you want to recommend a food to be added to our database?", view=Confirmation())

       
       
### THE FOLLOWING CODE IS FOR TAKING IN USER INPUT FOR THE FOOD DICTIONARY ###

# buttons to ask USERS if they would like to contribute food to the dictionary.
class Confirmation(discord.ui.View):
    
    @discord.ui.button(style=discord.ButtonStyle.success, label="Yes", emoji="<:pepehappy:873771479907577906>", row=0)
    async def yes(self, button, interaction): 
        response = 'Yes' 
        await interaction.response.edit_message(content=f"Thank you for saying {response}!\nOk. Now please tell us what time of meal best fits the food you would like to contribute!", view=TimeOfMeal_Contrib())
    
    @discord.ui.button(style=discord.ButtonStyle.danger, label="No", emoji="<a:pepecry:873771306993197157>", row=0)
    async def no(self, button, interaction):
        response = "No"
        await interaction.response.edit_message(content=f"You picked {response}!\nThat is very sad <a:pepecry:873771306993197157>", view=Confirmation_Disabled())
    
    @discord.ui.button(style=discord.ButtonStyle.secondary, label="View Current Foods", emoji="📖",row=1)
    async def viewallfood(self, button, interaction):
        all_foods = []
        for x in foodie.values():
            all_foods.append('\n\n')
            for y in x.values():
                for z in y.values():
                    for f in z:
                        all_foods.append(f+", ")
                    
        view_all = ''.join(all_foods)
        await interaction.response.send_message(content="Current List of Foods\n""```"+view_all+"```")
        
class Confirmation_Disabled(discord.ui.View):
    @discord.ui.button(style=discord.ButtonStyle.success, label="Yes", emoji="<:pepehappy:873771479907577906>", row=0, disabled=True)
    async def yes_disabled(self, button, interaction):
        pass
    
    @discord.ui.button(style=discord.ButtonStyle.danger, label="No", emoji="<a:pepecry:873771306993197157>", row=0, disabled=True)
    async def no_disabled(self, button, interaction):
        pass
    
    @discord.ui.button(style=discord.ButtonStyle.secondary, label="View Current Foods", emoji="📖",row=1, disabled=True)
    async def viewallfood_disabled(self, button, interaction):
        pass    
    
       

# buttons for taking in input for time of meal for USERS food contribution
class TimeOfMeal_Contrib(discord.ui.View):
   
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Breakfast")
    async def breakfast(self, button, interaction):
        global time_of_meal 
        time_of_meal = "breakfast"
        await interaction.response.edit_message(content=f"You picked {time_of_meal}!\nNow please input whether the food you are recommending is hot or cold!", view=TempOfMeal_Contrib())
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Lunch")
    async def lunch(self, button, interaction):
        global time_of_meal 
        time_of_meal = "lunch"
        await interaction.response.edit_message(content=f"You picked {time_of_meal}!\nNow please input whether the food you are recommending is hot or cold!", view=TempOfMeal_Contrib())

    @discord.ui.button(style=discord.ButtonStyle.primary, label="Dinner")
    async def dinner(self, button, interaction):
        global time_of_meal 
        time_of_meal = "dinner"
        await interaction.response.edit_message(content=f"You picked {time_of_meal}!\nNow please input whether the food you are recommending is hot or cold!", view=TempOfMeal_Contrib())
        
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Dessert")
    async def dessert(self, button, interaction):
        global time_of_meal 
        time_of_meal = "dessert"
        await interaction.response.edit_message(content=f"You picked {time_of_meal}!\nNow please input whether the food you are recommending is hot or cold!", view=TempOfMeal_Contrib())


# buttons for taking in input for temperature of meal for USERS food contribution
class TempOfMeal_Contrib(discord.ui.View):
    
    @discord.ui.button(style=discord.ButtonStyle.danger, label="Hot", emoji="🔥")
    async def hot(self, button, interaction):
        global temp_of_meal 
        temp_of_meal = "hot"
        await interaction.response.edit_message(content=f"You picked {temp_of_meal}!\nFinally, please input whether your food is heavy or light food!", view=SizeOfMeal_Contrib())
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Cold", emoji="❄")
    async def cold(self, button, interaction):
        global temp_of_meal
        temp_of_meal = "cold"
        await interaction.response.edit_message(content=f"You picked {temp_of_meal}!\nFinally, please input whether your food is heavy or light food!", view=SizeOfMeal_Contrib())


# buttons for taking in input for size of meal for USERS food contribution
class SizeOfMeal_Contrib(discord.ui.View):
    
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Heavy")
    async def heavy(self, button, interaction):
        
        global size_of_meal
        size_of_meal = "heavy"
        food_rec = random.choice(foodie[time_of_meal][temp_of_meal][size_of_meal])
        await interaction.message.reply(f"YYou chose to input a {temp_of_meal} meal that is {size_of_meal} and is eaten for {time_of_meal}.\nNow please type the food you would like to contribute and hit send\n(e.g. chicken nuggets)")
        await Contribution(interaction)
        
    @discord.ui.button(style=discord.ButtonStyle.primary, label="Light")
    async def light(self, button, interaction):
        
        global size_of_meal
        size_of_meal = "light"
        food_rec = random.choice(foodie[time_of_meal][temp_of_meal][size_of_meal])
        await interaction.message.reply(f"You chose to input a {temp_of_meal} meal that is {size_of_meal} and is eaten for {time_of_meal}.\nNow please type the food you would like to contribute and hit send\n(e.g. chicken nuggets)")
        await Contribution(interaction)


async def Contribution(interaction):
    
    def check(msg):
        return msg.author == interaction.user and msg.channel == interaction.channel
    try:
        msg = await client.wait_for("message", check=check, timeout=30) # 30 seconds to reply
    except asyncio.TimeoutError:
        await interaction.response.send_message(content="Sorry, you didn't reply in time!\nThank you for using our food recommendation bot\nCreated by @Nalsra7 [github] and @whyfai [github & discord]")
     
    with open("foodie_contrib.json","r") as f:
        foodie_contrib = json.load(f) 
            
    foodie_contrib[time_of_meal][temp_of_meal][size_of_meal].append(msg.content)
        
    with open('foodie_contrib.json','w') as json_file:
        json.dump(foodie_contrib,json_file,indent=4)
        
    await msg.reply("Thank you for making our food recommendation bot even better!\nThe developers will verify your contribution ASAP!\nCreated by @Nalsra7 [github] and @whyfai [github & discord]")       


### COMMANDS GO BELOW ###      
# to announce bot being operational
@client.event
async def on_ready():
    print("CHANCLA BOT IS ONLINE WOOOOOOOOOOOOOOOOOO!")

# command to trigger food recommendation in discord chat      
@client.command()
async def hungry(ctx):
    global message
    message = await ctx.send("Which time of meal would you like a recommendation for?", view=TimeOfMeal())



  
client.run(config.token) 