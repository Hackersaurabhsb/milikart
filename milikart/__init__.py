from .celery import app as celery_app
__all__=['celery_app']
#we have included these lines to make sure that celery starts automatically when django starts
