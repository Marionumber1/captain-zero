import enemies.objects
import enemies.sprites

class InfinityMook(enemies.objects.Enemy):
    def __init__(self, x, y, batch, group):
        # Initialize the PlayerObject class
        super().__init__(img=enemies.sprites.infinimook['walk'][0], x=x, y=y, batch=batch, group=group)

        # Images
        self.images = enemies.sprites.infinimook
    def on_load(self):
        pass
    def on_unload(self):
        pass
