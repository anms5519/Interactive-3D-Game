# ai.py

import unreal_engine as ue
from unreal_engine.classes import AIController, Character
from unreal_engine.enums import EPathFollowingRequestResult

class AIBehavior:
    def __init__(self, character):
        self.character = character
        self.controller = ue.get_editor_world().actor_spawn(AIController)
        self.controller.possess(self.character)

    def move_to_target(self, target):
        result = self.controller.move_to_actor(target)
        if result == EPathFollowingRequestResult.RequestSuccessful:
            ue.log("AI moving to target")
        else:
            ue.log("AI failed to move to target")

    def attack_target(self, target):
        if self.character.is_in_attack_range(target):
            self.character.attack(target)
            ue.log("AI attacking target")
        else:
            self.move_to_target(target)

    def update(self, delta_time):
        # Update AI behavior here
        pass
