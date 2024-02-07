## main.py
import pygame
from game import Game

class Main:
    @staticmethod
    def main():
        """The main entry point of the application."""
        pygame.init()
        game_instance = Game()
        game_instance.start_game()

# Check if this is the main module being run and, if so, start the game.
if __name__ == "__main__":
    Main.main()
