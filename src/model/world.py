import json

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
        for t in world_config['tools']:
            tool = Tool.from_config(t)
            world.tools_repo.register_tool(tool)

        for p in world_config['populations']:
            population = Population.from_config(p)
            world.populations.append(population)

        return world
