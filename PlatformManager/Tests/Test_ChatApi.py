import unittest
import uuid

from rocketchat_API.APIExceptions.RocketExceptions import RocketAuthenticationException, RocketMissingParamException
from rocketchat_API.rocketchat import RocketChat


class TestServer(unittest.TestCase):
    def setUp(self):
        self.rocket = RocketChat()
        self.user = 'user1'
        self.password = 'password'
        self.email = 'email@domain.com'
        self.rocket.users_register(
            email=self.email, name=self.user, password=self.password, username=self.user)
        self.rocket = RocketChat(self.user, self.password)

    def test_info(self):
        info = self.rocket.info().json()
        self.assertTrue('info' in info)
        self.assertTrue(info.get('success'))

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.rocket = RocketChat()
        self.user = 'user1'
        self.password = 'password'
        self.email = 'email@domain.com'
        self.rocket.users_register(
            email=self.email, name=self.user, password=self.password, username=self.user)
        self.rocket = RocketChat(self.user, self.password)
        user2_exists = self.rocket.users_info(
            username='user2').json().get('success')
        if user2_exists:
            user_id = self.rocket.users_info(
                username='user2').json().get('user').get('_id')
            self.rocket.users_delete(user_id)

    def test_login(self):
        login = self.rocket.login(self.user, self.password).json()

        with self.assertRaises(RocketAuthenticationException):
            self.rocket.login(self.user, 'bad_password')

        self.assertEqual(login.get('status'), 'success')
        self.assertTrue('authToken' in login.get('data'))
        self.assertTrue('userId' in login.get('data'))

    def test_users_info(self):
        login = self.rocket.login(self.user, self.password).json()
        user_id = login.get('data').get('userId')

        users_info_by_id = self.rocket.users_info(user_id=user_id).json()
        self.assertTrue(users_info_by_id.get('success'))
        self.assertEqual(users_info_by_id.get('user').get('_id'), user_id)

        users_info_by_name = self.rocket.users_info(username=self.user).json()
        self.assertTrue(users_info_by_name.get('success'))
        self.assertEqual(users_info_by_name.get('user').get('name'), self.user)

        with self.assertRaises(RocketMissingParamException):
            self.rocket.users_info()


    def test_users_create_update_delete(self):
        users_create = self.rocket.users_create(email='email2@domain.com', name='user2', password=self.password,
                                                username='user2').json()
        self.assertTrue(users_create.get('success'), users_create.get('error'))

        user_id = users_create.get('user').get('_id')
        users_update = self.rocket.users_update(user_id, email='anewemailhere@domain.com', name='newname',
                                                password=self.password, username='newusername').json()
        self.assertTrue(users_update.get('success'), 'Can not update user')
        self.assertEqual(users_update.get('user').get(
            'emails')[0].get('address'), 'anewemailhere@domain.com')

