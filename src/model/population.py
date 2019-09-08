import json

from faker import Faker
faker = Faker()


class Population(object):
    def __init__(self, pop_id, size):
        self.id = pop_id
        self.size = size
        self.tools = set()

    def add_tool(self, tool_id):
        if not isinstance(tool_id, str):
            raise Exception("add_tool accepts tool id, not an actual tool")

        self.tools.add(tool_id)

    def adopt_tools(self, tool_ids):
        [self.add_tool(tool_id) for tool_id in tool_ids]

    @staticmethod
    def from_config(pop_config):
        pop_id = pop_config['id'] if 'id' in pop_config else Population.next_id()
        size = pop_config['size']
        pop = Population(pop_id, size)
        [pop.add_tool(tool_id) for tool_id in pop_config['tools']]
        return pop

    @staticmethod
    def next_id():
        return faker.last_name()
