import pyglet

import sys
sys.path.append("..")

import objects

X_VEL = 75
Y_VEL = 600

class Enemy(objects.LivingObject):
    def __init__(self, *args, **kwargs):
        # Initialize the LivingObject class
        super().__init__(*args, **kwargs)

        # Set walking velocity to the left
        self.velocity_x = -X_VEL
        
        # Create the player move variables   
        self.walking = False
        self.jumping = False
        self.dashing = False
        self.jumps = 0
        self.jumpable = 0

        self.walk_image = 0
        self.jump_image = 0
        self.dash_image = 0
    def update(self, dt):
        # Update the LivingObject class
        super().update(dt)

    def collide(self, other, right=False, left=False, above=False, below=False):
        super().collide(other, right=right, left=left, above=above, below=below)

        if isinstance(other, objects.Barrier):
            if left:
                print(x)
                self.velocity_x = -X_VEL*16
            if right:
                print(y)
                self.velocity_x = X_VEL
