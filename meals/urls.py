from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='indexview'),
    path('meals/', views.MealView.as_view(), name='mealview'),
]