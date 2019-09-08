import numpy as np

from model.tool import Tool
from util import global_config


def run(world, generation):
    prob = global_config.get_var('tool_development.probability')
    for pop in world.populations:
        if np.random.binomial(pop.size, prob) <= 0:
            continue
        new_tool = generate_tool(generation)
        pop.add_tool(new_tool)

def generate_tool(generation):
    id = Tool.generate_id()
    selection_coefficient
    return Tool(id, generation, selection_coeffient)