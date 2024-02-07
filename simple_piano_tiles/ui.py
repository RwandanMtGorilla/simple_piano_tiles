## ui.py
import pygame
from typing import List
from tiles import Tile

class UIManager:
    def __init__(self, screen_width: int = 800, screen_height: int = 600):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.font = pygame.font.Font(None, 36)

    def display_start_screen(self) -> None:
        """Display the start screen of the game."""
        self.screen.fill((255, 255, 255))  # Fill the screen with white
        text = self.font.render('按任意键开始', True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.screen_width / 2, self.screen_height / 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def display_game_screen(self, tiles: List[Tile]) -> None:
        """Display the game screen with the current tiles.

        Args:
            tiles (List[Tile]): The list of tiles to display.
        """
        self.screen.fill((255, 255, 255))  # Fill the screen with white
        for tile in tiles:
            pygame.draw.rect(self.screen, tile.color, (tile.x, tile.y, tile.width, tile.height))
        pygame.display.flip()

    def display_end_screen(self, score: int) -> None:
        """Display the end screen with the player's score.

        Args:
            score (int): The score to display.
        """
        self.screen.fill((255, 255, 255))  # Fill the screen with white
        text = self.font.render(f'游戏结束！你的得分: {score}', True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.screen_width / 2, self.screen_height / 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def update_game_screen(self, tiles: List[Tile]) -> None:
        """Update the game screen with the current tiles.

        Args:
            tiles (List[Tile]): The list of tiles to display.
        """
        self.display_game_screen(tiles)
