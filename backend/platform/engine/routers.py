# routers.py
import os
from dotenv import load_dotenv

load_dotenv()

class ToggleRouter(object):
    def db_for_read(self, model, **hints):
        if os.getenv('DJANGO_TESTING') == 'true':
            return 'test'
        return 'default'

    def db_for_write(self, model, **hints):
        if os.getenv('DJANGO_TESTING') == 'true':
            return 'test'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations between objects if they are both using the same database
        if obj1._state.db == obj2._state.db:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Specify which databases should allow migrations
        if os.getenv('DJANGO_TESTING') == 'true':
            return db == 'test'
        return db == 'default'
