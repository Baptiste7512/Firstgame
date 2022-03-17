import pygame
import pytmx
import pyscroll


class Game:
    def __init__(self):

        # Création de fenêtre de jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("First Game")

        # Charge la carte
        tmx_data = pytmx.util_pygame.load_pygame("Map.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)

        # Recupère la taille
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # layer
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):

        # laisse ouvert la fenêtre
        running = True
        while running:

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
