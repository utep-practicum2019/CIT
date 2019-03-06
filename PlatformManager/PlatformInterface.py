import json, sys, os
#from PlatformManager import PlatformManager
from TiddlyWiki import TiddlyWiki

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
    #platform_manager = PlatformManager()
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
                "response": response
                }
        
        json_string = json.dumps(data)
        
        return json_string
    
    @staticmethod
    def forward_request(json_object):
        request = PlatformInterface.parse_JSON(json_object)
        
        if(request['platform name'] == "chat"):
            response = PlatformInterface.chat_handle_request(request)
        
        if(request['platform name'] == "wiki"):
            response = PlatformInterface.wiki_handle_request(request)
        
        if(request['platform name'] == "hackathon"):
            response = PlatformInterface.hackathon_handle_request(request)
        
        if(request['platform name'] == "rcr"):
            response = PlatformInterface.rcr_handle_request(request)
                
        return PlatformInterface.format_response(request['requester'], response)
    
#     @staticmethod
#     def chat_handle_request(request):
#         if(request['request'] == "start"):
#             pass
#         
#         if(request['request'] == "stop"):
#             pass
#         
#         return response
    
    @staticmethod
    def wiki_handle_request(request):
        if(request['request'] == "start"):
            response = TiddlyWiki.get_start_command(TiddlyWiki)
        
        if(request['request'] == "stop"):
            response = TiddlyWiki.get_stop_command()
        
        return response
    
#     @staticmethod
#     def hackathon_handle_request(request):
#         if(request['request'] == "start"):
#             pass
#         
#         if(request['request'] == "stop"):
#             pass
#         
#         return response
    
#     @staticmethod
#     def rcr_handle_request(request):
#         if(request['request'] == "start"):
#             pass
#         
#         if(request['request'] == "stop"):
#             pass
#         
#         return response
 
print(PlatformInterface.forward_request("generic.json"))