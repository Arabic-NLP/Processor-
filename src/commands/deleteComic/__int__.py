from os import listdir
from os.path import isdir, join
import sys, os, inspect, pkgutil
from pathlib import Path
from importlib import import_module

# prepare current path and utilities path
currentPath=Path(__file__).parent 
CommandPath=currentPath
utilitiesPath=join(currentPath,"..","..","utilities")

# add utilities as sys path so that python could find the modules inside it 
sys.path.append(utilitiesPath)

# import base class commandBase, but call it "base"
basePath=join(currentPath,"..")
sys.path.append(basePath)
#print(sys.path)
from commandBase import commandBase as base


#get module names from /utilities
modulesNames = [f for f in listdir(utilitiesPath) if (isdir(join(utilitiesPath, f)) and (f != '__pycache__'))]
print("Imported Modules are: ",modulesNames)


class deleteComic():
    def execut(self):
        
        return 
    def allInOne():
        return
    def clean():
        return
    def prepare():
        return
