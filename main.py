"""Allison Patterson and Jacob Kingery"""

import random

from room import *
from verbs import *
from player import *
from npc import *
from radar import *
from troll import *
from professor import *
from trollhunter import *
from homework import *
from computer import *


REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}


# add an exit in 'fr' toward 'to' in direction 'dir'
def connect (fr,dir,to):
    fr.exits()[dir] = to

# add an exit in 'fr' toward 'to' in direction 'dir'
# and an exit the other way, in 'to' toward 'fr' in the reverse direction
def biconnect (fr,dir,to):
    connect(fr,dir,to)
    connect(to,REVERSE[dir],fr)



def create_world ():
    mh353 = Room('Riccardo Office', 'It\'s a bit cramped in here.')
    mh3rd = Room('Milas Hall Third Floor', 'desc')
    mh2nd = Room('Milas Hall Second Floor', 'desc')
    mh1st = Room('Milas Hall First Floor', 'desc')
    oval = Room('Oval', 'The Oval, smack in the center of Olin College.')
    ac1st = Room('Academic Center First Floor', 'desc')
    ac113 = Room('Academic Center 113', 'desc')
    cc1st = Room('Campus Center First Floor', 'desc')
    westh = Room('West Hall', 'The first (and western most) of Olin\'s two dorms.')
    easth = Room('East Hall', 'The second (and eastern most) of Olin\'s two dorms.')
    babson = Room('Babson College', 'Land of the Beavers.')
    dhall = Room('Dining Hall', 'desc')

    biconnect(mh353, 'east',  mh3rd)
    biconnect(mh3rd, 'down',  mh2nd)
    biconnect(mh2nd, 'down',  mh1st)
    biconnect(mh1st, 'north',  oval)
    biconnect(oval, 'east',  cc1st)
    biconnect(cc1st, 'east',  westh)
    biconnect(westh, 'east',  easth)
    biconnect(oval, 'north',  babson)
    biconnect(oval, 'west',  ac1st)
    biconnect(ac1st, 'north',  ac113)

    biconnect(cc1st, 'east', dhall)

    # The player is the first 'thing' that has to be created

    Player('Blubbering-Fool', oval, 'player desc')

    Radar('handy radar', mh353, 'radar desc') 
    # Radar('handy radar', oval, 'radar desc') 
    Thing('blackboard', ac113, 'blackboard desc')
    Thing('lovely-trees', oval, 'trees desc')
    MobileThing('cs-book', oval, 'cs book desc')
    MobileThing('math-book', oval, 'math book desc')

    MobileThing('food', dhall, 'food desc')

    # Computer('hal-9000', ac113, 'hal-9000 desc')
    Computer('johnny-5', easth, 'johnny-5 desc')
    Computer('hal-9000', oval, 'hal-9000 desc')
    Homework('hw-7', oval, 'work work work')
    Homework('hw-8', oval, 'work work work')

    Professor('Riccardo', oval, 'Riccardo desc', random.randint(1,5),2)
    # Professor('Riccardo', mh353, 'Riccardo desc', random.randint(1,5),2)
    
    homeworks = ['hw-1', 
                 'hw-2',
                 'hw-3',
                 'hw-4',
                 'hw-5',
                 'hw-6']
    
    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms), 'hw-x desc')

    students = ['Frankie Freshman',
                'Joe Junior',
                'Sophie Sophomore',
                'Cedric Senior']

    for student in students:
        NPC(student,
            random.choice(Room.rooms), 
            'student desc',
            random.randint(1,5),
            random.randint(1,5))

    trolls = ['Polyphemus',
              'Gollum']

    for troll in trolls:
      Troll(troll,
            random.choice(Room.rooms),
            'troll desc',
            random.randint(1,3),
            random.randint(1,3))


    Trollhunter('Hunter', oval, 'trollhunter desc')

VERBS = {
    'quit' : Quit(),
    'look' : Look(),
    'wait' : Wait(),
    'take' : Take(),
    'drop' : Drop(),
    'give' : Give(),
    'god'  : God(),
    'use'  : Use(),
    'north' : Direction('north'),
    'south' : Direction('south'),
    'east' : Direction('east'),
    'west' : Direction('west'),
    'up'   : Direction('up'),
    'down' : Direction('down'),
    'kill' : Kill()
}
  

def print_tick_action (t):
    Player.me.location().report('The clock ticks '+str(t))


def read_player_input ():
    while True:
        response = raw_input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()


SAME_ROUND = 1
NEXT_ROUND = 2  
  
def main ():
    
    print 'Olinland, version 1.4 (Fall 2014)\n'


    # Create the world
    create_world()

    # Register time printer with clock
    Player.clock.register(print_tick_action, 0)
    
    Player.me.look_around()

    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Player.clock.tick()
                Player.me.look_around()
        else:
            print 'What??'
            

if __name__ == '__main__':
    main()
