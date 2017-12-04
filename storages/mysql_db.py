import os
import MySQLdb


class MySQLDB:

    def __init__(self):
        self.connection_name = os.environ.get('SQL_CONNECTION_NAME')
        self.host = os.environ.get('SQL_HOST')
        self.user = os.environ.get('SQL_USER')
        self.password = os.environ.get('SQL_PASSWORD')
        self.db_name = os.environ.get('SQL_DB')

    def ExecuteSQL(self, sql, params):
        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            cloudsql_unix_socket = os.path.join('/cloudsql', self.connection_name)
            self.db = MySQLdb.connect(unix_socket=cloudsql_unix_socket, user=self.user, passwd=self.password, db=self.db_name)
        else:
            self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.db_name)

        cursor = self.db.cursor()
        cursor.execute(sql, params);
        result = cursor.fetchall();
        return result;

    def Commit(self):
        self.db.commit();
