import unittest
import requests

from AccountManager.user_manager import UserManager, get_user, create_user
from AccountManager.user import User

from tests.Accounts.dummy_data import user1, updated_user1, user2, bare_user
from tests.Accounts.dummy_data import connection_url, users


class UserCreateTest(unittest.TestCase):
    def tearDown(self):
        UserManager.delete_user(user1['username'])

    def test_create_user(self):
        create_user(**user1)
        user = get_user(user1['username']).to_dict()
        self.assertDictEqual(user, user1)


class UserGetTest(unittest.TestCase):
    def setUp(self):
        create_user(**user1)

    def tearDown(self):
        UserManager.delete_user(user1['username'])

    def test_get_user(self):
        user = get_user(user1['username']).to_dict()
        self.assertDictEqual(user, user1)

    def test_get_unknown_user(self):
        self.assertIsNone(get_user('unknown_user'))

    def test_get_invalid_param(self):
        self.assertIsNone(get_user(1))


class UserUpdateTest(unittest.TestCase):
    def setUp(self):
        create_user(**user1)
        create_user(**user2)
        requests.patch(connection_url, json=users[:2])

    def tearDown(self):
        UserManager.delete_user(user1['username'])
        UserManager.delete_user(user2['username'])

    def test_update_user(self):
        # update everything but keep the username
        UserManager.update_user(user1['username'], User(**updated_user1))
        user = get_user(user1['username']).to_dict()
        self.assertDictEqual(user, updated_user1)

    def test_username_taken(self):
        self.assertFalse(UserManager.update_user(user1['username'], User(**user2)))

    def test_update_nonexistent(self):
        self.assertFalse(UserManager.update_user('notauser', User(**bare_user)))

    def test_update_invalid_param(self):
        self.assertFalse(UserManager.update_user(5, User('user')))


class UserUpdateTest2(unittest.TestCase):
    def setUp(self):
        create_user(**user1)
        create_user(**user2)
        requests.patch(connection_url, json=users[:2])

    def tearDown(self):
        UserManager.delete_user(user1['username'])
        UserManager.delete_user(user2['username'])
        UserManager.delete_user('updated_username')

    def test_update_new_username(self):
        # update to a new username
        before = User(**updated_user1)
        before.username = 'updated_username'
        UserManager.update_user(user1['username'], before)
        after = get_user(before.username)
        self.assertDictEqual(after.to_dict(), before.to_dict())

    def test_deleted_prev(self):
        # update to a new username
        user = User(**updated_user1)
        user.username = 'updated_username'
        UserManager.update_user(user1['username'], user)
        self.assertIsNone(get_user(user1['username']))


class UserDeleteTest(unittest.TestCase):
    def setUp(self):
        create_user(**user1)
        requests.patch(connection_url, json=[users[0]])

    def test_delete_user(self):
        UserManager.delete_user(user1['username'])
        self.assertIsNone(get_user(user1['username']))


if __name__ == '__main__':
    unittest.main()
