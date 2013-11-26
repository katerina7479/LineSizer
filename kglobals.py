# Single place for global scoped objects
# Provides a single DatabaseManager, and Creator.
# Also, the order of the imports is important, so don't try to
# neaten them up.


import os

_PATH = os.path.dirname(os.path.abspath(__file__))

from controller.database_manager import DatabaseManager
database_manager = DatabaseManager()

from controller.database_creator import DatabaseCreator
database_creator = DatabaseCreator()

from controller.test_db_creator import TestDatabaseCreator
test_database_creator = TestDatabaseCreator()

from controller.session import Session
session = Session()
