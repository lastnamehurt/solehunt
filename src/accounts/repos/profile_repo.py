from accounts.models import Profile
from core.base_repo import BaseRepo


class ProfileRepo(BaseRepo):
    repo = Profile
