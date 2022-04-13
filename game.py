import pygame
import pytmx
import pyscroll

from Firstgame.player import Player


class Game:
    def __init__(self):

        # Création de fenêtre de jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("First Game")

        # Charge la carte
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)

        # Recupère la taille
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # Genere le player
        # Recupere l'objet instancier du joueur dans tiled qui permet de le faire pop
        player_position = tmx_data.get_object_by_name("playeurstart")
        self.player = Player(player_position.x, player_position.y)

        # layer
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def run(self):

        # laisse ouvert la fenêtre
        running = True
        while running:

            self.group.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
