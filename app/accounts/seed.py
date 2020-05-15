import random

import names

from django.contrib.auth.models import User

from accounts.services import profileService
from subscribers.services.subscriber_service import subscriberService


class ProfileSeeder(object):

    @classmethod
    def seedProfile(cls, user=None, subscriber=None):

        first, last = names.get_full_name().split(" ")
        email = "{}.{}@example.com".format(first, last)
        username = "{}.{}".format(first, random.choice(range(150)))

        if user is None:
            user = cls.seedUser()

        if not subscriber:
            subscriber = subscriberService.createNewSubscriber(filters={'alias': username, 'isActive': True})

        return profileService.create(
            {
                'user': user,
                'twitter_id': 1,
                'first_name': first,
                'last_name': last,
                'email': email,
                'bio': 'testing',
                'isSubscribedToDigest': False,
                'signupConfirmation': False,
                'isRegistered': False,
                'subscriber': subscriber,
            }
        )

    @classmethod
    def seedUser(cls, username=None, password='solehunt', email=None, profile=None):
        if not username:
            username = names.get_first_name()
        if not email:
            email = "{}@example.com".format(username)

        return User.objects.create(username=username, password=password, email=email, profile=profile)


profileSeeder = ProfileSeeder()
