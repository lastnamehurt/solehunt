from celery.task.schedules import crontab
from celery.decorators import periodic_task

from blog.mappers.type_mapper import ResponseType
from blog.services import blogService
from blog.services.ghost_service import ghostContentApi


# https://realpython.com/asynchronous-tasks-with-django-and-celery/
@periodic_task(run_every=(crontab(minute='*/15')), name="getOrCreateBlogs", ignore_result=True)
def getOrCreateBlogs() -> ResponseType.BLOG_POSTS:
    allBlogs = blogService.getPosts()
    apiBlogData = ghostContentApi.getAllPosts()
    # TODO churt: finish this logic
    return [allBlogs] + [apiBlogData]
