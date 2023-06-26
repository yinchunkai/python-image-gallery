import psycopg2
import json
from db_secrets import Secrets

class Db():

    def __init__(self):
        json_string = Secrets.get_secret_image_gallery()
        dic = json.loads(json_string)
        self.db_host = dic['host']
        self.db_name = 'postgres' # dic['dbInstanceIdentifier']
        self.db_user = dic['username']
        self.password = dic['password']
        self.connection = None


    def connect(self):
        print("->" + self.db_host +"," + self.db_name + "," + self.db_user + "," + self.password)
        self.connection = psycopg2.connect(host=self.db_host, dbname=self.db_name, user=self.db_user, password=self.password)


    def execute(self, query, args=None):
        cursor = self.connection.cursor()
        if not args:
            cursor.execute(query)
        else:
            cursor.execute(query, args)
        return cursor


if __name__ == '__main__':
    g = Db()
    g.connect()
    res = g.execute('select * from users')
    for row in res:
        print(row)