class TestChat(unittest.TestCase):
    def test_chat_post_update_delete_message(self):
        chat_post_message = self.rocket.chat_post_message(
            "hello", channel='GENERAL').json()
        self.assertEqual(chat_post_message.get('channel'), 'GENERAL')
        self.assertEqual(chat_post_message.get('message').get('msg'), 'hello')
        self.assertTrue(chat_post_message.get('success'))

        with self.assertRaises(RocketMissingParamException):
            self.rocket.chat_post_message(text='text')

        msg_id = chat_post_message.get('message').get('_id')
        chat_get_message = self.rocket.chat_get_message(msg_id=msg_id).json()
        self.assertEqual(chat_get_message.get('message').get('_id'), msg_id)

        chat_update = self.rocket.chat_update(room_id=chat_post_message.get('channel'),
                                              msg_id=chat_post_message.get(
                                                  'message').get('_id'),
                                              text='hello again').json()

        self.assertEqual(chat_update.get('message').get('msg'), 'hello again')
        self.assertTrue(chat_update.get('success'))

        chat_delete = self.rocket.chat_delete(room_id=chat_post_message.get('channel'),
                                              msg_id=chat_post_message.get('message').get('_id')).json()
        self.assertTrue(chat_delete.get('success'))

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

    def test_channels_list(self):
        channels_list = self.rocket.channels_list().json()
        self.assertTrue(channels_list.get('success'))
        self.assertIn('channels', channels_list)

    def test_channels_info(self):
        channels_info = self.rocket.channels_info(room_id='GENERAL').json()
        self.assertTrue(channels_info.get('success'))
        self.assertIn('channel', channels_info)
        self.assertEqual(channels_info.get('channel').get('_id'), 'GENERAL')
        channel_name = channels_info.get('channel').get('name')
        channels_info = self.rocket.channels_info(channel=channel_name).json()
        self.assertTrue(channels_info.get('success'))
        self.assertIn('channel', channels_info)
        self.assertEqual(channels_info.get('channel').get('_id'), 'GENERAL')
        self.assertEqual(channels_info.get(
            'channel').get('name'), channel_name)

        with self.assertRaises(RocketMissingParamException):
            self.rocket.channels_info()

    def test_channels_history(self):
        channels_history = self.rocket.channels_history(
            room_id='GENERAL').json()
        self.assertTrue(channels_history.get('success'))
        self.assertIn('messages', channels_history)

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

    def test_channels_members(self):
        channels_members = self.rocket.channels_members(
            room_id='GENERAL').json()
        self.assertTrue(channels_members.get('success'))
        channels_members = self.rocket.channels_members(
            channel='general').json()
        self.assertTrue(channels_members.get('success'))

        with self.assertRaises(RocketMissingParamException):
            self.rocket.channels_members()

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

    def test_groups_list_all(self):
        groups_list = self.rocket.groups_list_all().json()
        self.assertTrue(groups_list.get('success'))
        self.assertIn('groups', groups_list)

    def test_groups_info(self):
        groups_info_by_id = self.rocket.groups_info(
            room_id=self.test_group_id).json()
        self.assertTrue(groups_info_by_id.get('success'))
        self.assertIn('group', groups_info_by_id)
        self.assertEqual(groups_info_by_id.get(
            'group').get('_id'), self.test_group_id)

        groups_info_by_name = self.rocket.groups_info(
            room_name=self.test_group_name).json()
        self.assertTrue(groups_info_by_name.get('success'))
        self.assertIn('group', groups_info_by_name)
        self.assertEqual(groups_info_by_name.get(
            'group').get('_id'), self.test_group_id)

        with self.assertRaises(RocketMissingParamException):
            self.rocket.groups_info()

    def test_groups_history(self):
        groups_history = self.rocket.groups_history(
            room_id=self.test_group_id).json()
        self.assertTrue(groups_history.get('success'))
        self.assertIn('messages', groups_history)

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

    def test_groups_invite(self):
        groups_invite = self.rocket.groups_invite(
            self.test_group_id, self.testuser_id).json()
        self.assertTrue(groups_invite.get('success'))

    def test_groups_kick(self):
        id_group_created = self.rocket.groups_create(
            str(uuid.uuid1())).json().get('group').get('_id')
        groups_invite = self.rocket.groups_invite(
            id_group_created, self.testuser_id).json()
        self.assertTrue(groups_invite.get('success'))
        groups_kick = self.rocket.groups_kick(
            id_group_created, self.testuser_id).json()
        self.assertTrue(groups_kick.get('success'))

    def test_groups_members(self):
        groups_members = self.rocket.groups_members(
            room_id=self.test_group_id).json()
        self.assertTrue(groups_members.get('success'))
        groups_members = self.rocket.groups_members(
            group=self.test_group_name).json()
        self.assertTrue(groups_members.get('success'))

        with self.assertRaises(RocketMissingParamException):
            self.rocket.groups_members()

if __name__ == '__main__':
    unittest.main(warnings='ignore')