import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    def __init__(self, ai_game, alien):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.color = (230, 40, 40)

        self.rect = pygame.Rect(0, 0,
                                self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        self.pos_y = float(self.rect.y)

    def update(self):
        self.pos_y += self.settings.bullet_speed
        self.rect.y = self.pos_y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
