import unittest
import uuid
import mock
import logging
import pprint
import requests

from rocketchat_API.APIExceptions.RocketExceptions import RocketAuthenticationException, RocketMissingParamException
from rocketchat_API.rocketchat import RocketChat
#from .data import test_login
from Tests.data import test_login


class TestServer(unittest.TestCase):
    def setUp(self):
        self.rocket = RocketChat()
        self.user = 'user1'
        self.password = 'password'
        self.email = 'email@domain.com'
        self.rocket.users_register(
            email=self.email, name=self.user, password=self.password, username=self.user)
        self.rocket = RocketChat(self.user, self.password)

    proxy_dict = {
        "http": "http://localhost:3000",
        "https": "https://localhost:3001",
    }

    # Create a RocketChat object and login on the specified server:
    rocket = RocketChat('Admin', 'chat.service', server_url='http://www.chat.service', proxies=None)

    def test_login_user(self):
        login = self.rocket.login(self.user, self.password).json()
        with self.assertRaises(RocketAuthenticationException):
            self.rocket.login(self.user, 'bad_password')
        self.assertEqual(login.get('status'), 'success')
        self.assertTrue('authToken' in login.get('data'))
        self.assertTrue('user_Id' in login.get('data'))

    def test_users_register_update_delete(self):
        users_register = self.rocket.users_register(email='email2@domain.com', name='user2', password=self.password,
                                                    username='user2').json()
        self.assertTrue(users_register.get('success'), users_register.get('error'))

        user_id = users_register.get('user').get('_id')
        users_update = self.rocket.users_update(user_id, email='anewemailhere@domain.com', name='newname',
                                                password=self.password, username='newusername').json()
        self.assertTrue(users_update.get('success'), 'Can not update user')
        self.assertEqual(users_update.get('user').get(
            'emails')[0].get('address'), 'anewemailhere@domain.com')


class TestChannels(unittest.TestCase):
    def setUp(self):
        self.rocket = RocketChat()
        self.user = 'user1'
        self.password = 'password'
        self.email = 'email@domain.com'
        self.rocket.users_register(
            email=self.email, name=self.user, password=self.password, username=self.user)
        self.rocket.channels_add_owner('GENERAL', username=self.user)
        self.rocket = RocketChat(self.user, self.password)

        testuser = self.rocket.users_info(username='testuser1').json()
        if not testuser.get('success'):
            testuser = self.rocket.users_create(
                'testuser1@domain.com', 'testuser1', 'password', 'testuser1').json()
            if not testuser.get('success'):
                self.fail("can't create test user")

        self.testuser_id = testuser.get('user').get('_id')

    def tearDown(self):
        self.rocket.users_delete(self.testuser_id)

    def test_channels_create_delete(self):
        name = str(uuid.uuid1())
        channels_create = self.rocket.channels_create(name).json()
        self.assertTrue(channels_create.get('success'))
        self.assertEqual(name, channels_create.get('channel').get('name'))
        channels_delete = self.rocket.channels_delete(channel=name).json()
        self.assertTrue(channels_delete.get('success'))
        channels_create = self.rocket.channels_create(name).json()
        self.assertTrue(channels_create.get('success'))
        room_id = channels_create.get('channel').get('_id')
        channels_delete = self.rocket.channels_delete(room_id=room_id).json()
        self.assertTrue(channels_delete.get('success'))

        with self.assertRaises(RocketMissingParamException):
            self.rocket.channels_delete()

    def test_channels_set_announcement(self):
        announcement = str(uuid.uuid1())
        channels_set_announcement = self.rocket.channels_set_announcement(
            'GENERAL', announcement).json()
        self.assertTrue(channels_set_announcement.get('success'))
        self.assertEqual(channels_set_announcement.get('announcement'), announcement,
                         'Topic does not match')

class TestGroups(unittest.TestCase):
    def setUp(self):
        self.rocket = RocketChat()
        self.user = 'user1'
        self.password = 'password'
        self.email = 'email@domain.com'
        self.rocket.users_register(
            email=self.email, name=self.user, password=self.password, username=self.user)
        self.rocket = RocketChat(self.user, self.password)
        testuser = self.rocket.users_info(username='testuser1').json()
        if not testuser.get('success'):
            testuser = self.rocket.users_create(
                'testuser1@domain.com', 'testuser1', 'password', 'testuser1').json()
            if not testuser.get('success'):
                self.fail("can't create test user")

        self.testuser_id = testuser.get('user').get('_id')
        self.test_group_name = str(uuid.uuid1())
        self.test_group_id = self.rocket.groups_create(
            self.test_group_name).json().get('group').get('_id')

    def tearDown(self):
        self.rocket.users_delete(self.testuser_id)

    def test_groups_create_delete(self):
        name = str(uuid.uuid1())
        groups_create = self.rocket.groups_create(name).json()
        self.assertTrue(groups_create.get('success'))
        self.assertEqual(name, groups_create.get('group').get('name'))
        groups_delete = self.rocket.groups_delete(group=name).json()
        self.assertTrue(groups_delete.get('success'))
        groups_create = self.rocket.groups_create(name).json()
        self.assertTrue(groups_create.get('success'))
        room_id = groups_create.get('group').get('_id')
        groups_delete = self.rocket.groups_delete(room_id=room_id).json()
        self.assertTrue(groups_delete.get('success'))

        with self.assertRaises(RocketMissingParamException):
            self.rocket.groups_delete()


if __name__ == '__main__':
    unittest.main(warnings='ignore')

