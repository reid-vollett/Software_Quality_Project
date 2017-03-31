# Software Quality Project 

Software Quality Project (Refactoring/Unit Tests for Technostalgic's Asteroid Game)

This project was created for SOFE 3980U to improve upon existing legacy software via refactoring and unit tests. 


### Asteroid Game
Credit for source code provided from Technostalgic under GNU General Public License v3.0

Github: https://github.com/Technostalgic/Asteroids-Too 

Website: https://soundlessdev.itch.io\asteroids-too

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
* asteroid:	 breaks into smaller peices upon destruction
* alien:		 flies around and shoots at you
* basher:		 does not spawn til late - fairly tough, will charge at you and self destruct on collision
* mothercow: does not spawn at beginning - extremely tough, fires projectiles in all directions and spawns aliens

### Powerups
* spread gun: 		  (S)weapon - 5 low damage projectiles fired at a fairly fast rate
* rapid fire: 		  (R)weapon - bullets extremely rapidly with slightly less accuracy
* ion cannon: 		  (I)weapon - an extremely powerful fast traveling continuous beam but is used up quickly
* missile launcher: (M)weapon - powerful heat-seeking missiles that lock on to a nearby enemy at a slightly slower pace
* quad shooter: 		(Q)fires your current weapon to your left, right and directly behind you
* overshield: 		  (O)protects you from any damage that would normally kill you - single use
* deflector shield: (D)projects a matrix 6 of shields that surround you, each deflecting a single projectile 

### Controls
* Menu Navigation / Fly: Arrow Keys
* Shoot Weapon: C
* Exit: Esc

### Working Document
https://docs.google.com/document/d/1kc9j95gGPbQybKr8xLRmZ_g6yBFudPAu6x7vnd741j0/edit?usp=sharing
