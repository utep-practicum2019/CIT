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
         
    def deleteNode(self, node, platformID):
        if(node.getPlatformID() == platformID):
            if(node.getRightNode() is None and node.getLeftNode() is None):
                # print("first case")
                node = None
                return node
            elif(node.getRightNode() != None and node.getLeftNode() is None):
                # print("second case")
                temp = node.getRightNode() 
                node.setPlatform(temp.getPlatform())
                node.setPlatformID(temp.getPlatformID())
                node.setRightNode(temp.getRightNode())
                node.setLeftNode(temp.getLeftNode())
                return node
            elif(node.getRightNode() is None and node.getLeftNode() != None):
                # print("third case")
                temp = node.getLeftNode() 
                node.setPlatform(temp.getPlatform())
                node.setPlatformID(temp.getPlatformID())
                node.setRightNode(temp.getRightNode())
                node.setLeftNode(temp.getLeftNode())
                return node 
            else:
                # print("fourth case")
                node = self.restructureTree(node)
                return node 
        if(platformID > node.getPlatformID()):
            node.setRightNode(self.deleteNode(node.getRightNode(), platformID))
        else:
            node.setLeftNode(self.deleteNode(node.getLeftNode(), platformID))
        return node
    
    def restructureTree(self, node):
        temp = node.getLeftNode()
        while(temp.getRightNode() != None):
            temp = temp.getRightNode()
        node.setPlatformID(temp.getPlatformID())
        node.setPlatform(temp.getPlatform())
        node.setLeftNode(self.removeNode(node.getLeftNode()))
        return node 
    
    def removeNode(self, node):
        if(node.getLeftNode() is None and node.getRightNode() is None):
            return None
        elif(node.getLeftNode() != None and node.getRightNode() is None):
            return node.getLeftNode()
        else:
            node.setRightNode(self.removeNode(node.getRightNode()))
        return node 
        
    def getNode(self, node, platformID):
        if(node is None):
            return None
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
            return self.id_Availability(node.rightNode, platformID)
        else:
            return self.id_Availability(node.leftNode, platformID) 
    

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
        main_id = self.generate_main_ID()
        subplatform_ids = {} 
        platform.setPlatformID(main_id)
        for x in platform.get_sub_platforms():
            id = self.generate_sub_ID(platform)
            platform.subplatforms[x].setPlatformID(id)
            subplatform_ids[x] = id
        self.root = self.PlatformTree.addNode(self.root, platform)
        return (main_id, subplatform_ids)
    
    def reAdd(self, platform):
        self.root = self.PlatformTree.addNode(self.root, platform)
        return 
    
    def remove(self, platformID):
        self.root = self.PlatformTree.deleteNode(self.root, platformID)
        return self.root 

    def getPlatform(self, platformID):
        return self.PlatformTree.getNode(self.root, platformID)

    def generate_main_ID(self):
        id = 0
        while(id == 0):
            randID = random.randint(1, 100000)
            if(self.PlatformTree.id_Availability(self.root, randID)):
                id = randID
        return id 
        
    def generate_sub_ID(self, Main_Platform):
        id = 0
        subplatforms = Main_Platform.get_sub_platforms()
        while(id == 0):
            id = random.randint(1, 100000)
            for x in subplatforms:
                if(subplatforms[x].getPlatformID() == id):
                    id = 0
                    break  
        return id 

        
            
        
        
        
        
