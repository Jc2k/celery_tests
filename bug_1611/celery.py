from __future__ import absolute_import
from celery import Celery
from . import settings

app = Celery("bug_1611.celery")
app.config_from_object(settings)

@app.task
def add(x, y):
    # print "hello"
    pass

