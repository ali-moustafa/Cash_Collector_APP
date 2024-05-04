from django.test import TestCase
from django.urls import reverse
from datetime import datetime

USERNAME_JOHN = 'john_lennon'
PASSWORD_JOHN = 'john_password'


class PostCreateTest(TestCase):

    def test_register_and_login_with_new_user(self):
        url = 'http://localhost:8000/myapp/tasks/'

        response = self.client.post(url, {'name': 'test name',
                                          'address': 'test_addr',
                                          'amount_due': 1000.00,
                                          'amount_due_at': datetime.now(),
                                          'collected': False,
                                          'delivered': False,
                                          'collector': 'ali',
                                          'manager': 'test manager'
                                          })

        self.assertEqual(response.status_code, 400)

        # Register User
        # response = self.client.post(url, {'username': USERNAME_JOHN,
        #                                   'password': PASSWORD_JOHN,
        #                                   'first_name': 'John',
        #                                   'last_name': 'Lennon',
        #                                   'email': 'lennon@thebeatles.com'})
        # self.assertRedirects(response, reverse('login'))
        #
        # # Log in newly registered user
        # user_logged_in = self.client.login(username=USERNAME_JOHN, password=PASSWORD_JOHN)
        # self.assertTrue(user_logged_in)
        #
        # url = reverse('myapp:home')
        # response = self.client.get(url)
        # self.assertTrue(response.context['request'].user.is_authenticated)
