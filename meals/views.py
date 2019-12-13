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

        return render(request, 'meals/home.html', {
            'name':name,
            'instructions': instructions,
            'picture': picture,
        })

