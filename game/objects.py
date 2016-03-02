import pyglet

class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, gravity=True, *args, **kwargs):
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

        # Whether gravity applies to this object
        self.gravity = gravity

    def update(self, dt):
        # Velocity
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Acceleration
        self.velocity_x += self.acc_x * dt
        self.velocity_y += self.acc_y * dt

    def check_collision(self, other):
        # Calculate next X/Y of self and other
        self_x = self.x #+ self.velocity_x * (1/120)
        self_y = self.y #+ self.velocity_y * (1/120)
        other_x = other.x #+ other.velocity_x * (1/120)
        other_y = other.y #+ other.velocity_y * (1/120)
        
        # Check collision, and handle it
        if (self_x < other_x+other.width and self_x+self.width > other_x and
                self_y < other_y+other.height and self_y+self.height > other_y):
            self.collide(other, left=self_x+self.width < other_x+other.width and self.velocity_x > 0,
                         right=self_x > other_x and self.velocity_x < 0,
                         above=self_y > other_y and self.velocity_y < 0,
                         below=self_y+self.height < other_y+other.height and self.velocity_y > 0)

    def collide(self, other, right=False, left=False, above=False, below=False):
        # Colliding with barrier
        if isinstance(other, Barrier) and not isinstance(self, Barrier):
            # Above barrier, so stop gravity
            if above:
                self.y = other.y + other.height
                self.velocity_y = max(0, self.velocity_y)
                self.acc_y = 0git st
            # Hitting barrier from bottom, so stop jump
            elif below:
                self.y = other.y - self.height
                self.velocity_y = min(0, self.velocity_y)
            # Hitting from left or right, so stop walk
            elif left or right:
                self.velocity_x = 0

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

class Barrier(PhysicalObject):
    def __init__(self, *args, **kwargs):
        kwargs['gravity'] = False
        # Initialize the PhysicalObject class
        super().__init__(*args, **kwargs)

    def update(self, dt):
        # Update the PhysicalObject class
        super().update(dt)
