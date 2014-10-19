import random
from npc import *

class BadNINJA (NPC):
    def __init__ (self,name,loc,desc,restlessness,miserly):
        NPC.__init__(self,name,loc,desc,restlessness,miserly)
        
        # Register proactive behaviors
        Player.clock.register(self.take_hw, 1)

    def take_hw (self, time):
        if not self.is_in_limbo():
            burned = False
            all_stuff = self.stuff_around() + self.peek_around()
            for obj in all_stuff:
                if obj.is_homework() and obj.is_done():
                    self.say('Aha! What\'s this! A completed homework? Let me look at it.')
                    obj.take(self)
                    self.say('No, no, no! It\'s all wrong, WRONG!')
                    self.say('Burn, baby, burn!')
                    obj.destroy()
                    burned = True
                    break

