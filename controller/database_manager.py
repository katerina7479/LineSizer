import sqlite3
from kglobals import _PATH


class DatabaseManager():
    def __init__(self, path=None):
        if path is None:
            self.set_path()
        else:
            self.path = path

    def set_path(self):
        try:
            self.path = _PATH + '/database/project.sqlite3'
        except:
            raise Exception('Cannot initialize database')

    def _create_connection(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

    def save(self):
        self.connection.commit()

    def _close_connection(self):
        self.connection.close()
        self.connection = None
        self.cursor = None

    def create_tables(self, tabledata):
        self._create_connection()
        for tablename, atts in tabledata.iteritems():
            start = 'CREATE TABLE %s (id INTEGER PRIMARY KEY, ' % tablename
            temp = []
            for item in atts:
                mytype = atts[item].upper()
                temp.append('%s %s' % (item, mytype))
            tempstr = ', '.join(temp)
            command = start + tempstr + (');')
            print command
            self.cursor.execute(command)
        self.save()
        self._close_connection()

    def get_table_list(self):
        self._create_connection()
        results = self.cursor.execute(
            'SELECT name FROM sqlite_master\
            WHERE type=\'table\' ORDER BY name;')
        tableslist = results.fetchall()
        self._close_connection()
        return tableslist

    def get_columns(self, tablename):
        self._create_connection()
        command = 'PRAGMA table_info( %s );' % tablename
        results = self.cursor.execute(command)
        columns = results.fetchall()
        self._close_connection()
        colnames = []
        for col in columns:
            colnames.append(col[1])
        return colnames

    def delete(self, tablename, myid):
        self._create_connection()
        command = 'DELETE FROM %s WHERE id == ?;' % tablename
        self.cursor.execute(command, (myid,))
        self.save()
        self._close_connection()
        pass

    def update(self, tablename, row, dic):
        self._create_connection()
        for key, value in dic.iteritems():
            command = 'UPDATE %s SET %s = ? WHERE id = ?;' % (tablename, key)
            self.cursor.execute(command, (value, row))
        self.save()
        self._close_connection()

    def add(self, tablename, dic):
        key = dic.keys()[0]
        command1 = 'INSERT INTO %s (%s) VALUES (?);' % (tablename, key)
        value = dic[key]
        command2 = 'SELECT last_insert_rowid();'
        self._create_connection()
        self.cursor.execute(command1, (value,))
        results = self.cursor.execute(command2)
        myid = results.fetchone()
        self.save()
        self._close_connection()
        self.update(tablename, myid[0], dic)
        return myid[0]

    def _query_table_all(self, tablename):
        columns = self.get_columns(tablename)
        values = self._query_by_cols_all(tablename, columns)
        answerlist = []
        for row in values:
            answerdict = {}
            answerlist.append(answerdict)
            i = 0
            for col in columns:
                answerdict[col] = row[i]
                i += 1
        return answerlist

    def _query_table_row(self, tablename, row):
        columns = self.get_columns(tablename)
        answerdict = {}
        self._create_connection()
        for col in columns:
            command = 'SELECT %s FROM %s WHERE id == ?;' % (col, tablename)
            results = self.cursor.execute(command, (row,))
            answer = results.fetchone()
            answerdict[col] = answer[0]
        self._close_connection()
        return answerdict

    def _query_by_cols_all(self, tablename, colist):
        columns = ', '.join(colist)
        command = 'SELECT %s FROM %s;' % (columns, tablename)
        self._create_connection()
        results = self.cursor.execute(command)
        answerlist = results.fetchall()
        self._close_connection()
        return answerlist

    def _query_cols_where(self, tablename, colist, wheretup):
        columns = ', '.join(colist)
        command = 'SELECT %s FROM %s WHERE %s = ?;' % \
                  (columns, tablename, wheretup[0])
        self._create_connection()
        results = self.cursor.execute(command, (wheretup[1],))
        answerlist = results.fetchall()
        self._close_connection()
        return answerlist

    def _query_where(self, tablename, wheretup):
        command = 'SELECT id FROM %s WHERE %s = ?;' % (tablename, wheretup[0])
        self._create_connection()
        results = self.cursor.execute(command, (wheretup[1],))
        rows = results.fetchall()
        self._close_connection()
        anslist = []
        for row in rows:
            anslist.append(self._query_table_row(tablename, row[0]))
        return anslist

    def query(self, tablename, col=False, cols=False, row=False,
              wcol=False, wval=False):
        if wcol is not False and wval is not False:
            if cols:
                answers = self._query_cols_where(tablename, cols, (wcol, wval))
            elif col:
                answers = self._query_cols_where(tablename,
                                                 [col], (wcol, wval))
            else:
                answers = self._query_where(tablename, (wcol, wval))
        elif row:
            answers = self._query_table_row(tablename, row)
        elif cols:
            answers = self._query_by_cols_all(tablename, cols)
        elif col:
            answers = self._query_by_cols_all(tablename, [col])
        else:
            answers = self._query_table_all(tablename)
        return answers
