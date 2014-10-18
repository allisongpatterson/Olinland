from player import *
from npc import *
import random
import sys

class Professor (NPC):

    def __init__ (self,name,loc,desc,restlessness,professorial):
        NPC.__init__(self,name,loc,desc,restlessness,100)
        self._professorial = professorial

        # Register proactive behaviors
        Player.clock.register(self.lecture, 2)

    _topics = ['Turing machines',
               'the lambda calculus',
               'Godel']

    def lecture (self,time):
        if not self.is_in_limbo():
            if random.randrange(self._professorial) == 0:
                if self.people_around():
                    self.location().report(self.name()+' starts lecturing about '+random.choice(self._topics))
                else:
                    self.location().report(self.name()+' mutters to himself about '+random.choice(self._topics))

    def grade_hw (self, hw, student):
        if hw.is_done():
            self.say('Good, good... Excellent...')
            self.say('Mmm, could have used some more comments.')
            self.say('All in all, well done. Top work.')
            if student is Player.me:
              self.say('Looks like that\'s enough to pass the class. Congrats.')
              print 'You win, I guess.'
              sys.exit(0)
        else:
            self.say('Ah, a homework to be graded! Let\'s see here...')
            self.say('Wait, this homework\'s not even been started!')

    def accept (self,obj,source):
        if 'hw-' in obj.name():
            self.grade_hw(obj, source)
            obj.give(self, source)
        else:
            self.say('Thanks, ' + source.name())