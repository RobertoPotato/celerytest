import os
from celery import Celery
from celery.schedules import crontab
# from .views import add_new_input

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerytest.settings')

app = Celery('celerytest')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     pass
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(10.0, test.s('Hello'), name='add every 10')

    # # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), name='do sumn', expires=10)

    # # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=14, minute=37, day_of_week=2),
    #     test.s('Happy Mondays!'),
    # )

    # Calls data input insertion every 10 seconds.
    # sender.add_periodic_task(10.0, add_new_input(), name='add every 10')

# @app.task
# def test(arg):
#     print(arg)

# @app.task
# def add(x, y):
#     z = x + y
#     print(z)
