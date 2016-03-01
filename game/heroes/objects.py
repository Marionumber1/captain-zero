import pyglet

import sys
sys.path.append("..")

import objects

class PlayerObject(objects.LivingObject):
    def __init__(self, *args, **kwargs):
        # Initialize the LivingObject class
        super().__init__(*args, **kwargs)

        # Create the key dictionary
        self.keys = {'left':False, 'right':False, 'up':False, 'down':False, 'jump':False, 'special':False}
        
        # Create the player move variables   
        self.walking = False
        self.jumping = False
        self.dashing = False
        self.ducking = False

        self.walk_image = 0
        self.jump_image = 0
        self.dash_image = 0
        self.swim_image = 0
    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.LEFT:
            self.keys['left'] = True
        if symbol == pyglet.window.key.RIGHT:
            self.keys['right'] = True
        if symbol == pyglet.window.key.UP:
            self.keys['up'] = True
        if symbol == pyglet.window.key.DOWN:
            self.keys['down'] = True
        if symbol == pyglet.window.key.SPACE:
            self.keys['jump'] = True
    def on_key_release(self, symbol, modifiers):
        if symbol == pyglet.window.key.LEFT:
            self.keys['left'] = False
        if symbol == pyglet.window.key.RIGHT:
            self.keys['right'] = False
        if symbol == pyglet.window.key.UP:
            self.keys['up'] = False
        if symbol == pyglet.window.key.DOWN:
            self.keys['down'] = False
        if symbol == pyglet.window.key.SPACE:
            self.keys['jump'] = False
    def update(self, dt):
        # Update the LivingObject class
        super().update(dt)

        # Left key pressed
        if self.keys['left'] == True:
            self.walking = True
            self.velocity_x = -50
        # Right key pressed
        elif self.keys['right'] == True:
            self.walking = True
            self.velocity_x = 50
