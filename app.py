import pandas as pd
import sys

def RecipesNotFound(recipes_list):
    print(f'Oops, {len(recipes_list)} recipes found for your combination of ingredients')
    new_try = input('Wanna try again with other ingredients? (Y/N): ').lower()
    if new_try == 'y':
        print('Thank you for giving it another try!!')
        GetRecipes()
    elif new_try == 'n':
        print('Maybe another time then!')
        sys.exit()
        
    else: 
        print('Invalid input')
        RecipesNotFound(recipes_list)

def Space():
    print('')

def GetRecipes():
    #If it says recipes.csv can't be found, you should change the path inside df
    df = pd.read_csv('recipes.csv').head(100) #Shows the first 100 results
    #You can increase this number to get more results there are over 4000 recipes
    ing_parsed = df['ingredients_parsed']
    print(f'Hello there user!\nMy machine recommends recipes based on the ingredients you type in')
    print('Type x to exit')
    ing_list = []
    while True:
        user_ingredients = input('Enter your ingredient (type done to continue): ').lower()
        ing_list.append(user_ingredients)
        if user_ingredients.lower() == 'done':
            break
        if user_ingredients.lower() == 'x':
            print('Bye!')
            sys.exit()

    recipes_list = [] #Empty list to which recipes containing user_ingredients will be appendend to
    for index,recipe in enumerate(ing_parsed): #Iterates through dataframe
        try:
            num = 0
            for i in ing_list:
                if i in recipe.split():
                    num += 1
        except AttributeError and TypeError :
            continue
        if num>= 1:
            recipes_list.append(index)

   
    print(f'{len(recipes_list)} Recipes Found')
    for i in recipes_list:
        #Result formatting
        name =df.iloc[i,1]
        ing_set = [i if i not in ('[',']') else '' for i in df.iloc[i,2]]
        ing = "".join(ing_set)
        url = df.iloc[i,0]
        Space()
        print('*'*90)
        print(f'The recipe\'s name is {name}')
        Space()
        print(f'Find more at {url}')
        Space()
        print(f'The ingredients are: {ing}')
        print('*'*90)
    
    if len(recipes_list) == 0:
        RecipesNotFound(recipes_list)

GetRecipes()    















