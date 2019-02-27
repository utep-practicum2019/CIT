from group import Group
 
class GroupManager:
    data1 = {'group_id':1, 'min_members':11, 'max_members':111}
    data2 = {'group_id':2, 'min_members':22, 'max_members':222}
    data3 = {'group_id':3, 'min_members':33, 'max_members':333}
    database = {1:data1, 2:data2, 3:data3}

    
    @staticmethod
    def get_group(group_id):
        # TODO get info from the database
        # temporary solution
        data = GroupManager.database
        
        if data[group_id] is None:
            # group does not exist
            return None 
        assert data[group_id]['group_id'] == group_id
        return Group(**data[group_id])

    @staticmethod
    def get_groups():
        # TODO get info from database
        # temporary solution
        data = GroupManager.database

        groups = []
        for n in data.keys():
            groups.append(data[n]['group_id'])
        return groups
        
    @staticmethod
    def create_group(group_id, **kwargs):
        # Check if group already exists
        if GroupManager.get_group(group_id)is None:
            # TODO store group in the database
            # temporary solution
            data = GroupManager.database
            data[group_id] = {'group_id':group_id, **kwargs}
            
            return Group(group_id, **kwargs)
        # group_id is already used
        return None

    @staticmethod
    def delete_group(group_id):
        return None

    @staticmethod
    def add_user(group_id, username):
        return None

    @staticmethod
    def remove_user(group_id, username):
        return None

    @staticmethod
    def add_platform(group_id, platform):
        return None

    @staticmethod
    def remove_platform(group_id, platform):
        return None

    @staticmethod
    def add_chat(group_id, chat_id):
        return None

    @staticmethod
    def remove_chat(group_id):
        return None
