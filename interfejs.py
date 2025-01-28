import pygame
from Przyciski import Przyciski
from Postacie import Bohater
from Postacie import Bohater2

pygame.init()
okno = pygame.display.set_mode((1291, 829))


def pierwszy_swiat():
    run = True
    bohater = Bohater(0, 0) or Bohater2(0, 0)
    zegar = 0
    tlo = pygame.image.load("las.png")
    while run:
        zegar += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

        bohater.tick()

        okno.blit(tlo, (0, 0))
        bohater.draw(okno)
        pygame.display.update()


def lobby():
    run = True
    zegar = 0
    bohater1 = Bohater(500, 500)
    bohater2 = Bohater2(200, 200)
    przyciski = [Przyciski(1000, 600, "Przycisk"),
                 Przyciski(1000, 700, "Wyjdź"),
                 Przyciski(100, 0, "Postac1"),
                 Przyciski(300, 0, "Postac2"),
                 Przyciski(500, 0, "Postac3"),
                 Przyciski(1000, 500, "Multiplayer")
                 ]
    tlo = pygame.image.load("Lobby.png")
    while run:
        zegar += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

        if przyciski[0].tick():
            pierwszy_swiat()
        if przyciski[1].tick():
            run = False

        bohater1.tick()
        bohater2.tick()

        okno.blit(tlo, (0, 0))
        przyciski[0].draw(okno)
        przyciski[1].draw(okno)
        przyciski[2].draw(okno)
        przyciski[3].draw(okno)
        przyciski[4].draw(okno)
        przyciski[5].draw(okno)

        if przyciski[2].tick():
            bohater1.draw(okno)

        if przyciski[3].tick():
            bohater2.draw(okno)

        pygame.display.update()


def main():
    run = True
    zegar = 0
    przyciski = [
        Przyciski(550, 444, "Przycisk"),
        Przyciski(550, 550, "Wyjdź")
    ]
    while run:
        zegar += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if przyciski[0].tick():
            run = True
            lobby()

        if przyciski[1].tick():
            run = False

        okno.blit(pygame.image.load("tło początkowe.png"), (0, 0))
        przyciski[0].draw(okno)
        przyciski[1].draw(okno)
        pygame.display.update()


if __name__ == '__main__':
    main()
