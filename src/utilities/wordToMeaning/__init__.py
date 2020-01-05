'''
this module should replace each word with its frame.
if the word is not root its frame is calculated by 
inheritance 
'''
from os import listdir
from os.path import isdir, join
import sys, os, inspect, pkgutil
from pathlib import Path
from importlib import import_module
from modefier import applyModefier 

# prepare current path 
currentPath=Path(__file__).parent 
# add utilities path to sys path and import db
utilitiesPath=join(str(currentPath),"..")
sys.path.append(utilitiesPath)
from db import db

class wordToMeaning:
    def __init__(self):
        self.applyModefier=applyModefier
        return
    
    # gets frame of a word. In case of non-root words it get it recursively  
    def getframe(self, word, modefier=None):
        frame=db.getframe(word)
        if self.rootOrNot(frame):
            return self.applyModefier(frame,modefier)
        else:
            word = db.getframe(word["orig"]) # get the origin of the word
            return self.getframe(word,applyModefier(frame,modefier))

        # return #dict (frame) of the word. statement is 
        # the calculated list by the preprocessor of the phrase
   
    # this is the main function for word to meaning    
    def excute(self,statement):
        for i in range(len(statement)):
            statement[i]=self.getframe(statement[i])
        return statement#list of dicts 

    def rootOrNot(self,frame):
        if frame.root == 1:
            return 1 #bool 1 = root, 0 = non-root
        return 0
        
    
    
    
        

    