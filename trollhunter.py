import random
from npc import *

class Trollhunter (NPC):

    def __init__ (self,name,loc,desc):
        Person.__init__(self,name,loc,desc)
        
        # Register proactive behaviors
        Player.clock.register(self.hunt, 1)

    def hunt (self, time):
        killed = False
        for person in self.people_around():
            if person.is_troll() and not killed:
                self.say('Troll! TROLL! Aaargggh! I go berserk!')
                self.say('I slap ' + person.name() + ' with a dainty white glove.')
                person.suffer(5)
                killed = True
                break
        if not killed:
            self.say('I sniff around but smell no trolls. Bummer.')
            self.move_somewhere()

    def die (self):
        self.say('AHHH! I have been slain! Avenge me...')
        Person.die(self)