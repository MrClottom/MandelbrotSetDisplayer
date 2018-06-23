import pygame
from pygame.locals import *
from mandelbrot import calc_value, pixel_to_real

"""
while the script is running press the space bar in order to get the mouse position logged in the console
which you can then insert as a value for center points  
"""
pixel_to_value_ratio = 1000  # increase to zoom further in
center_point= (-1.755, 0.005)  # change this coordinate to change where the center of the screen should look at
max_iter = 300  # increase this value if you see only black, this value adjusts the color 
screen_width = 800  
screen_height = 600
values = calc_value(
    max_iter, 
    pixel_to_value_ratio=pixel_to_value_ratio, 
    center_point=center_point,
    px_width=screen_width,
    px_height=screen_height
)
pygame.init()


class Game:
    def __init__(self, run=True, bg_color=(0, 0, 0), fps=60, screen_dim=(screen_width, screen_height)):
        self.display = pygame.display.set_mode(screen_dim)
        self.first_time = True
        self.screen_dim = screen_dim
        self.bg_color = bg_color
        self.fps = fps
        pygame.display.set_caption("Mandelbrot Set")
        self.clock = pygame.time.Clock()
        self.is_running = False
        if run:
            self.run()

    def run(self, clean_up=True):
        self.is_running = True
        while self.is_running:
            self.event_handling()
            self.display_handling()

    def event_handling(self):
        global center_point, pixel_to_value_ratio
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    print("mouse pos =", pixel_to_real(*pygame.mouse.get_pos(), pixel_to_value_ratio=pixel_to_value_ratio, center_point=center_point))

    def display_handling(self):
        self.display.fill(self.bg_color)
        for x in range(self.screen_dim[0]):
            for y in range(self.screen_dim[1]):
                self.display.set_at((x, y), values[x, y])
        if self.first_time:
            print("first time render")
            self.first_time = False
        pygame.display.update()
        self.clock.tick(self.fps)

    def clean_up(self):
        pygame.quit()


if __name__ == "__main__":
    g = Game()