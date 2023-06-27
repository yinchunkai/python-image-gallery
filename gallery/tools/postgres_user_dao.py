from user_dao import UserDao
from db import Db
from user import User


class PostgresUserDAO(UserDao):

    def get_user_by_username(self, username):
        user = None
        d = Db()
        d.connect()
        cursor = d.execute("select user_name, user_password, full_name from users where user_name=%s", (username,))
        for t in cursor:
            user = User(t[0], t[1], t[2])
        return user


    def delete_user(self, username):
        Db.execute("delete from users where user_name=%s", (username,))
