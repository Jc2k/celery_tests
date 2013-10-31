Build and run with::

    pip install -r requirements.txt
    DJANGO_SETTINGS_MODULE=bug_1603.settings celery -A bug_1603 beat -l DEBUG

Notice it sleeps for 5 minutes - but there is a task set to execute once a minute.

Ctrl+c and start it again. Notice the traceback.

Also commit 457e25e0f7c8dbd74f2b956699546cad9a2b6c42 shows that you can't use config_from_object where object is a module.

