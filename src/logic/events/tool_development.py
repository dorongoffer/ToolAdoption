import numpy as np
from model.tool import Tool
from util import global_config


def run(world, generation):
    prob = global_config.get_var('tool_development.probability')
    for pop in world.populations:
        if np.random.binomial(pop.size, prob) <= 0:
            continue
        new_tool = Tool.generate_instance(generation)
        print("Tool Development: population %s developed the mighty '%s' (coeff=%.3f)." % (pop.id, new_tool.id, new_tool.sc))
        world.tools_repo.register_tool(new_tool)
        pop.adopt_tool(new_tool.id)
