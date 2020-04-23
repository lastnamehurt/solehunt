from django.contrib.auth.models import User


class ProfileSeeder(object):

    @classmethod
    def seedUser(cls, username='testUser', password='solehunt', email='solehunt@example.com'):
        return User.objects.create(username=username, password=password, email=email)


profileSeeder = ProfileSeeder()
