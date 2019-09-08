import random
from functools import reduce
from util import global_config


def run(world, generation):
    base_prob = global_config.get_var('tool_abandonment.probability')
    for tool in filter(lambda t: not t.is_abandoned(), world.tools_repo):
        populations = list(filter(lambda pop: pop.is_adopted(tool.id), world.populations))
        sizes = map(lambda pop: pop.size, populations)
        adopters = reduce((lambda x, y: x + y), sizes)
        prob = base_prob / adopters
        if random.random() < prob:
            print("Tool Abandonment: {} abandoned by {} adopters across {} populations :(".format(tool.id, adopters, len(populations)))
            [pop.abandon_tool(tool.id) for pop in populations]
            world.tools_repo.mark_abandoned(tool.id, generation)
