import pyglet

class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        # Initialize the sprite class
        super().__init__(*args, **kwargs)

        # Images
        self.images = []

        # Create the physics variables
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.acc_x = 0.0
        self.acc_y = 0.0

        # Points
        self.points = 0

        # Deletion status
        self.delete = False
    def update(self, dt):
        # Velocity
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Acceleration
        self.velocity_x += self.acc_x * dt
        self.velocity_y += self.acc_y * dt

        # Change the bounding box

        # Handle object events

        # Change the bounding box

class LivingObject(PhysicalObject):
    def __init__(self, *args, **kwargs):
        # Initialize the PhysicalObject class
        super().__init__(*args, **kwargs)
        
        # HP and stats
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.jump_height = 0
        self.speed = 0
        
        # Create the object direction variable
        self.direction = 0 # -1 - Left, 1 - Right
    def update(self, dt):
        # Update the PhysicalObject class
        super().update(dt)

        # Check if the HP is depleted, and if so, call self.die()
        if self.hp <= 0:
            #self.die()
            pass
