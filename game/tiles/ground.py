from game import objects

import pyglet

image = pyglet.image.load('../sprites/tiles/ground.png')

class Ground(objects.Barrier):
    def __init__(self, x, y, batch, group):
        # Initialize the Player class
        super().__init__(img=image, x=x, y=y, batch=batch, group=group)

        self.images = [image]

    def on_load(self):
        pass
    def on_unload(self):
        pass
