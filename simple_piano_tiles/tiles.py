## tiles.py
import random
from typing import List
from player import Player

class Tile:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0, 0, 0)  # Default color is black for the tile

    def move(self, speed: int):
        """Move the tile down the screen.

        Args:
            speed (int): The speed at which the tile moves.
        """
        self.y += speed

class TilesManager:
    def __init__(self, screen_width: int = 800, screen_height: int = 600):
        self.tiles: List[Tile] = []  # List to store the tiles
        self.tile_width = 100  # Default tile width
        self.tile_height = 200  # Default tile height
        self.screen_width = screen_width
        self.screen_height = screen_height

    def generate_tiles(self, difficulty: int = 1) -> None:
        """Generate a new set of tiles based on the difficulty.

        Args:
            difficulty (int, optional): The game difficulty level. Defaults to 1.
        """
        num_tiles = difficulty * 2
        for _ in range(num_tiles):
            x = random.randint(0, self.screen_width - self.tile_width)
            y = -random.randint(self.tile_height, self.screen_height * 2)
            new_tile = Tile(x, y, self.tile_width, self.tile_height)
            self.tiles.append(new_tile)

    def move_tiles(self, speed: int = 5) -> None:
        """Move all the tiles down the screen.

        Args:
            speed (int, optional): The speed at which the tiles move. Defaults to 5.
        """
        for tile in self.tiles:
            tile.move(speed)

    def check_collision(self, player: Player) -> bool:
        """Check if the player has collided with any of the tiles.

        Args:
            player (Player): The player object to check for collisions.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        for tile in self.tiles:
            if (tile.x < player.x < tile.x + tile.width and
                    tile.y < player.y < tile.y + tile.height):
                return True
        return False

    # 在 TilesManager 类中添加以下方法

    def remove_tile_on_click(self, mouse_pos):
        """Remove a tile if it is clicked by the mouse.

        Args:
            mouse_pos (tuple): The (x, y) position of the mouse click.
        """
        x, y = mouse_pos
        self.tiles = [tile for tile in self.tiles if
                      not (tile.x < x < tile.x + tile.width and tile.y < y < tile.y + tile.height)]

