import sys
import pygame
from setting import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()

        # controlling Frame rates
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # set into full screen
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            
            # controlling Frame rates 60F/s
            self.clock.tick(60)

    def _check_events(self):
        # respond to keypress and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Properly quit Pygame
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                 # here key down mean key is clicked/pressed
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                # keyup mean key is released
                self._check_keyup_events(event)
                

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            ## MOVE ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        if event.key ==  pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
         


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # update the screen changes
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
