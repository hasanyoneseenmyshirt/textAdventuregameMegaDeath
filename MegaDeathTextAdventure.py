from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print "this scene is not yet configured. Subclass it and implement enter()."
		exit(1)
		


		
		
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map= scene_map
		
	def play(self):
		current_scene=self.scene_map.opening_scene()
		
		while True:
			print "\n--------"
			next_scene_name=current_scene.enter()
			current_scene=self.scene_map.next_scene(next_scene_name)
			

			
class Death(Scene):
	quip=[
		"You suck at this",
		"Better luck next time",
		"You could do better...maybe",
		]
		
	def enter(self):
		print Death.quip[randint(0,len(self.quip)-1)]
		exit(1)

class RoomOne(Scene):
	def enter(self):
		print "You are in room one"
		print "There is a door."
		print"Do you want to open the door and go to room two"
		answer=raw_input("Yes or No:  ")
		if answer == 'Yes':
			return 'roomtwo'
				
		else: 
			print "Guess we can just stay here and starve to death"
			return 'death'
		
class RoomTwo(Scene):
	def enter(self):
		print "Room two has no floor."
		print "You plummet to the floor and die"
		return 'death'
	
class Map(object):
	scenes={
	'roomone':RoomOne(),
	'roomtwo':RoomTwo(),
	'death':Death()
	}
	
	def __init__(self, start_scene):
		self.start_scene=start_scene
	
	def next_scene(self,scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
a_map = Map('roomone')
a_game=Engine(a_map)
a_game.play()

	
			


