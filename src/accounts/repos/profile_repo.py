from accounts.models import Profile
from core.core_repo import BaseRepo


class ProfileRepo(BaseRepo):
    model = Profile


profileRepo = ProfileRepo()
