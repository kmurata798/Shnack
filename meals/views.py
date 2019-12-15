from django.http import HttpResponse
from django.shortcuts import render

import requests
import os
from django.views import View 
from dotenv import load_dotenv
load_dotenv()

class IndexView(View):
    def get(self, request):
        return render(request, 'meals/index.html')

class MealView(View):
    def get(self, request):
        #Public API Key does not need to be secured
        random_recipe = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')

        if random_recipe.status_code == 200:
            response = random_recipe.json()['meals'][0]

        name = response['strMeal']
        instructions = response['strInstructions']
        picture = response['strMealThumb']
        ing1 = response['strIngredient1']
        ing2 = response['strIngredient2']
        ing3 = response['strIngredient3']
        ing4 = response['strIngredient4']
        ing5 = response['strIngredient5']
        ing6 = response['strIngredient6']
        ing7 = response['strIngredient7']
        ing8 = response['strIngredient8']
        ing9 = response['strIngredient9']
        ing10 = response['strIngredient10']
        ing11 = response['strIngredient11']
        ing12 = response['strIngredient12']
        ing13 = response['strIngredient13']
        ing14 = response['strIngredient14']
        ing15 = response['strIngredient15']
        ing16 = response['strIngredient16']
        ing17 = response['strIngredient17']
        ing18 = response['strIngredient18']
        ing19 = response['strIngredient19']
        ing20 = response['strIngredient20']

        return render(request, 'meals/home.html', {
            'name':name,
            'instructions': instructions,
            'picture': picture,
            'ing1': ing1,
            'ing2': ing2,
            'ing3': ing3,
            'ing4': ing4,
            'ing5': ing5,
            'ing6': ing6,
            'ing7': ing7,
            'ing8': ing8,
            'ing9': ing9,
            'ing10': ing10,
            'ing11': ing11,
            'ing12': ing12,
            'ing13': ing13,
            'ing14': ing14,
            'ing15': ing15,
            'ing16': ing16,
            'ing17': ing17,
            'ing18': ing18,
            'ing19': ing19,
            'ing20': ing20
        })

