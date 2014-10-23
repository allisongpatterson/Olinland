Olinland
========

Text adventure game for Game Programming course

Jacob Kingery and Allison Patterson

We added a more complete map; food that restores your health, makes cats your friend, and puts pigs to sleep; cats that follow you if you feed them; pigs that run around and trip people; wo$

Added classes are Food, Cat, Pig, and Wocket. Room class was also modified.

How to see:

* Food restoring health - obtain food (check the dining hall), get hurt, use food
* Befriending Cat with Food - obtain food, go to EH1W, give food to Felix
* Cat being your friend - befriend cat, walk around (cat should follow), get hurt (cat should go crazy and attack all trolls nearby), have cat get hurt (custom message should appear)
* Pigs doing things - observe pigs moving around, observe pigs tripping people
* Putting Pigs to sleep with Food - obtain food, find pig, give food to pig
* Putting Wocket in pocket - find wocket, put in pocket
* Dining hall schedule - attempt to go to dining hall (if you cannot enter, wait a few ticks and try again), wait in dining hall until it closes (you should get kicked out)


Game output:

```
The clock ticks 2    
Bill-the-Babbie-Beater says -- Hi Blubbering-Fool, Buttface, Pig#1, Riccardo
Riccardo starts lecturing about Godel
Buttface says -- I try to take lovely-trees but can't
Pig#1 tries to go to Dining-Hall, but isn't able to get in right now
```

This shows a pig moving and the dining hall being closed.
