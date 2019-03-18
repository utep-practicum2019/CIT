import os, sys, random  

'''
    author: Hector Cervantes
    Date of last update: March 16 
    Descritption:
        This class implements a binary search tree to keep track of specific platform instances.
        This tree will be able to retrive specific instances by specifying a platform identifier for each platform,
        in order to facilitate retrieval of platforms.

'''

class platformNode():

    def __init__(self, platform):
        self.platformID = platform.getPlatformID()
        self.platform = platform 
        self.rightNode = None
        self.leftNode = None
        self.isLeaf = True
    
    def getPlatformID(self): 
        return self.platformID
    
    def getPlatform(self):
        return self.platform
    
    def getRightNode(self):
        return self.rightNode
    
    def getLeftNode(self):
        return self.leftNode
    
    def getIsLeaf(self):
        return self.getIsLeaf
    
    def setPlatformID(self, platformID):
         self.platformID = platformID
    
    def setPlatform(self, platform):
        self.platform = platform
    
    def setRightNode(self, rightNode):
        self.rightNode = rightNode
    
    def setLeftNode(self, leftNode):
        self.leftNode = leftNode
    
    def setIsLeaf(self, isLeaf):
        self.isLeaf = isLeaf



class PlatformTree():
   
    def addNode(self, node, platform):
        if(node is None):
            node = platformNode(platform)
            return node 
        elif(node.getPlatformID() <= platform.getPlatformID()):
            right_node = self.addNode(node.rightNode, platform)
            node.setRightNode(right_node)
            node.setIsLeaf(False)
            return node 
        else: 
            left_node = self.addNode(node.leftNode, platform)
            node.setLeftNode(left_node)
            node.setIsLeaf(False)
            return node 
        
            
    # need to finish 
    def deleteNode(self, node, platformID):
        if(node.getPlatformID() == platformID):
            if(node.getRightNode() is None and node.getLeftNode() is None):
                node = None
                return node
            elif(node.getRightNode() != None and node.getLeftNode() is None):
                node = node.getRightNode()
                return node
            elif(node.getRightNode() is None and node.getLeftNode() != None):
                node = node.getLeftNode()
                return node
            else:
                node = self.restructure(node.getRightNode())
                return node 
    
    def restructure(self, node):
        temp = node
        while(temp.getLeftNode() != None):
            temp = temp.getLeftNode()
        node.setPlatformID(temp.left)
             

        
        
         

            

    def getNode(self, node, platformID):
        if(node is None):
            return 0
        if(platformID == node.getPlatformID()):
            return node.platform
        elif(platformID >= node.getPlatformID()):
            return self.getNode(node.rightNode, platformID)
        else:
            return self.getNode(node.leftNode, platformID) 
    
    def id_Availability(self, node, platformID):
        if(node is None):
            return True
        if(platformID == node.getPlatformID()):
            return False
        elif(platformID >= node.getPlatformID()):
            return self.getNode(node.rightNode, platformID)
        else:
            return self.getNode(node.leftNode, platformID) 
    

class PlatformTreeManager():
    def __init__(self):
        self.root = None
        self.PlatformTree = PlatformTree()
        self.ids = {}
    
    def getRoot(self):
        return self.root
    
    def printTree(self, node):
        if(node is None):
            return 
        self.printTree(node.leftNode)
        print("printing id: " + str(node.getPlatformID()))
        self.printTree(node.rightNode)
    
    def add(self, platform):
        main_id = random.randint(1, 100000)
        subplatform_ids = {} 
        platform.setPlatformID(main_id)
        for x in platform.get_sub_platforms():
            id = random.randint(1, 100000)
            platform.subplatforms[x].setPlatformID(id)
            subplatform_ids[x] = id
        self.root = self.PlatformTree.addNode(self.root, platform)
        return (main_id,subplatform_ids)

    def getPlatform(self, platformID):
        return self.PlatformTree.getNode(self.root, platformID)


    # these generate methods need work to be able to generate globally unique id's for each instance 
    def generate_main_ID(self):
        id = 0
        counter = 0
        while(True):
            id = random.randint(1, 100000)
            if(self.PlatformTree.id_Availability(self.root, id)):
                return id 
            if(counter == 100000000):
                break 
            counter += 1
        return id


    
    def generate_sub_ID(self, Main_Platform):
        id = 0
        subplatfrms = Main_Platform.get_sub_platforms()
        while(True):
            id = random.randint(1, 100000)
            for x in subplatfrms:
                if(subplatfrms[x].getPlatformID == id):
                    break 
            if(id != 0):
                return id 

        
            
        
        
        
        
