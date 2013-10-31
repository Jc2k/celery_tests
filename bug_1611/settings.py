from __future__ import absolute_import

SECRET_KEY = 'hello'

BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'cache+memcached://127.0.0.1:11211/'
CELERYD_POOL = 'gevent'

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'every-minute': {
        'task': 'bug_1603.celery.add',
        'schedule': crontab(minute='*/1'),
        'args': (1,2),
    }
}

