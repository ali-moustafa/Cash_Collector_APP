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
                                          'collector': 9,
                                          'manager': 5
                                          })

        self.assertEqual(response.status_code, 404)
