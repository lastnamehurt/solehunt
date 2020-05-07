from django.contrib.auth.models import User

from accounts.services import profileService
from subscribers.seed import subscriberSeeder


class ProfileSeeder(object):

    @classmethod
    def seedProfile(cls, user=None, subscriber=None):

        if user is None:
            user = cls.seedUser()

        if subscriber is None:
            subscriber = subscriberSeeder.seedSubscriber()

        return profileService.create(
            {
                'user': user,
                'twitter_id': 1,
                'first_name': 'test',
                'last_name': 'profile',
                'email': 'test@example.com',
                'bio': 'testing',
                'isSubscribedToDigest': False,
                'signupConfirmation': False,
                'isRegistered': False,
                'subscriber': subscriber,
            }
        )

    @classmethod
    def seedUser(cls, username='testUser', password='solehunt', email='solehunt@example.com', profile=None):
        return User.objects.create(username=username, password=password, email=email, profile=profile)


profileSeeder = ProfileSeeder()
