import pygame


class Bohater:
    def __init__(self, x, y):
        # self.imie = imie
        self.x = x
        self.y = y
        self.grafika = pygame.image.load("Bohater/stand.png")
        self.wysokosc = self.grafika.get_height()
        self.szerokosc = self.grafika.get_width()
        self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.predkosc = 10

    def tick(self):
        klawisze = pygame.key.get_pressed()
        if klawisze[pygame.K_w]:
            self.y -= self.predkosc
        if klawisze[pygame.K_s]:
            self.y += self.predkosc
        if klawisze[pygame.K_a]:
            self.x -= self.predkosc
        if klawisze[pygame.K_d]:
            self.x += self.predkosc

    def draw(self, okno):
        okno.blit(self.grafika, (self.x, self.y))


class Bohater2:
    def __init__(self, x, y):
        # self.imie = imie
        self.x = x
        self.y = y
        self.grafika = pygame.image.load("Bohater.png")
        self.wysokosc = self.grafika.get_height()
        self.szerokosc = self.grafika.get_width()
        self.hitbox = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.predkosc = 10

    def tick(self):
        klawisze = pygame.key.get_pressed()
        if klawisze[pygame.K_UP]:
            self.y -= self.predkosc
        if klawisze[pygame.K_DOWN]:
            self.y += self.predkosc
        if klawisze[pygame.K_LEFT]:
            self.x -= self.predkosc
        if klawisze[pygame.K_RIGHT]:
            self.x += self.predkosc

    def draw(self, okno):
        okno.blit(self.grafika, (self.x, self.y))
