from sqlite3 import Connection, connect


class UsersCRUD:

    def __init__(self, connection: Connection):
        self._connection = connection

    def setup(self):
        self._connection.execute("""CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY);""")

    def create(self, username: str) -> str:
        try:
            self._connection.execute("INSERT INTO users VALUES (?)", (username,))
        except BaseException:
            raise ValueError('Unique violation')
        else:
            return username
        

class UsersService:

    def __init__(self, users_crud: UsersCRUD) -> None:
        self._users_crud = users_crud
    
    def create_user(self, username: str) -> str:
        username_to_create = username
        is_created = False
        retries = 0
        while not is_created:
            try:
                self._users_crud.create(username_to_create)
            except ValueError as e:
                retries += 1
                username_to_create = username + str(retries)
            else:
                is_created = True
        if username_to_create == username:
            return "OK"
        return username_to_create


def main():
    connection = connect('users.db')
    users_crud = UsersCRUD(connection)
    users_crud.setup()
    users_service = UsersService(users_crud)
    usernames_number = int(input())
    usernames_to_create = [input(f'Enter username [{i + 1}|{usernames_number}]: ') for i in range(usernames_number)]
    for username_to_create in usernames_to_create:
        created_username = users_service.create_user(username_to_create)
        print(created_username)

    connection.close()
    print('closed db connection')


if __name__ == "__main__":
    main()
    