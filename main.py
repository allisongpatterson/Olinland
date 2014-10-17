"""Allison Patterson and Jacob Kingery"""

import random

from room import *
from verbs import *
from player import *
from npc import *
from radar import *
from troll import *
from professor import *
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

    # Outside
    Oval = Room('The Oval','The Center Of Both The Campus And The Swirling Vortex')
    GLW = Room('Great Lawn West','Couches Migrate Here In Nice Weather')
    GLE = Room('Great Lawn East','Where People Sunbathe In Bikinis Even When There\'s No Actual Sunlight')

    biconnect(Oval,'west',AC1)
    biconnect(Oval,'south',MH1)
    biconnect(Oval,'north',DH)
    biconnect(Oval,'east',GLW)
    biconnect(GLW,'east',GLE)
    biconnect(GLW,'north',WH1)
    biconnect(GLE,'north',EH1)

    # AC
    AC1 = Room('Academic Center First Floor')
    AC2 = Room('Academic Center Second Floor','Freshie Central')
    AC3 = Room('Academic Center Third Floor')
    AC4 = Room('Academic Center Fourth Floor')

    biconnect(AC1,'up',AC2)
    biconnect(AC2,'up',AC3)
    biconnect(AC3,'up',AC4)

    # MH
    MH1 = Room('Milas Hall First Floor','Part Library, Part Big Awkward Echoey Cavern')
    MH2 = Room('Milas Hall Second Floor')
    MH3 = Room('Milas Hall Third Floor')
    MH4 = Room('Milas Hall Fourth Floor')

    biconnect(MH1,'up',MH2)
    biconnect(MH2,'up',MH3)
    biconnect(MH3,'up',MH4)

    # DH
    DH = Room('Dining Hall')
    Mezz = Room('Dining Hall Mezz','That Place Where All The Meetings Happen')

    biconnect(DH,'up',Mezz)

    # WH
    WH1 = Room('West Hall First Floor','Foose-Ball, Air Hockey, And Nerf Armory')
    WH1W = Room('West Hall First Floor West','That Door Everyone Uses Because It\'s Closer To The DH And We\'re Lazy')
    WH1E = Room('West Hall First Floor East','Humble Abode Of The Tatars And Their Tots')
    WH1N = Room('West Hall First Floor North','The Semi-Recently Refurbished Kitchen Thanks To Greg And His Infamous Tea Kettle Incident')

    WH2 = Room('West Hall Second Floor')
    WH2W = Room('West Hall Second Floor West')
    WH2E = Room('West Hall Second Floor East')
    WH2N = Room('West Hall Second Floor North')

    WH3 = Room('West Hall Third Floor')
    WH3W = Room('West Hall Third Floor West')
    WH3E = Room('West Hall Third Floor East')
    WH3N = Room('West Hall Third Floor North')

    WH4 = Room('West Hall Fourth Floor')
    WH4W = Room('West Hall Fourth Floor','That One Lofted Room That No One Knows Exists')
    WH4E = Room('West Hall Fourth Floor')
    WH4N = Room('West Hall Fourth Floor','Coveted Land O\' Lofts')

    biconnect(WH1,'up',WH2)
    biconnect(WH1,'west',WH1W)
    biconnect(WH1,'east',WH1E)
    biconnect(WH1,'north',WH1N)

    biconnect(WH2,'up',WH3)
    biconnect(WH2,'west',WH2W)
    biconnect(WH2,'east',WH2E)
    biconnect(WH2,'north',WH2N)

    biconnect(WH3,'up',WH4)
    biconnect(WH3,'west',WH3W)
    biconnect(WH3,'east',WH3E)
    biconnect(WH3,'north',WH3N)

    biconnect(WH4,'west',WH4W)
    biconnect(WH4,'east',WH4E)
    biconnect(WH4,'north',WH4N)

    # EH
    EH1 = Room('East Hall First Floor','The Most-Used Team Rooms Because Nobody Likes Stairs')
    EH1W = Room('East Hall First Floor West','Felix\'s Personal Luxury Hotel')
    EH1E = Room('East Hall First Floor East','Scotland')
    EH1N = Room('East Hall First Floor North')

    EH2 = Room('East Hall Second Floor','Free Art Stuff For Students With Wellesley Classes And No Monies')
    EH2W = Room('East Hall Second Floor West')
    EH2E = Room('East Hall Second Floor East')
    EH2N = Room('East Hall Second Floor North','Remenants Of The Fallen Society Of Mann Hall')

    EH3 = Room('East Hall Third Floor')
    EH3W = Room('East Hall Third Floor West')
    EH3E = Room('East Hall Third Floor East')
    EH3N = Room('East Hall Third Floor North')

    EH4 = Room('East Hall Fourth Floor')
    EH4W = Room('East Hall Fourth Floor West')
    EH4E = Room('East Hall Fourth Floor East')
    EH4N = Room('East Hall Fourth Floor North','Home Of Virtually Everyone In Olin Robotic Sailing')

    biconnect(EH1,'up',EH2)
    biconnect(EH1,'west',EH1W)
    biconnect(EH1,'east',EH1E)
    biconnect(EH1,'north',EH1N)

    biconnect(EH2,'up',EH3)
    biconnect(EH2,'west',EH2W)
    biconnect(EH2,'east',EH2E)
    biconnect(EH2,'north',EH2N)

    biconnect(EH3,'up',EH4)
    biconnect(EH3,'west',EH3W)
    biconnect(EH3,'east',EH3E)
    biconnect(EH3,'north',EH3N)

    biconnect(EH4,'west',EH4W)
    biconnect(EH4,'east',EH4E)
    biconnect(EH4,'north',EH4N)

    ########################################################################

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

    Computer('hal-9000', ac113, 'hal-9000 desc')
    Computer('johnny-5', easth, 'johnny-5 desc')


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
    
    Player.me.look_around()

    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Player.me.look_around()
        else:
            print 'What??'
            

if __name__ == '__main__':
    main()
