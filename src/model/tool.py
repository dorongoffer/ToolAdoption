import json

from faker import Faker

faker = Faker()


class Tool(object):
    def __init__(self, tool_id, generation, sc):
        self.id = tool_id
        self.generation = generation
        self.sc = sc  # selection_coefficient

    @staticmethod
    def from_config(tool_config):
        tool_id = tool_config['id'] if 'id' in tool_config else Tool.generate_id()
        return Tool(tool_id, 0, tool_config['selection_coeffient'])

    @staticmethod
    def generate_id():
        return faker.color_name()
