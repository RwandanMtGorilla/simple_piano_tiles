## game.py
import pygame
from tiles import TilesManager
from player import Player
from ui import UIManager

class Game:
    def __init__(self):
        pygame.init()
        initial_x = 400  # 屏幕宽度的一半
        initial_y = 300  # 屏幕高度的一半

        # 在创建 Player 实例时传入这些初始坐标
        self.player = Player(initial_x, initial_y)
        self.tiles_manager = TilesManager()
        self.ui_manager = UIManager()
        self.running = True
        self.clock = pygame.time.Clock()
        self.difficulty = 1
        self.speed = 5
        self.tile_generation_interval = 60  # Frames until new tiles are generated
        self.frames_since_last_generation = 0

    def start_game(self) -> None:
        """Start the game loop."""
        self.ui_manager.display_start_screen()
        self.wait_for_player_to_start()
        self.tiles_manager.generate_tiles(self.difficulty)  # Generate tiles once at the start

        while self.running:
            self.game_loop()

        self.end_game()

    def end_game(self) -> None:
        """End the game and display the end screen."""
        score = self.player.get_score()
        self.ui_manager.display_end_screen(score)
        self.wait_for_player_to_restart_or_quit()

    def restart_game(self) -> None:
        """Restart the game."""
        self.player = Player()
        self.tiles_manager = TilesManager()
        self.frames_since_last_generation = 0
        self.start_game()

    def game_loop(self) -> None:
        """The main loop of the game."""
        self.handle_events()
        self.clock.tick(60)
        self.handle_tile_generation()
        self.tiles_manager.move_tiles(self.speed)
        collision = self.tiles_manager.check_collision(self.player)

        if collision:
            self.player.update_score(1)
        self.ui_manager.update_game_screen(self.tiles_manager.tiles)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按钮被按下
                mouse_pos = pygame.mouse.get_pos()  # 获取鼠标位置
                self.tiles_manager.remove_tile_on_click(mouse_pos)

    def handle_tile_generation(self) -> None:
        """Handle the generation of new tiles at set intervals."""
        self.frames_since_last_generation += 1
        if self.frames_since_last_generation >= self.tile_generation_interval:
            self.tiles_manager.generate_tiles(self.difficulty)
            self.frames_since_last_generation = 0

    def handle_events(self) -> None:
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def wait_for_player_to_start(self) -> None:
        """Wait for the player to press any key to start the game."""
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def wait_for_player_to_restart_or_quit(self) -> None:
        """Wait for the player to restart the game or quit."""
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart_game()
                    elif event.key == pygame.K_q:
                        self.running = False
                        waiting = False
                elif event.type == pygame.QUIT:
                    self.running = False
                    waiting = False

if __name__ == "__main__":
    game = Game()
    game.start_game()
