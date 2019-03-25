

test_login= {
  "status": "success",
  "data": {
      "authToken": "9HqLlyZOugoStsXCUfD_0YdwnNnunAJF8V47U3QHXSq",
      "userId": "aobEdbYhXfu5hkeqG",
      "me": {
            "_id": "aYjNnig8BEAWeQzMh",
            "name": "Rocket Cat",
            "emails": [
                {
                  "address": "rocket.cat@rocket.chat",
                  "verified": 'false'
                }
            ],
            "status": "offline",
            "statusConnection": "offline",
            "username": "rocket.cat",
            "utcOffset": -3,
            "active": 'true',
            "roles": [
                "admin"
            ],
            "settings": {
                "preferences": {}
              }
        }
   }
}
test_delete_user = {
  "success": 'true'
}

test_register_user= {
  "user": {
    "_id": "nSYqWzZ4GsKTX4dyK",
    "type": "user",
    "status": "offline",
    "active": 'true',
    "name": "Example User",
    "utcOffset": 0,
    "username": "example"
  },
  "success": 'true'
}

test_create_channel = {
   "channel": {
      "_id": "ByehQjC44FwMeiLbX",
      "name": "channelname",
      "t": "c",
      "usernames": [
         "example"
      ],
      "msgs": 0,
      "u": {
         "_id": "aobEdbYhXfu5hkeqG",
         "username": "example"
      },
      "ts": "2016-05-30T13:42:25.304Z"
   },
   "success": 'true'
}

test_delete_channel= {
   "success": 'true'
}

test_create_group = {
  "group": {
    "_id": "NtR6RQ7NvzA9ejecX",
    "name": "testing",
    "t": "p",
    "usernames": [
      "tester"
    ],
    "msgs": 0,
    "u": {
      "_id": "aobEdbYhXfu5hkeqG",
      "username": "tester"
    },
    "ts": "2016-12-09T16:53:06.761Z",
    "ro": 'false',
    "sysMes": 'true',
    "_updatedAt": "2016-12-09T16:53:06.761Z"
  },
  "success": 'true'
}

test_delete_group= {
   "success": 'true'
}

test_anouncement = {
  "announcement": "Test out everything.",
  "success": 'true'
}