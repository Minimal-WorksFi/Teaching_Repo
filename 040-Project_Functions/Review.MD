# Review
## Overview
Congrats, all the functional requirements were met. You have done a good job with those, you even touched most of the bonus requirements at least to a certain level. You've improved a lot, and learnt a lot. Keep going, you will do great in uni :3.
## Basic Requirements
Weee, you met them all.
### 1. Matrix Map
A simple matrix map. The enemies traverse it randomly and the player is placed ontop of it. I can't glitch myself outside (so I'll pressume it all works fine), and it's moddable if I so desire.

Full marks, good job.

Tip: You could have the matrix_printer in the same file as the grid map. You can import multiple things from one file.
### 2. Turn based system
The user moves on turns, same with the enemy. No move goes unchecked by the enemy. Neat.

Tip: There would've been a way to make the dragon walk thowards the player, it would use basic trigonometry. Think Jane think, how could you make it work with the code knowledge you have?
### 3. Statistics
You keep a track of user score via measuring the amount of turns it takes to win. Cool.
### 4. Enemy types
The dragon is cool, it's fighting blindly and making it quite hellish. The traps are well made and you check to make sure the trap doesn't spawn underneath the player. A thing of note is you check the spawn of the trap *after* the player moves so it doesn't feel unfair. Cool.

Still mad about the trap being so hard to see oml

## Bonus Requirements
A really strong attempt. This has probably helped you learn a lot.

### 1. Leaderboard and Username
Your leaderboard system works and is functional, and you take the username. I will give credit where it's due, you checked if the players' name starts with x, which is an insanely good catch. Honestly I might've missed it myself.

The leaderboard itself is..............
Lacking. You keep track of the stats, but you need to learn to make it more easy to digest. The UI is sometimes pretty egregious even for a programmer, and it would make life way worse for you to work on. I will cover this later.
### 2. No Extra Levels
C'est la vie. It's fine, you used files for other things, which would've been the purpose of using multiple levels anyways. Sadly I don't think your game is too easy to extend with more maps, units, and things.
### 3. UI Design
The UI is pretty... ehhh, sometimes not from your fault.
It is hard to tell what turn I am on and what notifications I got for the specific turn. It's part of the issue of using a console. Maybe you could've added a turn counter?

For the leaderboard, the score is just printed there as a list. What the hell does that list mean? I can tell, could a *median voter* tell? Probably not. You have to start building stuff for the lowest common denominator, cause you will work, and you will be the lowest common denominator xD.

Also, the average person would have *0* clue about how to beat the game, ***WHY IS THE SWORD NOT MARKED ON THE GROUND AFTER THE DRAGON MOVES ITS ASS OFF OF IT???*** Only reason I finished it is cause I looked into the code first.
### 4. Gameplay
The gameplay is... kinda there. The dragon is dumb as bricks, the traps are honestly really interesting, if frustrating at first. The sword at least is an objective, so you added an actual end state. You did a surprisingly functional game, I honestly expected it to be a lot worse. Might even be fun to just tap away at it as a phone game.

People play flappy bird so why not this?

## Code Review
The code looks well. It's separated into files, honestly I might say a few too many files lol. But it's a fine job. You applied a lot of the lessons I gave you, so you should feel proud. The code is sadly not too expandable. If you wanted to add more enemies you'd have to write it in manually and add a loop for it specifically. You probably could've made a list of enemies and controlled them like that based on type.

Always look for ways to make your code more easy to extend. Always. OOP will help you with it, but it's not just an OOP paradigm.

## What's next
I will add some extra material, and then you will jump into OOP. I recommend you write a review of your own, think of what you did wrong, what you did right. If you ever had to expand your work, how would it go?
These are important lessons, and I hope my guidance has been at the very least adequate.

## Links
By the way you know how to view MD files right?

[User Stories & Requirements (Link not added yet)]()