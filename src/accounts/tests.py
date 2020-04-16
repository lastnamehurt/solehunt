import unittest

from django.test import TestCase

from accounts.models import Profile
from accounts.seed import profileSeeder
from accounts.services import profileService
from subscribers.models import Subscriber

NEW_PROFILE = {
    # 'twitter_id': '234234123',
    'first_name': 'sole',
    'last_name': 'hunt',
    'email': 'acb@abc.com'
}


class ProfileServiceTest(TestCase):
    """
    API Tests
    """

    def setUp(self):
        self.newProfile = profileService.createNewProfileInstance(filters=NEW_PROFILE)

    def testCreateProfileNoUser(self):
        self.assertIsInstance(self.newProfile, Profile)
        self.assertIsNone(self.newProfile.user)

    def testCreateProfileWithUser(self):
        user = profileSeeder.seedUser()
        PROFILE_WITH_USER = NEW_PROFILE.copy()
        PROFILE_WITH_USER['user'] = user
        self.updatedProfile = profileService.createNewProfileInstance(filters=PROFILE_WITH_USER)

        self.assertIsInstance(self.updatedProfile, Profile)
        self.assertEqual(user.id, self.updatedProfile.user.id)

    @unittest.skip  # TODO: churt unskip once signals are created
    def testNewProfileCreatesNewSubscriberFromSignal(self):
        subscriber = Subscriber.objects.last()

        self.assertEqual(self.newProfile.id, subscriber.profile.id)

    def testDeleteProfile(self):
        with self.assertRaises(Exception) as context:
            profileService.deleteProfile(self.newProfile.id)

        self.assertIn("Profile matching query does not exist.", context.exception.args)
        self.assertEqual(Profile.DoesNotExist, context.exception.__class__)

    def testUpdateProfile(self):
        oldProfile = profileService.createNewProfileInstance(filters=NEW_PROFILE)
        oldProfile.save()
        profileService.updateProfile(oldProfile.id, filters={'first_name': 'Admin', 'last_name': 'User'})
        updatedProfile = profileService.getAllProfiles()[0]

        self.assertEqual(updatedProfile.first_name, 'Admin')
        self.assertEqual(updatedProfile.last_name, 'User')
        self.assertEqual(updatedProfile.id, oldProfile.id)

    @unittest.skip
    def testSubscribeToSoleHunt(self):
        """
        RULE: Subscriber must follow instagram or twitter
        """
        pass

    @unittest.skip
    def testUnsubscribe(self):
        pass
