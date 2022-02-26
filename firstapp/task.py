import string

from django.contrib.auth.models import User

from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        # print(username)
        email = '{}@example.com'.format(username)
        # print(email)
        password = get_random_string(50)
        # print(password)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)