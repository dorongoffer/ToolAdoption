import json
import random

from faker import Faker

from util import global_config

faker = Faker()


class Population(object):
    def __init__(self, pop_id, size):
        self.id = pop_id
        self.size = size
        self.tools = set()

    def adopt_tool(self, tool_id):
        if not isinstance(tool_id, str):
            raise Exception("adopt_tool accepts tool id, not an actual tool")

        self.tools.add(tool_id)

    def adopt_tools(self, tool_ids):
        [self.adopt_tool(tool_id) for tool_id in tool_ids]

    def is_adopted(self, tool_id):
        return tool_id in self.tools

    def abandon_tool(self, tool_id):
        self.tools.remove(tool_id)

    @staticmethod
    def from_config(pop_config):
        pop_id = pop_config['id'] if 'id' in pop_config else Population.generate_id()
        size = pop_config['size']
        pop = Population(pop_id, size)
        [pop.adopt_tool(tool_id) for tool_id in pop_config['tools']]
        return pop

    @staticmethod
    def generate_id():
        return "{}{}".format(faker.last_name(), random.randint(1, 1000))
