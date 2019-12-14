from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from accounts.forms import UserCreationForm

# Create your tests here.
class RegisterViewTest(TestCase):

    def test_single_page(self):
            response = self.client.get(reverse_lazy('sign-up-page'))
            self.assertEqual(response.status_code, 200)
        
class FormCreationTest(TestCase):
    #test creation of form
    def test_form(self):

        form_input = {
            'username': 'pennyjennybenny',
            'email': 'test123@testing.com',
            'password1': 'mypassword123',
            'password2': 'mypassword123',
        }

        form = UserCreationForm(data=form_input)
        self.assertTrue(form.is_valid())