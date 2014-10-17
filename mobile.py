from thing import *

class MobileThing (Thing):

    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)
        self._original_location = loc

    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self)
        self._location = loc

    def take (self,actor):
        actor.say('I take '+self.name()+' from '+self.location().name())
        if self.location().is_person():
            self.location().say('I lose '+self.name())
            self.location().have_fit()
        self.move(actor)

    def drop (self,actor):
        actor.say('I drop '+self.name()+' in '+actor.location().name())
        self.move(actor.location())

    def give (self,actor,target):
        actor.say('I give '+self.name()+ ' to '+target.name())
        target.accept(self, actor)
        self.move(target)

    def creation_site (self):
        return self._original_location

    def is_mobile_thing (self):
        return True

