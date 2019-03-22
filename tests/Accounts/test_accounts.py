import unittest
import requests
from parameterized import parameterized

from AccountManager.user_manager import get_user, create_user
from AccountManager.user import User
from AccountManager.group_manager import get_group, create_group, get_next_id
from AccountManager.group import Group
from AccountManager.account_manager import AccountManager

from tests.Accounts.dummy_data import user1, updated_user1, user2, bare_user
from tests.Accounts.dummy_data import file_content, file_users, test_filepath
from tests.Accounts.dummy_data import updated_group, group_count, user_count
from tests.Accounts.dummy_data import connection_url, users


class AccountUserUpdateTest(unittest.TestCase):
    def setUp(self):
        create_user(**user1)
        create_user(**user2)
        requests.patch(connection_url, json=users[:2])

    def tearDown(self):
        self.assertTrue(AccountManager.delete_user(user1['username']))
        self.assertTrue(AccountManager.delete_user(user2['username']))

    def test_update_user(self):
        # update everything but keep the username
        AccountManager.update_user(user1['username'], User(**updated_user1))
        user = get_user(user1['username']).to_dict()
        self.assertDictEqual(user, updated_user1)

    def test_username_taken(self):
        self.assertFalse(AccountManager.update_user(user1['username'], User(**user2)))

    def test_update_nonexistent(self):
        self.assertFalse(AccountManager.update_user('notauser', User(**bare_user)))

    def test_update_invalid_param(self):
        self.assertFalse(AccountManager.update_user(5, User('user')))


class AccountUserUpdateTest2(unittest.TestCase):
    def setUp(self):
        create_user(**user1)
        create_user(**user2)
        requests.patch(connection_url, json=users[:2])

    def tearDown(self):
        AccountManager.delete_user('updated_username')
        AccountManager.delete_user(user2['username'])
        AccountManager.delete_user(user1['username'])

    def test_update_new_username(self):
        # update to a new username
        before = User(**updated_user1)
        before.username = 'updated_username'
        AccountManager.update_user(user1['username'], before)
        after = get_user(before.username)
        self.assertDictEqual(after.to_dict(), before.to_dict())

    def test_deleted_prev(self):
        # update to a new username
        user = User(**updated_user1)
        user.username = 'updated_username'
        AccountManager.update_user(user1['username'], user)
        self.assertIsNone(get_user(user1['username']))


class UserDeleteTest(unittest.TestCase):
    def setUp(self):
        create_user(**user1)
        requests.patch(connection_url, json=[users[0]])

    def test_delete_user(self):
        AccountManager.delete_user(user1['username'])
        self.assertIsNone(get_user(user1['username']))


class AccountGroupUpdateTest(unittest.TestCase):
    def setUp(self):
        global start_id
        start_id = get_next_id()
        AccountManager.create_groups(1, 2)

    def tearDown(self):
        AccountManager.delete_group(start_id)

    def test_update_nonexistent(self):
        self.assertFalse(AccountManager.update_group(102, Group(**updated_group)))

    def test_change_id(self):
        self.assertFalse(AccountManager.update_group(start_id, Group(**updated_group)))


class AccountGroupImportTest(unittest.TestCase):
    """
        This test case will fail the next time it runs if tearDown does not complete properly.
    """
    def tearDown(self):
        for line in file_users:
            current = get_user(line[0]).group_id
            AccountManager.delete_group(current)

    def test_import(self):
        with open(test_filepath, 'w') as f:
            f.writelines(file_content)
        self.assertTrue(AccountManager.create_groups(filepath=test_filepath))


class AccountGroupImportContentTest(unittest.TestCase):
    def setUp(self):
        with open(test_filepath, 'w') as f:
            f.writelines(file_content)
        global start_id
        start_id = get_next_id()
        AccountManager.create_groups(filepath=test_filepath)

    def tearDown(self):
        for line in file_users:
            current = get_user(line[0]).group_id
            AccountManager.delete_group(current)

    @parameterized.expand([user for user in file_users[0]])
    def test_member_group1(self, username):
        self.assertEquals(get_user(username).group_id, start_id)

    @parameterized.expand([user for user in file_users[1]])
    def test_member_group2(self, username):
        self.assertEquals(get_user(username).group_id, start_id + 1)

    @parameterized.expand([user for user in file_users[0]])
    def test_group1_members(self, username):
        group = get_group(start_id)
        self.assertTrue(username in group.members)

    @parameterized.expand([user for user in file_users[1]])
    def test_group2_members(self, username):
        group = get_group(start_id + 1)
        self.assertTrue(username in group.members)


class AccountGenerateGroupTest(unittest.TestCase):
    def tearDown(self):
        for i in range(group_count):
            AccountManager.delete_group(start_id + i)

    def test_create_groups(self):
        global start_id
        start_id = get_next_id()
        self.assertTrue(AccountManager.create_groups(group_count, user_count))


class AccountGenerateGroupContentTest(unittest.TestCase):
    def setUp(self):
        global start_id
        start_id = get_next_id()
        self.assertTrue(AccountManager.create_groups(group_count, user_count))

    def tearDown(self):
        for i in range(group_count):
            AccountManager.delete_group(start_id + i)

    @parameterized.expand((g,) for g in range(group_count))
    def test_user_count(self, g):
        group = get_group(start_id + g)
        self.assertEqual(len(group.members), user_count)

    @parameterized.expand((u, ) for u in range(user_count))
    def test_user_group1(self, u):
        group = get_group(start_id)
        user = get_user(group.members[u])
        self.assertEqual(user.group_id, group.group_id)

    @parameterized.expand((u,) for u in range(user_count))
    def test_user_group2(self, u):
        group = get_group(start_id + 1)
        user = get_user(group.members[u])
        self.assertEqual(user.group_id, group.group_id)


class AccountDeleteGroupTest(unittest.TestCase):
    def setUp(self):
        requests.patch(connection_url, json=users)
        create_group(1000, users)

    def test_group_delete(self):
        self.assertTrue(AccountManager.delete_group(1000))

    def test_group_delete(self):
        AccountManager.delete_group(1000)
        self.assertIsNone(get_group(1000))

    @parameterized.expand(user[0] for user in users)
    def test_members_deleted(self, username):
        AccountManager.delete_group(1000)
        self.assertIsNone(get_user(username))



