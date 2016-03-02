import pyglet

import sys
sys.path.append("..")

import objects

X_VEL = 150
Y_VEL = 600

class Player(objects.LivingObject):
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
        self.jumps = 0
        self.jumpable = 0

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
            self.velocity_x = -X_VEL
        # Right key pressed
        elif self.keys['right'] == True:
            self.walking = True
            self.velocity_x = X_VEL
        # No horizontal movement key pressed
        else:
            self.walking = False
            self.velocity_x = 0

        if self.keys['up'] == True:
            if self.jumps < 2 and self.jumpable:
                self.jumps += 1
                self.jumping = True
                self.jumpable = False
                self.velocity_y = Y_VEL
        else:
            self.jumpable = True

        # Move camera
        pyglet.gl.glViewport(-int(self.x), 0, 960, 540)
        print("YO")

    def collide(self, other, right=False, left=False, above=False, below=False):
        super().collide(other, right=right, left=left, above=above, below=below)

        if above:
            self.jumps = 0
