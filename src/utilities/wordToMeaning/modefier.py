'''
this module calculates the new frame. newFrame= frame * modefier
'''
class modefier:
    def __init__(self,frame,modefier):
        self.frame=frame
        self.modefier=modefier

    # modefy tags  
    def modTag(self):
        lestOfTags=self.frame["tags"].keys()
        for i in range(len(lestOfTags)):
            self.frame["tags"][lestOfTags[i]]=self.frame["tags"][lestOfTags[i]]*self.modefier["tags"][lestOfTags[i]]
        
    # mdefy feal
    def modFeal(self):
        lestOffealings=self.frame["fealling"].keys()
        for i in range(len(lestOffealings)):
            self.frame["fealling"][lestOffealings[i]]=self.frame["fealling"][lestOffealings[i]]*self.modefier["fealling"][lestOffealings[i]]
    
    # modefy effect on after
    def modAfter(self):
        lestOfkeys=self.frame["effectOnAfter"].keys()
        for i in range(len(lestOfkeys)):
            self.frame["effectOnAfter"][lestOfkeys[i]]=self.frame["effectOnAfter"][lestOfkeys[i]]*self.modefier["effectOnAfter"][lestOfkeys[i]]
    
    # modefy effect on before
    def modBefore(self):
        lestOfkeys=self.frame["effectOnBefore"].keys()
        for i in range(len(lestOfkeys)):
            self.frame["effectOnBefore"][lestOfkeys[i]]=self.frame["effectOnBefore"][lestOfkeys[i]]*self.modefier["effectOnBefore"][lestOfkeys[i]]
        
    
# applys all modefiers
def applyModefier(frame,modefier):
    x = modefier(frame,modefier)
    x.modTag()
    x.modFeal()
    x.modAfter()
    x.modBefore()
    return x.frame