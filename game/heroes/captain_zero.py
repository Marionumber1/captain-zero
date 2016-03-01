from game import heroes

class CaptainZero(heroes.objects.Player):
    def __init__(self, x, y, batch, group):
        # Initialize the PlayerObject class
        super().__init__(img=heroes.sprites.captain_zero['walk'][0], x=x, y=y, batch=batch, group=group)

        # Images
        self.images = heroes.sprites.captain_zero
    def on_load(self):
        pass
    def on_unload(self):
        pass
