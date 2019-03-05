import json
from HackathonManager import HackathonManager
from RapidCyberRangeManager import RapidCyberRangeManager

""" 
        @authors:
            Alejandro Balderrama
            Nadia Karichev
            Hector Cervantes
        @description
            This class represents the platfrom manager. 
            The plugin manager will be able to add, delete, start, stop, and configure services(platfroms).
    """

class PlatformManager():
    hackathon = HackathonManager()
    rcr = RapidCyberRangeManager()
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
        request = PlatformManager.parse_JSON(json_object)
        
        if(request['type'] == "start"):
            if(request['platform name'] == "hackathon"):
                hackathon_response = PlatformManager.hackathon.start_platform()
                chat_response = PlatformManager.hackathon.chat.start_platform_for_hackathon()
                wiki_response = PlatformManager.hackathon.wiki.start_platform_for_hackathon()
                
                if(hackathon_response == 200 and chat_response == 200 and wiki_response == 200):
                    response = 200
                else:
                    response = 0
                
            if(request['platform name'] == "rcr"):
                rcr_response = PlatformManager.rcr.start_platform()
                chat_response = PlatformManager.rcr.chat.start_platform_for_rcr()
                wiki_response = PlatformManager.rcr.wiki.start_platform_for_rcr()

                if(rcr_response == 200 and chat_response == 200 and wiki_response == 200):
                    response = 200
                else:
                    response = 0

        if(request['type'] == "stop"):
            if(request['platform name'] == "hackathon"):
                hackathon_response = PlatformManager.hackathon.stop_platform()
                chat_response = PlatformManager.hackathon.chat.stop_platform()
                wiki_response = PlatformManager.hackathon.wiki.stop_platform()
                
                if(rcr_response == 200 and chat_response == 200 and wiki_response == 200):
                    response = 200
                else:
                    response = 0
                
            if(request['platform name'] == "rcr"):
                rcr_response = PlatformManager.rcr.stop_platform()
                chat_response = PlatformManager.rcr.chat.stop_platform()
                wiki_response = PlatformManager.rcr.wiki.stop_platform()

                if(rcr_response == 200 and chat_response == 200 and wiki_response == 200):
                    response = 200
                else:
                    response = 0
        
        if(request['type'] == "show" and request['subplatform'] == "chat"):
            if(request['platform name'] == "hackathon"):
                response = PlatformManager.cit_IP + str(PlatformManager.hackathon.chat.show_hackathon_chat())
            if(request['platform name'] == "rcr"):
                response = PlatformManager.cit_IP + str(PlatformManager.rcr.chat.show_rcr_chat())

        if(request['type'] == "show" and request['subplatform'] == "wiki"):
            if(request['platform name'] == "hackathon"):
                response = PlatformManager.cit_IP + str(PlatformManager.hackathon.wiki.show_hackathon_wiki())
            if(request['platform name'] == "rcr"):
                response = PlatformManager.cit_IP + str(PlatformManager.rcr.wiki.show_rcr_wiki())

        return PlatformManager.format_response(request['requester'], response)
 
#print(PlatformManager.forward_request("generic.json"))