# game_logic.py

import unreal_engine as ue
from unreal_engine.classes import Character, PlayerController
from unreal_engine.enums import EInputEvent

class GameLogic:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.game_state = "INIT"

    def start_game(self):
        self.game_state = "RUNNING"
        self.spawn_player()
        self.spawn_enemies()

    def spawn_player(self):
        self.player = ue.get_editor_world().actor_spawn(Character)
        ue.log("Player spawned")

    def spawn_enemies(self):
        for i in range(5):
            enemy = ue.get_editor_world().actor_spawn(Character)
            self.enemies.append(enemy)
            ue.log(f"Enemy {i+1} spawned")

    def on_player_input(self, key, event):
        if event == EInputEvent.IE_Pressed:
            if key == "W":
                self.player.add_movement_input(ue.Vector(1, 0, 0))
            elif key == "S":
                self.player.add_movement_input(ue.Vector(-1, 0, 0))
            elif key == "A":
                self.player.add_movement_input(ue.Vector(0, -1, 0))
            elif key == "D":
                self.player.add_movement_input(ue.Vector(0, 1, 0))

    def update(self, delta_time):
        if self.game_state == "RUNNING":
            self.check_game_over()

    def check_game_over(self):
        if not self.player.is_alive():
            self.game_state = "GAME_OVER"
            ue.log("Game Over")
