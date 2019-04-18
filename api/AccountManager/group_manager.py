
        created = create_user(user['username'], user['password'], remote_ip=user['pptpIP'], group_id=group_id)
        if not created:
            print('Unable to create user ', user['username'])
            return False

        current.platforms.remove(platform_id)
        return GroupManager.update_group(group_id, current)
