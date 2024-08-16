import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and do rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # set ship at bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x =float(self.rect.x)
        # FOR Moving right
        self.moving_right = False

        # for moving left
        self.moving_left = False

    def blitme(self):
        # draw screen at its current location
        self.screen.blit(self.image,self.rect)


    def update(self):
        # update position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
