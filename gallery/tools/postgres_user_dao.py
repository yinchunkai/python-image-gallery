from user_dao import UserDao
from . import db
from .user import User


class PostgresUserDAO(UserDao):

    def get_users(self):
        result = []
        cursor = db.execute("select user_name, user_password, full_name from users")
        for t in cursor.fetchall():
            result.append(User(t[0], t[1], t[2]))
        return result


    def delete_user(self, username):
        db.execute("delete from users where user_name=%s", (username,))