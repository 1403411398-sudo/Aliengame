import pygame
from pygame.sprite import Sprite

class Shield(Sprite):
    """玩家飞船前方的护盾，可被子弹摧毁"""

    def __init__(self, ai_game, x, y):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.color = (50, 200, 50)
        self.width = 90
        self.height = 25
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = (x, y)
        self.hp = 4

    def hit(self):
        """被子弹命中一次"""
        self.hp -= 1

        fade = max(0, 255 - (4 - self.hp) * 40)
        self.color = (50, fade, 50)

        if self.hp <= 0:
            self.kill()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
