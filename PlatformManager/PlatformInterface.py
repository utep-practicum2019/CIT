import json
from Platforms.TiddlyWiki import TiddlyWiki
from Platforms.RocketChat import RocketChat

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class PlatformInterface():
    cit_IP = "http://127.0.0.1:"
        
    @staticmethod
    def parse_JSON(json_object):
        with open(json_object, "r") as j_object:
            parsed_input = json.load(j_object)
        
        return parsed_input
    
    @staticmethod
    def format_response(destination, response):
        data = {
                "destination": destination,
                "response": response[0]
                }
        
        json_string = json.dumps(data)
        
        return json_string
    
    #Create
    @staticmethod
    def post(json_object):
        pass
    
    #Read
    @staticmethod
    def get(json_object):
        request = PlatformInterface.parse_JSON(json_object)
        response = []
        
        if(request['request'] == "start"):
            if(request['platform'] == "chat"):
                response.append(RocketChat.get_start_command(RocketChat))
                
            if(request['platform'] == "wiki"):
                response.append(TiddlyWiki.get_start_command(TiddlyWiki))
        
        if(request['request'] == "stop"):
            if(request['platform'] == "chat"):
                response.append(RocketChat.get_stop_command(RocketChat))
                
            if(request['platform'] == "wiki"):
                response.append(TiddlyWiki.get_stop_command(TiddlyWiki))
                
        if(request['request'] == "name"):
            if(request['platform'] == "chat"):
                response.append(RocketChat.getPlatformName(RocketChat))
                
            if(request['platform'] == "wiki"):
                response.append(TiddlyWiki.getPlatformName(TiddlyWiki))
                
        if(request['request'] == "installation"):
            if(request['platform'] == "chat"):
                response.append(RocketChat.getPlatformInstallation(RocketChat))
                
            if(request['platform'] == "installation"):
                response.append(TiddlyWiki.getPlatformInstallation(TiddlyWiki))
                
        if(request['request'] == "version"):
            if(request['platform'] == "chat"):
                response.append(RocketChat.getPlatformVersion(RocketChat))
                
            if(request['platform'] == "wiki"):
                response.append(TiddlyWiki.getPlatformVersion(TiddlyWiki))
                
        if(request['request'] == "id"):
            if(request['platform'] == "chat"):
                response.append(RocketChat.getPlatformID(RocketChat))
                
            if(request['platform'] == "wiki"):
                response.append(TiddlyWiki.getPlatformID(TiddlyWiki))
                
        if(request['request'] == "name"):
            if(request['platform'] == "chat"):
                response.append(RocketChat.getPlatformName(RocketChat))
                
            if(request['platform'] == "wiki"):
                response.append(TiddlyWiki.getPlatformName(TiddlyWiki))
                
        if(request['request'] == "ip/port"):
            if(request['platform'] == "chat"):
                response.append(RocketChat.getIpPort(RocketChat))
                
            if(request['platform'] == "wiki"):
                response.append(TiddlyWiki.getIpPort(TiddlyWiki))
                
        if(request['request'] == "link"):
            if(request['platform'] == "chat"):
                response.append(RocketChat.getLink(RocketChat))
                
            if(request['platform'] == "wiki"):
                response.append(TiddlyWiki.getLink(TiddlyWiki))
                
        if(request['request'] == "subplatforms"):
            if(request['platform'] == "chat"):
                response.append(RocketChat.get_sub_platforms(RocketChat))
                
            if(request['platform'] == "wiki"):
                response.append(TiddlyWiki.get_sub_platforms(TiddlyWiki))
                
        return PlatformInterface.format_response(request['requester'], response)
    
    #Update
    @staticmethod
    def put(json_object):
        pass
    
    @staticmethod
    def delete(json_object):
        pass
     
#print(PlatformInterface.get("Tests/JSON_Test_Files/test.json"))