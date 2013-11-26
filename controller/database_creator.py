import os
from utils import myjson
from kglobals import _PATH, database_manager


class DatabaseCreator():
    def __init__(self):
        self._database_path = _PATH + '/database/project.sqlite3'
        self.table_path = _PATH + '/setup/tables.json'
        self.table_init_path = _PATH + '/setup/db_init.json'

    def create_database(self):
        try:
            self._delete_database()
        except:
            pass
        self.tabledata = myjson.get_data(self.table_path)
        database_manager.create_tables(self.tabledata)

    def initialize_database(self):
        self.initial_data = myjson.get_data(self.table_init_path)
        self._add_data()

    def _add_data(self):
        for tablename in self.initial_data:
            test = self.initial_data[tablename]
            if isinstance(test, list):
                for dic in test:
                    database_manager.add(tablename, dic)
            elif isinstance(test, dict):
                database_manager.add(tablename, test)

    def _delete_database(self):
        try:
            os.remove(self._database_path)
        except OSError:
            raise Exception('Did not remove database')
