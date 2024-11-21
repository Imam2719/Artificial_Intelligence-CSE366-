class Agent:
    def __init__(self, environment, x=0, y=0, speed=5):
    
        self.environment = environment
        self.x = x
        self.y = y
        self.speed = speed
        self.size = 20  # Size of the agent square

    def move(self, dx, dy):
     
        new_x = self.x + (dx * self.speed)
        new_y = self.y + (dy * self.speed)
        
        # Wrap around screen
        new_x = new_x % self.environment.width
        new_y = new_y % self.environment.height
        
        self.x, self.y = new_x, new_y
        
        # Increase speed slightly with each movement
        self.speed += 0.01

    def get_position(self):
        return (self.x, self.y)