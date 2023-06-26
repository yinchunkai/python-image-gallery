from db import Db
import psycopg2


class UserAdmin():

    def __init__(self):
        self.db = Db()
        self.db.connect()

    def list_accounts(self):
        res = self.db.execute('select * from users')
        print(f'username\tpassword\tfull name')
        print('----------------------------------------')
        accts = []
        for row in res:
            print(f'{row[0]}\t\t{row[1]}\t\t{row[2]}')
            dict = {"username":row[0], "password":row[1], "fullname":row[2]}
            accts.append(dict)
        return accts

    def add_account(self, user_name, passwd, full_name):
        try:
            res = self.db.execute('INSERT INTO users VALUES (%s, %s, %s)', (user_name, passwd, full_name))
            self.db.connection.commit()
        except psycopg2.errors.UniqueViolation as e:
            print(f"Error: user with username {user_name} already exists")

    def edit_account(self, user_name, passwd, full_name):

        self.db.execute('UPDATE users SET user_password = %s, full_name = %s where user_name = %s',
                         (passwd, full_name, user_name))
        self.db.connection.commit()

    def del_account(self, user_name):
        self.db.execute('DELETE from users WHERE user_name = %s', (user_name))
        self.db.connection.commit()
        print('deleted.')


if __name__ == '__main__':
    userAdmin = UserAdmin()
    userAdmin.list_accounts()
