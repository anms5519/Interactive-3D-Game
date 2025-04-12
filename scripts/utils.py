# utils.py

import unreal_engine as ue
from unreal_engine.classes import Actor

def log_message(message):
    ue.log(message)

def get_actor_location(actor):
    if isinstance(actor, Actor):
        return actor.get_actor_location()
    else:
        ue.log("Invalid actor")
        return None

def set_actor_location(actor, location):
    if isinstance(actor, Actor):
        actor.set_actor_location(location)
    else:
        ue.log("Invalid actor")

def get_distance_between_actors(actor1, actor2):
    if isinstance(actor1, Actor) and isinstance(actor2, Actor):
        location1 = actor1.get_actor_location()
        location2 = actor2.get_actor_location()
        return (location1 - location2).size()
    else:
        ue.log("Invalid actors")
        return None
