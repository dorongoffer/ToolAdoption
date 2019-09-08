import random
import math
from faker import Faker
from util import global_config
from util.json_serializer import jsonify

faker = Faker()


class Tool(object):
    def __init__(self, tool_id, generation, sc):
        self.id = tool_id
        self.created_at = generation
        self.sc = sc  # selection_coefficient
        self.abandoned_at = None

    def __str__(self):
        return jsonify(self.__dict__)

    def is_abandoned(self):
        return self.abandoned_at is not None

    @staticmethod
    def generate_instance(generation=0):
        tool_id = Tool.generate_id()
        sc_distribution_func = global_config.get_var('sc_func')
        x = random.random()
        sc = eval(sc_distribution_func)
        return Tool(tool_id, generation, sc)

    @staticmethod
    def from_config(tool_config):
        tool_id = tool_config['id'] if 'id' in tool_config else Tool.generate_id()
        return Tool(tool_id, 0, tool_config['sc'])

    @staticmethod
    def generate_id():
        return "{} {}".format(faker.color_name(), faker.word())
