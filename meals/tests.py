from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from accounts.forms import UserCreationForm

# Create your tests here.
class IndexViewTest(TestCase):

    def test_true_is_true(self):
        self.assertEqual(True, True) # Tests if True is equal to True. Should always pass.

class Test(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse_lazy('indexview'))
        self.assertEqual(response.status_code, 200)

# class MealsViewTest(TestCase):

#     def test_meals_view(self):
#         response = self.client.get(reverse_lazy('mealsview')
#         self.assertEqual(response.status_code, 200)