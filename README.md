# Software Quality Project 

Software Quality Project (Refactoring/Unit Tests for Technostalgic's Asteroid Game)

This project was created for SOFE 3980U to improve upon existing legacy software via refactoring and unit tests. 


### Asteroid Game
Credit for source code provided from Technostalgic under GNU General Public License v3.0

Github: https://github.com/Technostalgic/Asteroids-Too 

Website: https://technostalgic.itch.io/asteroids-too

Source Code Cloned: March 29th, 2017


## Execution:
### Game Execution
1. Install latest version of Anaconda (https://www.continuum.io/downloads)
2. \> pip install pygame
3. \> python spacegame.py
### Unit Test Suite Execution
1. Install lastest version of anaconda (https://www.continuum.io/downloads)
2. \> python TestMain.py --unittest

## Instructions
### Enemies
* Asteroid:	 Breaks into smaller peices upon destruction
* Alien:		 Flies around and shoots at you
* Basher:		 Does not spawn until late - fairly tough, will charge at you and self destruct on collision
* Mothercow: Does not spawn at beginning - extremely tough, fires projectiles in all directions and spawns aliens

### Powerups
* Spread gun: 		  (S)Weapon - 5 low damage projectiles fired at a fairly fast rate
* Rapid fire: 		  (R)Weapon - Bullets extremely rapidly with slightly less accuracy
* Ion cannon: 		  (I)Weapon - An extremely powerful fast traveling continuous beam but is used up quickly
* Missile launcher: (M)Weapon - Powerful heat-seeking missiles that lock on to a nearby enemy at a slightly slower pace
* Quad shooter: 		(Q)Fires your current weapon to your left, right and directly behind you
* Overshield: 		  (O)Protects you from any damage that would normally kill you - single use
* Deflector shield: (D)Projects a matrix 6 of shields that surround you, each deflecting a single projectile 

### Controls
* Menu Navigation / Fly: Arrow Keys
* Shoot Weapon: C
* Exit: Esc

### Working Document
https://docs.google.com/document/d/1kc9j95gGPbQybKr8xLRmZ_g6yBFudPAu6x7vnd741j0/edit?usp=sharing
