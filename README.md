Olinland
========

Text adventure game for Game Programming course

Jacob Kingery and Allison Patterson

We thought the project was nicely scoped and didn't really have any big problems.

We added a more complete map; food that restores your health, makes cats your friend, and puts pigs to sleep; cats that follow you if you feed them; pigs that run around and trip people (and become bacon when they die); wockets that go in your pockets; and a locking cycle for the dining hall.

Added classes are Food, Cat, Pig, and Wocket. Room class was also modified.

How to see:

* Map - explore
* Food restoring health - obtain food (check the dining hall), get hurt, use food
* Befriending Cat with Food - obtain food, go to EH1W, give food to Felix
* Cat being your friend - befriend cat, walk around (cat should follow), get hurt (cat should go crazy and attack all trolls nearby), have cat get hurt (custom message should appear)
* Pigs doing things - observe pigs moving around, observe pigs tripping people
* Putting Pigs to sleep with Food - obtain food, find pig, give food to pig
* Pig becoming bacon - observe pig dying
* Putting Wocket in pocket - find wocket, put in pocket
* Dining hall schedule - attempt to go to dining hall (if you cannot enter, wait a few ticks and try again), wait in dining hall until it closes (you should get kicked out)


Game output:

```
Pig#1 tries to go to Dining-Hall, but isn't able to get in right now
```
Pig moving and the dining hall being closed

```
Pig#1 enthusiastically trips Riccardo
Riccardo says -- Ouch! 1 hits is more than I want!
Riccardo says -- My health is now 4
```
Pig tripping Riccardo

```
The clock ticks 10
Dining-Hall closed and kicked out Blubbering-Fool
```
Dining hall closing are kicking out the people inside

```
What is thy bidding? use bagel


Blubbering-Fool says -- I chow down on bagel
Blubbering-Fool says -- The bagel restores my health to 5!
```
Food restoring health

```
What is thy bidding? give milkshake Pig#1


Blubbering-Fool says -- I give milkshake to Pig#1
Pig#1 takes the food, squeals happily, and promptly falls asleep.
```
Food putting pig to sleep

```
You see: lovely-trees, Eric, bacon#1
```
What used to be Pig#1

```
What is thy bidding? give tuna Felix


Blubbering-Fool says -- I give tuna to Felix
Felix takes the food and purrs loudly
```
Feeding a cat

```
Felix follows Blubbering-Fool to East-Hall-First-Floor
```
Cat following its friend

```
Buttface takes a bite out of Blubbering-Fool
Blubbering-Fool says -- Ouch! 2 hits is more than I want!
Blubbering-Fool says -- My health is now 2
Felix tries to protect Blubbering-Fool and attackes all trolls nearby.
Buttface says -- Ouch! 1 hits is more than I want!
Buttface says -- My health is now 2
```
Cat defending its friend

```
Felix says -- me-OW! 1 meow meow meow meow meow meow!
Felix says -- meow meow meow meow 4
Felix runs to Blubbering-Fool for comfort.
```
Cat getting hurt when it has a friend

```
What is thy bidding? take wocket

Blubbering-Fool says -- I take wocket from The-Oval

What is thy bidding? use wocket

Blubbering-Fool says -- THERE'S A WOCKET IN MY POCKET!!!
Blubbering-Fool dances a happy little jig
```
Wockets:  they go in pockets
