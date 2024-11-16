import pygame
import sys
from agent import Agent
from environment import Environment

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the environment and display
    WIDTH = 800
    HEIGHT = 600
    environment = Environment(WIDTH, HEIGHT)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Agent Environment Simulation")
    
    # Create the agent in the center of the screen
    agent = Agent(environment, x=WIDTH//2, y=HEIGHT//2)
    
    # Set up font for position display
    font = pygame.font.Font(None, 36)
    
    # Main game loop
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Handle continuous keyboard input
        keys = pygame.key.get_pressed()
        dx = dy = 0
        
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1
            
        # Move agent if there's input
        if dx != 0 or dy != 0:
            agent.move(dx, dy)
        
        # Clear screen
        screen.fill((255, 255, 255))  # White background
        
        # Draw agent
        pygame.draw.rect(screen, (0, 0, 255),  # Blue square
                        (agent.x - agent.size//2,
                         agent.y - agent.size//2,
                         agent.size, agent.size))
        
        # Display position
        position_text = f"Position: ({int(agent.x)}, {int(agent.y)})"
        speed_text = f"Speed: {agent.speed:.1f}"
        
        position_surface = font.render(position_text, True, (0, 0, 0))
        speed_surface = font.render(speed_text, True, (0, 0, 0))
        
        screen.blit(position_surface, (10, 10))
        screen.blit(speed_surface, (10, 50))
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()