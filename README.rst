This seems to be an interaction between gevent and mingle as ``--without-mingle`` avoids this issue and it only happens with a gevent pool.

Install and start 2 workers::

    pip install -r requirements.txt
    celery -A bug_1611 worker -n worker1 -l INFO
    celery -A bug_1611 worker -n worker2 -l INFO

Inject some tasks::

    (bug_1603)john@curiosity:~/bug_1603$ celery -A bug_1611 shell
    Python 2.7.3 (default, Sep 26 2013, 20:03:06) 
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from bug_1611.celery import add
    >>> import time
    >>> while True:
    ...     time.sleep(1)
    ...     add(1, 2)

Ctrl+c a worker. Within a few seconds the other worker will stop.

