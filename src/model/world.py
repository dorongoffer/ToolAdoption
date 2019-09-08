import json
import math
import random

from faker import Faker

from model.population import Population
from model.tool import Tool
from util.json_serializer import JsonSerializer
from util.tools_repo import ToolsRepo

faker = Faker()


class World(object):
    def __init__(self):
        self.tools_repo = ToolsRepo()
        self.populations = []

    def __str__(self):
        return json.dumps(self, cls=JsonSerializer, indent=2, sort_keys=True)

    @staticmethod
    def from_config(world_config):
        world = World()
        if 'tools' in world_config:
            for t in world_config['tools']:
                tool = Tool.from_config(t)
                world.tools_repo.register_tool(tool)

        if 'populations' in world_config:
            for p in world_config['populations']:
                population = Population.from_config(p)
                world.populations.append(population)

        if len(world.populations) == 0:
            for i in range(0, world_config['populations_count']):
                pop_id = Population.generate_id()
                size = random.randint(world_config['min_pop_size'], world_config['max_pop_size'])
                world.populations.append(Population(pop_id, size))

        if len(world.tools_repo) == 0:
            min_adopting = 1
            max_adopting = round(math.sqrt(len(world.populations)))
            for i in range(0, world_config['tools_count']):
                tool = Tool.generate_instance()
                world.tools_repo.register_tool(tool)
                adopting_pops = random.randint(min_adopting, max_adopting)
                adopters = random.sample(world.populations, adopting_pops)
                [pop.adopt_tool(tool.id) for pop in adopters]

        return world
