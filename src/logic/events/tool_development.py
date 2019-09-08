import math
import random

import numpy as np

from model.tool import Tool
from util import global_config


def run(world, generation):
    prob = global_config.get_var('tool_development.probability')
    for pop in world.populations:
        if np.random.binomial(pop.size, prob) <= 0:
            continue
        new_tool = generate_tool(generation)
        print("Population %s developed a great new tool: %s! sc=%.3f" % (pop.id, new_tool.id, new_tool.sc))
        world.tools_repo.register_tool(new_tool)
        pop.add_tool(new_tool.id)


def generate_tool(generation):
    id = Tool.generate_id()
    sc_distribution_func = global_config.get_var('tool_development.sc_func')
    x = random.random()
    sc = eval(sc_distribution_func)
    return Tool(id, generation, sc)
