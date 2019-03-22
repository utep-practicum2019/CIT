import unittest
import requests
from parameterized import parameterized

from AccountManager.user_manager import UserManager, get_user, create_user
from AccountManager.group_manager import GroupManager, get_group, create_group, get_next_id
from AccountManager.group import Group

from tests.Accounts.dummy_data import file_content, file_users, test_filepath
from tests.Accounts.dummy_data import updated_group, group_count, user_count
from tests.Accounts.dummy_data import connection_url, users


class GroupCreateTest(unittest.TestCase):
    def setUp(self):
        requests.patch(connection_url, json=users)

    def tearDown(self):
        GroupManager.delete_group(1000)

    def test_create_group(self):
        self.assertTrue(create_group(1000, users))


class GroupCreateTest1(unittest.TestCase):
    def setUp(self):
        requests.patch(connection_url, json=users)
        create_group(1000, users)

    def tearDown(self):
        GroupManager.delete_group(1000)

    @parameterized.expand([user[0] for user in users])
    def test_group_members(self, username):
        group = get_group(1000)
        self.assertTrue(username in group.members)

    @parameterized.expand([user[0] for user in users])
    def test_user_group(self, username):
        self.assertEquals(get_user(username).group_id, 1000)

    def test_create_duplicate(self):
        self.assertFalse(create_group(1000, users))

    def test_create_duplicate_user(self):
        self.assertFalse(create_group(1002, [users[2]]))


class GroupGetTest(unittest.TestCase):
    def setUp(self):
        requests.patch(connection_url, json=users)
        create_group(1000, users)

    def tearDown(self):
        GroupManager.delete_group(1000)

    def test_get_group(self):
        self.assertIsNotNone(get_group(1000))

    def test_get_no_group(self):
        self.assertFalse(get_group(777))


class GroupFileTest(unittest.TestCase):
    def test_nonexistent(self):
        self.assertFalse(GroupManager.create_groups(filepath="notafile.txt"))

    def test_empty(self):
        with open(test_filepath, 'w') as f:
            f.write("")
        self.assertFalse(GroupManager.create_groups(filepath=test_filepath))

    def test_whitespace(self):
        with open(test_filepath, 'w') as f:
            f.write("          ")
        self.assertFalse(GroupManager.create_groups(filepath=test_filepath))

    def test_duplicate_in_file(self):
        with open(test_filepath, 'w') as f:
            content = ["user2 ", "user3\n", "user2"]
            f.writelines(content)
        self.assertFalse(GroupManager.create_groups(filepath=test_filepath))


class GroupFileTest1(unittest.TestCase):
    def setUp(self):
        requests.patch(connection_url, json=[users[0]])
        create_user(users[0][0], users[0][1])

    def tearDown(self):
        UserManager.delete_user(users[0][0])

    def test_duplicate_user(self):
        with open(test_filepath, 'w') as f:
            content = ["user2 ", "user3\n", users[0][0]]
            f.writelines(content)
        self.assertFalse(GroupManager.create_groups(filepath=test_filepath))


class GroupImportTest(unittest.TestCase):
    """
        This test case will fail the next time it runs if tearDown does not complete properly.
    """
    def tearDown(self):
        for line in file_users():
            current = get_user(line[0]).group_id
            GroupManager.delete_group(current)

    def test_import(self):
        with open(test_filepath, 'w') as f:
            f.writelines(file_content)
        self.assertTrue(GroupManager.create_groups(filepath=test_filepath))


class GroupImportContentTest(unittest.TestCase):
    def setUp(self):
        with open(test_filepath, 'w') as f:
            f.writelines(file_content)
        global start_id
        start_id = get_next_id()
        GroupManager.create_groups(filepath=test_filepath)

    def tearDown(self):
        for line in file_users():
            current = get_user(line[0]).group_id
            GroupManager.delete_group(current)

    @parameterized.expand([user for user in file_users()[0]])
    def test_member_group1(self, username):
        self.assertEquals(get_user(username).group_id, start_id)

    @parameterized.expand([user for user in file_users()[1]])
    def test_member_group2(self, username):
        self.assertEquals(get_user(username).group_id, start_id + 1)

    @parameterized.expand([user for user in file_users()[0]])
    def test_group1_members(self, username):
        group = get_group(start_id)
        self.assertTrue(username in group.members)

    @parameterized.expand([user for user in file_users()[1]])
    def test_group2_members(self, username):
        group = get_group(start_id + 1)
        self.assertTrue(username in group.members)


class GroupGenerationTest(unittest.TestCase):
    def tearDown(self):
        for i in range(group_count):
            GroupManager.delete_group(start_id + i)

    def test_create_groups(self):
        global start_id
        start_id = get_next_id()
        self.assertTrue(GroupManager.create_groups(group_count, user_count))


class GroupGenerationContentTest(unittest.TestCase):
    def setUp(self):
        global start_id
        start_id = get_next_id()
        self.assertTrue(GroupManager.create_groups(group_count, user_count))

    def tearDown(self):
        for i in range(group_count):
            GroupManager.delete_group(start_id + i)

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


class GroupUpdateTest(unittest.TestCase):
    def setUp(self):
        global start_id
        start_id = get_next_id()
        GroupManager.create_groups(1, 2)

    def tearDown(self):
        GroupManager.delete_group(start_id)

    def test_update_nonexistent(self):
        self.assertFalse(GroupManager.update_group(102, Group(**updated_group)))

    def test_change_id(self):
        self.assertFalse(GroupManager.update_group(start_id, Group(**updated_group)))


class GroupDeleteTest(unittest.TestCase):
    def setUp(self):
        requests.patch(connection_url, json=users)
        create_group(1000, users)

    def test_group_delete(self):
        self.assertTrue(GroupManager.delete_group(1000))

    def test_group_delete(self):
        GroupManager.delete_group(1000)
        self.assertIsNone(get_group(1000))

    @parameterized.expand(user[0] for user in users)
    def test_members_deleted(self, username):
        GroupManager.delete_group(1000)
        self.assertIsNone(get_user(username))



