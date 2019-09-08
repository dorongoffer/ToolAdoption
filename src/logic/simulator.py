import importlib
from util import global_config


class Simulator(object):
    def __init__(self, world, generational_events=[]):
        self.world = world
        self.generational_events = generational_events

    def run(self):
        simulation_length = global_config.get_var('simulation_length') + 1
        for gen in range(1, simulation_length):
            print("Generation %d" % gen)
            for event in self.generational_events:
                event_module = importlib.import_module("logic.events." + event)
                event_module.run(self.world, gen)
