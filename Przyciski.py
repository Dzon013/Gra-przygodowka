import pygame


class Przyciski:
    def __init__(self, x, y, file_name):
        self.x_cord = x
        self.y_cord = y
        self.zdjecie_przycisku = pygame.image.load(f"Przyciski/{file_name}_wl.png")
        self.zdjecie_nacisnietego_przycisku = pygame.image.load(f"Przyciski/{file_name}_wyl.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.zdjecie_przycisku.get_width(),
                                  self.zdjecie_przycisku.get_height())

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw(self, okno):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            okno.blit(self.zdjecie_nacisnietego_przycisku, (self.x_cord, self.y_cord))
        else:
            okno.blit(self.zdjecie_przycisku, (self.x_cord, self.y_cord))
