from mobile import *


class Food (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)

    def use (self,actor):
        actor.say('I chow down on ' + self.name())
        if actor.health() == actor.max_health():
            actor.say('The ' + self.name() + ' has no effect')
        else:
            actor.reset_health()
            actor.say('The ' + self.name() + ' restores my health to ' + actor.health() + '!')

    def is_food (self):
        return True
        